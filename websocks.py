
import asyncio, websockets, json

def start_loop(loop, server):
    loop.run_until_complete(server)
    loop.run_forever()

def startws():
    newloop = asyncio.new_event_loop()
    start_server = websockets.serve(getface, "localhost", 5001, loop=newloop)    # yeah couldnt think of another port
    newloop.run_until_complete(start_server)
    newloop.run_forever()

async def getface(websocket, path):
    global data
    async for message in websocket:
        positions = await websocket.recv()
        data = json.loads(positions)
        # for pos in data[0]:
            # print(pos["_x"], pos["_y"])

        # print(data[1])
