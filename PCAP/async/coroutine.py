import asyncio

async def say_hello():
    print('Hello')
    await asyncio.sleep(2)
    print('async world!')


event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(say_hello())
event_loop.close()
