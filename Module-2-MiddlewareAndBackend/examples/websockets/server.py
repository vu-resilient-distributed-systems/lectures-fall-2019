#server.py which receives data through websockets from the client.
#Asynchronous communication happens between the client & server.

import asyncio
import websockets
import sys

localhost = '127.0.01'
socket = '5555'

#Loop which runs forever
async def sensordata(websocket, path):
        while True:
            data = await websocket.recv()#recv data from client
            print(data)
            if(data=="stop"):
                break
        print("Exiting loop")
        websocket.close()
        sys.exit()#Exit the program

def main():
    print("Starting server at %s and socket %s" %(localhost, socket))
    start_server = websockets.serve(sensordata, localhost, socket)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
    sensordata()

if __name__ == '__main__':
    main()
