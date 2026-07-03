from qdrant_client import QdrantClient
from qdrant_client.http import models
from dotenv import load_dotenv
import os
import uuid
import asyncio

load_dotenv()
quadrant_host = os.getenv("QUADRANT_HOST")
quadrant_port = int(os.getenv("QUADRANT_PORT"))

class QdrantService:
    def __init__(self, host=quadrant_host, port=quadrant_port):
        self.client = QdrantClient(host=host, port=port)

    async def upsert_point(self, collection_name, point_id, vector, question):
        await asyncio.to_thread(
            self._upsert_point_sync,
            collection_name,
            point_id,
            vector,
            question
        )

    def _upsert_point_sync(self, collection_name, point_id, vector, question):
        self.client.upsert(
            collection_name=collection_name,
            points=[
                models.PointStruct(
                    id=point_id,
                    payload={"question": question,
                                "id":point_id
                    },
                    vector={
                        "dense-vector": vector
                    },
                ),
            ],
        )

        