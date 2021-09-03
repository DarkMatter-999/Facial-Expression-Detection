from flask import Flask, render_template, send_from_directory
import asyncio, websockets, json
import os, threading

facedir = os.path.abspath('FaceDetect')

app = Flask(__name__, template_folder=facedir)
absposition = None
@app.route("/")
def main():
	return render_template('index.html')

@app.route("/<path:path>")
def server_static(path):
	return send_from_directory("FaceDetect", path)

def startface():
    app.run(debug=False)

async def echo(websocket, path):
    async for message in websocket:
        positions = await websocket.recv()
        absposition = json.loads(positions)
        print(absposition)



if __name__ == "__main__":
    thread = threading.Thread(target=startface)
    thread.start()

    start_server = websockets.serve(echo, "localhost", 5001)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
