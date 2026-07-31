# Web Scrape RAG Backend

This is the backend service for the Web Scrape RAG project. It provides FastAPI endpoints for scraping, RAG-based retrieval, and user/role management.

## Project structure

- `src/app/main.py` - FastAPI application entry point
- `src/app/api/` - API routers and route handlers
- `src/app/ingestion/` - scraping and ingestion logic
- `src/app/embeddings/` - embedding generation
- `src/app/vectorstore/` - vector storage integration
- `src/app/db/` - database-related modules

## Requirements

- Python 3.10+
- Virtual environment support

## Run locally

From the project root:

```bash
cd src
source .venv/bin/activate
uvicorn app.main:app --reload
```

The API will be available at:

- http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs

## Health check

You can verify the service is running with:

```bash
curl http://127.0.0.1:8000/
```

Expected response:

```json
{"status": "ok"}
```

## Optional: install dependencies

If you need to recreate the environment:

```bash
cd src
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
deactivate
```
