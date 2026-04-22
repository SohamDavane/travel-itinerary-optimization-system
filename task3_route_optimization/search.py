import os
from dotenv import load_dotenv
import pymongo
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from typing import List, Dict

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
DB_NAME = os.getenv('DB_NAME', 'trip_planner')
COLLECTION_NAME = os.getenv('COLLECTION_NAME', 'chunked_documents')
MODEL_NAME = os.getenv('MODEL_NAME', 'all-MiniLM-L6-v2')
DIM = 384

class SemanticSearch:
    def __init__(self):
        self.client = pymongo.MongoClient(MONGO_URI)
        self.collection = self.client[DB_NAME][COLLECTION_NAME]
        self.model = SentenceTransformer(MODEL_NAME)
        self.index = None
        self.texts = []
        self._load_index()

    def _load_index(self):
        docs = list(self.collection.find({'embedding': {'$exists': True}}, {'embedding':1, 'chunk_text':1}))
        if not docs:
            print('No embeddings found. Lazy load later.')
            self.index = None
            self.texts = []
            return

        embeddings = np.array([d['embedding'] for d in docs], dtype='float32')
        self.texts = [d['chunk_text'] for d in docs]
        
        self.index = faiss.IndexFlatIP(DIM)
        self.index.add(embeddings)
        print(f'FAISS index loaded with {len(docs)} vectors')

    def search(self, query: str, k: int = 5) -> List[Dict]:
        if self.index is None:
            return []
        q_emb = self.model.encode([query], normalize_embeddings=True, convert_to_numpy=True)
        scores, indices = self.index.search(q_emb, k)
        results = []
        for score, idx in zip(scores[0], indices[0]):
            if idx < len(self.texts):
                results.append({'text': self.texts[idx], 'score': float(score)})
        return results[:5]


    def close(self):
        self.client.close()


if __name__ == '__main__':
    searcher = SemanticSearch()
    print(searcher.search('test query'))
    searcher.close()

