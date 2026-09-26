# 16_async_demo.py
# Level 1 — Topic 16: Async with asyncio and httpx

import asyncio

try:
    import httpx
    HAS_HTTPX = True
except ImportError:
    HAS_HTTPX = False
    print("httpx not installed. Run: pip install httpx")


async def fetch_url(client: "httpx.AsyncClient", url: str) -> str:
    response = await client.get(url, timeout=10)
    return f"{url} → {response.status_code}"


async def main():
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1",
        "https://api.github.com",
    ]

    async with httpx.AsyncClient() as client:
        tasks = [fetch_url(client, url) for url in urls]
        results = await asyncio.gather(*tasks)

    for r in results:
        print(r)


if __name__ == "__main__":
    if HAS_HTTPX:
        asyncio.run(main())
    else:
        print("Skipping async demo (httpx missing).")
