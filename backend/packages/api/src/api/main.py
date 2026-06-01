import asyncio
from concurrent.futures import ThreadPoolExecutor

from fastapi import FastAPI

from core.sources.ars_technica import get_ars_technica
from core.sources.github import get_trending_repos
from core.sources.hn import get_hn
from core.sources.lobsters import get_lobsters
import uvicorn

app = FastAPI()
executor = ThreadPoolExecutor()


@app.get("/sources/lobsters")
def lobsters():
    return get_lobsters()


@app.get("/sources/hn")
def hn():
    return get_hn()


@app.get("/sources/ars-technica")
def ars_technica():
    return get_ars_technica()


@app.get("/sources/github")
def github():
    return get_trending_repos()


@app.get("/sources/all")
async def all_sources():
    loop = asyncio.get_event_loop()
    lobsters_task, hn_task, ars_task, github_task = await asyncio.gather(
        loop.run_in_executor(executor, get_lobsters),
        loop.run_in_executor(executor, get_hn),
        loop.run_in_executor(executor, get_ars_technica),
        loop.run_in_executor(executor, get_trending_repos),
    )
    return {
        "lobsters": lobsters_task,
        "hn": hn_task,
        "ars_technica": ars_task,
        "github": github_task,
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)