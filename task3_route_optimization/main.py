import os
from dotenv import load_dotenv
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from typing import Dict, List, Any
from search import SemanticSearch

load_dotenv()

from typing import Optional

searcher: Optional[SemanticSearch] = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global searcher
    try:
        searcher = SemanticSearch()
    except Exception as e:
        print(f'Searcher init failed: {e}. Run embedding_generator.py')
        searcher = None
    yield
    if searcher:
        searcher.close()


app = FastAPI(title='Semantic Search API', docs_url='/docs', redoc_url='/redoc', lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get('/health')
async def health():
    return {'status': 'OK'}

@app.get('/search')
async def search(query: str = Query(..., min_length=1)):
    global searcher
    if searcher is None:
        raise HTTPException(503, 'No embeddings. Run python embedding_generator.py first')
    try:
        results = searcher.search(query)
        return {'results': results}
    except Exception as e:
        raise HTTPException(500, str(e))


if __name__ == '__main__':
    import uvicorn
    print('FastAPI running:')
    print('  - http://localhost:8001/docs')
    print('  - http://localhost:8001/health') 
    print('  - http://127.0.0.1:8001/search?query=test')
    uvicorn.run(app, host='127.0.0.1', port=8001)

