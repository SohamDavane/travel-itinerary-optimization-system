# Task 1 — Soham: Read PDFs & Store in MongoDB

## What This Does
- Reads all PDF files from the `pdfs/` folder
- Extracts full text from each PDF using PyMuPDF
- Stores each PDF as a document in MongoDB
- Updates the file path in MongoDB after storing

## Folder Structure
```
task1_soham/
├── main.py           ← Your main script (run this)
├── requirements.txt  ← Libraries to install
├── README.md         ← This file
└── pdfs/             ← Put your PDF files here
```

## Setup & Run

### 1. Install dependencies
```
pip install -r requirements.txt
```

### 2. Add your PDF files
Drop your PDF files into the `pdfs/` folder.

### 3. Make sure MongoDB is running
```
mongod
```

### 4. Run the script
```
python main.py
```

## MongoDB Output
- Database   : `trip_planner`
- Collection : `pdf_documents`

Each document will look like:
```json
{
  "file_name"   : "mumbai_guide.pdf",
  "file_path"   : "/absolute/path/to/file.pdf",
  "total_pages" : 42,
  "raw_text"    : "Full extracted text...",
  "status"      : "extracted",
  "created_at"  : "2026-04-17T10:00:00"
}
```

## Handover to Yashada (Task 2)
Tell her:
- Database   : trip_planner
- Collection : pdf_documents
- Key field  : raw_text  (this is what she chunks)
