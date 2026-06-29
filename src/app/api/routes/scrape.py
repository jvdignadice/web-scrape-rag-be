from fastapi import APIRouter
import httpx
from bs4 import BeautifulSoup
from app.embeddings import ollama_embedder

router = APIRouter()
embedder = ollama_embedder.OllamaEmbedder()
@router.post("/")
async def scrape_url(url: str):
    async with httpx.AsyncClient() as client:
        res = await client.get(url)

    soup = BeautifulSoup(res.text, "html.parser")
    text = soup.get_text()
    formatted_text = soup.prettify()
    title = soup.title.string if soup.title else "No title found"
    title_string = soup.title.string if soup.title else "No title found"
    head = soup.head
    links = []
    for link in soup.find_all("a"):
        links.append(link.get("href"))

    return {
        "url": url,
        "length": len(text),
        "links": links,
        "title": title,
        "title_string": title_string,
    }