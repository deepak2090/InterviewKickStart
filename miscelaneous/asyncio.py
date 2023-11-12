import asyncio

async def task1():
    print('Send first Email')
    asyncio.create_task(task2())
    await asyncio.sleep(2) # Simulating that the email reply takes 2 seconds
    print('First Email reply')

async def task2():
    print('Send second Email')
    asyncio.create_task(task3())
    await asyncio.sleep(2)
    print('Second Email reply')

async def task3():
    print('Send third Email')
    await asyncio.sleep(2)
    print('Third Email reply')

asyncio.run(task1())