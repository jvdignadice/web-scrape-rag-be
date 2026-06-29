import httpx

class OllamaEmbedder:
    def __init__(self, model="nomic-embed-text"):
        self.model = model

    async def embed(self, text: str):
        async with httpx.AsyncClient() as client:
            res = await client.post(
                "http://localhost:11434/api/embeddings",
                json={
                    "model": self.model,
                    "prompt": text
                }
            )
        return res.json()["embedding"]