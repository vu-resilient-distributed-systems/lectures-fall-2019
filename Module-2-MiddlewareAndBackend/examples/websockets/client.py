#client.py which sends data through websockets.
#Asynchronous communication happens between the client & server.

import asyncio
import websockets
import time
socket= "5555"
localhost ="127.0.0.1"

#Loop which runs till complete
async def collectdata():
    async with websockets.connect('ws://localhost:5555') as websocket:
        print("connecting to server at %s and socket %s" %(localhost, socket))
        for i in range(0,10):
            await websocket.send(str(i))
            print(i)
            await asyncio.sleep(5)
        await websocket.send("stop")
        websocket.close()

def main():
    asyncio.get_event_loop().run_until_complete(collectdata())

if __name__=="__main__":
    main()
