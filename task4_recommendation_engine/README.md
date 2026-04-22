<<<<<<< HEAD
﻿# Task 4 - Recommendation Engine/ Fast Api generation 


## Overview
Implements a FastAPI-based search API that retrieves relevant results from chunked documents stored in MongoDB for efficient querying.

---

## Process
- Read user query from API request  
- Process query text  
- Search in `chunked_documents` collection  
- Rank and filter results  
- Return top matches  

---

## API Endpoints

### POST `/search`
Search for relevant documents

#### Request Body
```
{
  "query": "best places in mumbai"
}

#### RESPONSE

{
  "results": [
    {
      "text": "Marine Drive is a popular tourist spot...",
      "score": 0.89
    }
  ]
}
```
### Project Structure
```
task3_fastapi_search/
├── main.py
├── database.py

```
## How to Run

1. Clone the repository
```bash
git clone <your-repo-url>
cd travel-itinerary-optimization-system
```

2. Create virtual environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate   # For Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run FastAPI server
```bash
uvicorn task3_fastapi_search.main:app --reload
```
----

## Testing

### Using Postman

- Method: **POST**
- URL: `http://127.0.0.1:8000/search`
- Body → raw → JSON:

```json
{
  "query": "best places in mumbai"
}
```

### Expected Response

```json
{
  "results": [
    {
      "text": "Marine Drive is a popular tourist spot...",
      "score": 0.89
    }
  ]
}
```
## Conclusion

The FastAPI Search module enables efficient and structured retrieval of information from pre-processed text chunks. By integrating API-based querying with MongoDB storage, the system ensures fast and relevant results, making it suitable for real-world applications like travel planning and recommendation engines.
=======
﻿# Task 4 - Recommendation Engine/ Fast Api generation 


## Overview
Implements a FastAPI-based search API that retrieves relevant results from chunked documents stored in MongoDB for efficient querying.

---

## Process
- Read user query from API request  
- Process query text  
- Search in `chunked_documents` collection  
- Rank and filter results  
- Return top matches  

---

## API Endpoints

### POST `/search`
Search for relevant documents

#### Request Body
```
{
  "query": "best places in mumbai"
}

#### RESPONSE

{
  "results": [
    {
      "text": "Marine Drive is a popular tourist spot...",
      "score": 0.89
    }
  ]
}
```
### Project Structure
```
task3_fastapi_search/
├── main.py
├── database.py

```
## How to Run

1. Clone the repository
```bash
git clone <your-repo-url>
cd travel-itinerary-optimization-system
```

2. Create virtual environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate   # For Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run FastAPI server
```bash
uvicorn task3_fastapi_search.main:app --reload
```
----

## Testing

### Using Postman

- Method: **POST**
- URL: `http://127.0.0.1:8000/search`
- Body → raw → JSON:

```json
{
  "query": "best places in mumbai"
}
```

### Expected Response

```json
{
  "results": [
    {
      "text": "Marine Drive is a popular tourist spot...",
      "score": 0.89
    }
  ]
}
```
## Conclusion

The FastAPI Search module enables efficient and structured retrieval of information from pre-processed text chunks. By integrating API-based querying with MongoDB storage, the system ensures fast and relevant results, making it suitable for real-world applications like travel planning and recommendation engines.
>>>>>>> 1cf7b0d1eb73b503fee403cc834ec4d4f54cd372
