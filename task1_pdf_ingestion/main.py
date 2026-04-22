import fitz  # PyMuPDF
import pymongo
import os
from datetime import datetime, UTC

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["trip_planner"]
collection = db["pdf_documents"]

# Create index to prevent duplicate PDFs
collection.create_index("file_name", unique=True)


#  Read PDF and extract page-wise text
def read_pdf(file_path):
    doc = fitz.open(file_path)

    pages = []

    for page_number, page in enumerate(doc, start=1):
        pages.append({
            "page_number": page_number,
            "text": page.get_text()
        })

    return pages, len(doc)


# Store PDF data into MongoDB 
def store_pdf(file_path):
    file_name = os.path.basename(file_path)
    abs_path = os.path.abspath(file_path)

    # Check if PDF already exists
    if collection.find_one({"file_name": file_name}):
        print(f"{file_name} already exists in database. Skipping.\n")
        return

    print(f"Reading: {file_name}...")

    try:
        pages, page_count = read_pdf(file_path)
    except Exception as e:
        print(f"Error reading {file_name}: {e}\n")
        return

    document = {
        "file_name": file_name,
        "file_path": abs_path,
        "total_pages": page_count,
        "pages": pages,
        "status": "extracted",
        "created_at": datetime.now(UTC)
    }

    try:
        result = collection.insert_one(document)

        # Update file path after insert (task requirement)
        collection.update_one(
            {"_id": result.inserted_id},
            {"$set": {"file_path": abs_path}}
        )

        print(f"  Stored : {file_name}")
        print(f"  ID     : {result.inserted_id}")
        print(f"  Pages  : {page_count}")
        print(f"  Path   : {abs_path}\n")

    except pymongo.errors.DuplicateKeyError:
        print(f"{file_name} already exists. Skipping.\n")


# Run on all PDFs in the pdfs folder
def main():
    pdf_folder = os.path.join(os.path.dirname(__file__), "pdfs")

    if not os.path.exists(pdf_folder):
        print("pdfs folder not found.")
        return

    pdf_files = [f for f in os.listdir(pdf_folder) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print("No PDF files found in the pdfs/ folder.")
        print("Please add your PDF files to: task1_soham/pdfs/")
        return

    print(f"Found {len(pdf_files)} PDF(s). Starting extraction...\n")

    for file in pdf_files:
        store_pdf(os.path.join(pdf_folder, file))

    print("All PDFs processed and stored in MongoDB successfully.")
    print("Database   : trip_planner")
    print("Collection : pdf_documents")


if __name__ == "__main__":
    main()