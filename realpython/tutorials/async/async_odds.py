import asyncio


async def odds(start, stop):
    if start % 2 == 0:
        start += 1
    for odd in range(start, stop + 1, 2):
        yield odd


async def main():
    g = odds(1, 29)
    numbers = await g.asend(None)
    print(numbers)

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
