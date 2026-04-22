import os
from dotenv import load_dotenv
import pymongo
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
DB_NAME = os.getenv('DB_NAME', 'trip_planner')
COLLECTION_NAME = os.getenv('COLLECTION_NAME', 'chunked_documents')
MODEL_NAME = os.getenv('MODEL_NAME', 'all-MiniLM-L6-v2')

client = pymongo.MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

model = SentenceTransformer(MODEL_NAME)

def generate_embeddings():
    chunks = list(collection.find({'embedding': {'$exists': False}}))
    if not chunks:
        print('All chunks have embeddings')
        return

    print(f'Generating {len(chunks)} embeddings...')
    texts = [chunk['content'] for chunk in chunks]
    embeddings = model.encode(texts, batch_size=32, show_progress_bar=True, normalize_embeddings=True)

    for chunk, emb in zip(chunks, embeddings):
        collection.update_one(
            {'_id': chunk['_id']},
            {'$set': {
                'chunk_text': chunk['content'],
                'embedding': emb.tolist()
            }}
        )

    print('Embeddings generated!')

if __name__ == '__main__':
    generate_embeddings()
    client.close()

