from fastapi import APIRouter
from ollama import Client
from app.embeddings import ollama_embedder
from app.vectorstore import quadrant_client
import uuid

embedder = ollama_embedder.OllamaEmbedder()
router = APIRouter()
client = Client()
qdrant_client = quadrant_client.QdrantService()


@router.post("/ask")
async def ask_question(question: str):
    embedding = await embedder.embed(question)
    chunked_embedding = embedding[:512]
    point_id = str(uuid.uuid4())
    await qdrant_client.upsert_point("web-scrape-rag-collection-1", point_id, chunked_embedding, question)
    messages = [
    {
    'role': 'user',
    'content': question,
    },
    ]
    response = ''
    for part in client.chat('qwen2.5:7b', messages=messages, stream=True):
        response += part.message.content
    return {
        "question": question,
        "answer": response
    }


async def store_valid_resource(list_of_resources: list[str]):
    for resource in list_of_resources:
        embedding = await embedder.embed(resource)
        chunked_embedding = embedding[:512]
        point_id = str(uuid.uuid4())
        await qdrant_client.upsert_point("web-scrape-rag-collection-1", point_id, chunked_embedding, resource)






