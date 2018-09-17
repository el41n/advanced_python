import asyncio
import math


async def prime(n, m, acc=[]):
    for i in range(n, m):
        if i == 2 or i == 3:
            acc.append(i)
            continue
        for y in range(2, int(math.sqrt(i) + 1)):
            if i % y == 0:
                break
        else:
            acc.append(i)
    print(acc)
    return acc


async def sm(n, m, ):
    acc = await prime(n, m)
    return sum(acc)


if __name__ == '__main__':
    acc = []
    ioloop = asyncio.get_event_loop()
    acc = ioloop.run_until_complete(sm(1, 10))
    print(acc)
    ioloop.close()
