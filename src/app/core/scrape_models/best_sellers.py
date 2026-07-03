from pydantic import BaseModel
from typing import List

class BestSellerItem(BaseModel):
    title: str
    link: List[str]
    url: str
    text_result: str = ""

