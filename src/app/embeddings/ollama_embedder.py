import httpx
from dotenv import load_dotenv
import os

load_dotenv()

emedding_api = os.getenv("EMBEDDDING_API")

class OllamaEmbedder:
    def __init__(self, model="nomic-embed-text"):
        self.model = model

    async def embed(self, text: str):
        async with httpx.AsyncClient() as client:
            res = await client.post(
                emedding_api,
                json={
                    "model": self.model,
                    "prompt": text
                }
            )
        return res.json()["embedding"]