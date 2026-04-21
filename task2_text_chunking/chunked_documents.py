import pymongo
from datetime import datetime, UTC

# ------------------ DB CONNECTION ------------------ #
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["trip_planner"]

source_collection = db["pdf_documents"]
chunk_collection = db["chunked_documents"]

# Prevent duplicate chunks
chunk_collection.create_index(
    [("file_name", 1), ("chunk_index", 1)],
    unique=True
)


# ------------------ CHUNKING ------------------ #
def chunk_text(text, chunk_size=400, overlap=50):
    words = text.split()
    chunks = []

    step = chunk_size - overlap
    for i in range(0, len(words), step):
        chunk = words[i:i + chunk_size]
        if chunk:
            chunks.append(" ".join(chunk))

    return chunks


# ------------------ TEXT EXTRACTION ------------------ #
def extract_text(doc):
    if "raw_text" in doc and doc["raw_text"].strip():
        return doc["raw_text"]

    if "pages" in doc:
        return " ".join(p.get("text", "") for p in doc["pages"]).strip()

    return None


# ------------------ MAIN PROCESS ------------------ #
def process_documents():
    docs = source_collection.find()

    for doc in docs:
        file_name = doc.get("file_name", "unknown")
        print(f"Processing: {file_name}")

        full_text = extract_text(doc)

        if not full_text:
            print("  Skipped → No usable text\n")
            continue

        chunks = chunk_text(full_text)

        inserted = 0

        for idx, chunk in enumerate(chunks):
            try:
                chunk_collection.insert_one({
                    "file_name": file_name,
                    "chunk_index": idx,
                    "content": chunk,
                    "created_at": datetime.now(UTC)
                })
                inserted += 1

            except pymongo.errors.DuplicateKeyError:
                continue

        print(f"  → {inserted} chunks stored\n")


# ------------------ RUN ------------------ #
if __name__ == "__main__":
    process_documents()