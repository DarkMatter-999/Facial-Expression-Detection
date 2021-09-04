import os, threading

from flask import Flask, render_template, send_from_directory
import asyncio, websockets, json

from ursina import *

facedir = os.path.abspath('FaceDetect')
app = Flask(__name__, template_folder=facedir)

data = [{"x_":0, "y_":0}]*68

display = Ursina()

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/<path:path>")
def server_static(path):
    return send_from_directory("FaceDetect", path)

def startapp():
    app.run(debug=False)

def start_loop(loop, server):
    loop.run_until_complete(server)
    loop.run_forever()

def startws():
    newloop = asyncio.new_event_loop()
    start_server = websockets.serve(getface, "localhost", 5001, loop=newloop)    # yeah couldnt think of another port
    newloop.run_until_complete(start_server)
    newloop.run_forever()

def startdisplay():
    display.run()

async def getface(websocket, path):
    global data
    async for message in websocket:
        positions = await websocket.recv()
        data = json.loads(positions)
        # for pos in data[0]:
            # print(pos["_x"], pos["_y"])

        # print(data[1])

class Player(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        global data
        self.model='cube'
        self.texture = 'brick'
        self.color = color.red
        self.scale = 4

        for key, value in kwargs.items():
            setattr(self, key, value)

    def input(self, key):
        if key == 'space':
            self.animate_x(2, duration=1)

    def update(self):
        try:
            self.x  = ((data[0][29]["_x"] - 360)/(720 * 0.3) + self.x)/2
            self.y  = ((data[0][29]["_y"] - 280)/(560 * -0.3) + self.y)/2

            self.rotation_y = ( ((data[0][29]["_x"] / ((data[0][1]["_x"] + data[0][15]["_x"])/2) - 1) * 200) + self.rotation_y)/2
            self.rotation_x = ( ((data[0][30]["_y"] / ((data[0][31]["_y"] + data[0][35]["_y"])/2) - 1) * -200) + self.rotation_x)/2

        except Exception as e:
            # print(e)
            # self.rotation_x = (mouse.position.y * 45)
            # self.rotation_y = (mouse.position.x * -45)

            pass

if __name__ == "__main__":
    appthread = threading.Thread(target=startapp)    # start the flask webapp
    appthread.start()

    t = threading.Thread(target=startws)            # start websocket server
    t.start()

    e = Player()
    startdisplay()                                    # start Ursina engine
