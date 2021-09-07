import os, threading
#from . import game, websocks, web
from game import *
from web import *
from websocks import *

data = [{"x_":0, "y_":0}]*68


if __name__ == "__main__":
    appthread = threading.Thread(target=startapp)    # start the flask webapp
    appthread.start()

    websock = threading.Thread(target=startws)            # start websocket server
    websock.start()

    startdisplay()                                    # start Ursina engine
