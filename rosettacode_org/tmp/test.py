import aiohttp
import asyncio

SITES = ["https://google.com/","https://duckduckgo.com/",
	 "https://amazon.com/","https://overstock.com/",
	 "https://www.54356456456456.com",
	 "https://nytimes.com","https://ft.com/",
	 "https://wired.com","https://arstechnica.com/",
	 "https://abfdgdfsegfdgfdfsd.com",
	 "https://twitter.com","https://facebook.com/"]

async def crawler(site):
    if site is None:
        print("Must provide a site to crawl")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(site) as page:
                page_content = await page.read()
                html = await page.text()
                print(html)
                page_size = len(page_content)
                print(f"Home page {site} size is {page_size}")
    except Exception as e:
        print(f"Can't crawl home page on {site}: {e}")

async def multibot(sites):
    tasks = [asyncio.create_task(crawler(site)) for site in sites]
    for coroutine in asyncio.as_completed(tasks):
        await coroutine

#asyncio.run(multibot(SITES))
loop = asyncio.get_event_loop()
loop.run_until_complete(multibot(SITES))