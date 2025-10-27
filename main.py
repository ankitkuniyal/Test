from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import requests
from bs4 import BeautifulSoup

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/outline")
def get_country_outline(country: str = Query(..., description="Country name")):
    # Format Wikipedia URL properly
    url = f"https://en.wikipedia.org/wiki/{country.replace(' ', '_')}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/122.0 Safari/537.36"
    }

    try:
        res = requests.get(url, headers=headers, timeout=10)
        res.raise_for_status()
    except Exception as e:
        return {"error": f"Could not fetch Wikipedia page for '{country}'", "details": str(e)}

    soup = BeautifulSoup(res.text, "html.parser")

    headings = []
    for level in range(1, 7):  # h1 to h6
        for h in soup.find_all(f"h{level}"):
            text = h.get_text().strip()
            if text and "See also" not in text:
                headings.append((level, text))

    if not headings:
        return {"error": f"No headings found for '{country}'"}

    markdown_outline = "## Contents\n\n"
    for level, text in headings:
        markdown_outline += f"{'#' * level} {text}\n\n"

    return {"country": country, "outline": markdown_outline}
