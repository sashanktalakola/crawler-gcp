from fastapi import FastAPI
from pydantic import BaseModel
import asyncio
from crawl4ai import AsyncWebCrawler

app = FastAPI()

class URLRequest(BaseModel):
    url: str

async def main(url: str):
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=url)
        return result.markdown

@app.post("/")
async def root(request: URLRequest):
    markdown_content = await main(request.url)
    return {"content": markdown_content}