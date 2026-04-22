<<<<<<< HEAD
# Task 2 — Text Chunking

## Overview
Splits extracted PDF text into smaller chunks and stores them in MongoDB for efficient search.

---

## Process
- Read from `pdf_documents`
- Extract text (`pages` or `raw_text`)
- Split into chunks (with overlap)
- Store in `chunked_documents`

---

## Database

**Input**
- DB: `trip_planner`
- Collection: `pdf_documents`

**Output**
- DB: `trip_planner`
- Collection: `chunked_documents`

---

## Output Format

```json
{
  "file_name": "sample.pdf",
  "chunk_index": 1,
  "content": "text chunk...",
  "created_at": "timestamp"
}
=======
# Task 2 — Text Chunking

## Overview
Splits extracted PDF text into smaller chunks and stores them in MongoDB for efficient search.

---

## Process
- Read from `pdf_documents`
- Extract text (`pages` or `raw_text`)
- Split into chunks (with overlap)
- Store in `chunked_documents`

---

## Database

**Input**
- DB: `trip_planner`
- Collection: `pdf_documents`

**Output**
- DB: `trip_planner`
- Collection: `chunked_documents`

---

## Output Format

```json
{
  "file_name": "sample.pdf",
  "chunk_index": 1,
  "content": "text chunk...",
  "created_at": "timestamp"
}
>>>>>>> 1cf7b0d1eb73b503fee403cc834ec4d4f54cd372
