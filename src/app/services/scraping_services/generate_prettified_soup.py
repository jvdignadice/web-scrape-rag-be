from pathlib import Path
from datetime import datetime

output_dir = Path("app/services/scraping_services/soup_prettified")
output_dir.mkdir(exist_ok=True)
async def generate_prettified_soup(html_result: str):
    filename = output_dir / f"soup_prettified_{datetime.now():%Y%m%d_%H%M%S}.html"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_result)

    print(filename)