from bs4 import BeautifulSoup
import httpx
from app.core.scrape_models.best_sellers import BestSellerItem
from app.services.scraping_services.generate_prettified_soup import generate_prettified_soup

async def scrape_amazon_best_sellers(url: str):
    async with httpx.AsyncClient() as client:
        res = await client.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    await generate_prettified_soup(soup.prettify())
    best_sellers = BestSellerItem(title="", link=[], url=url, text_result="")


    for item in soup.find_all("a"):
        link = item.get("href")
        best_sellers.url = url
        best_sellers.link.append(link)
        best_sellers.title = soup.title.string if soup.title else "No title found"
        best_sellers.text_result = soup.prettify() if soup else "No text found"

    return best_sellers