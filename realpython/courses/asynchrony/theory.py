from random import randint
import time
import asyncio


def odds(start, stop):
    for odd in range(start, stop + 1, 2):
        yield odd


def randn():
    time.sleep(3)
    return randint(1, 10)


def main():
    odd_values = [odd for odd in odds(3, 15)]
    odds2 = tuple(odds(21, 29))
    print(odd_values)
    print(odds2)


if __name__ == "__main__":
    main()
