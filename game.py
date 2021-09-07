
from ursina import *

display = Ursina()

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
            self.rotation_z = ( ((data[0][36]["_y"] - data[0][45]["_y"])/(data[0][36]["_x"] - data[0][45]["_x"])) *-20 + self.rotation_z)/2

            # self.scale = ( (data[0][45]["_x"] - data[0][36]["_x"])*0.05 + self.scale_x)/2

        except Exception as e:
            # print(e)
            # print("No face found")
            # self.rotation_x = (mouse.position.y * 45)
            # self.rotation_y = (mouse.position.x * -45)

            pass

def startdisplay():
    e = Player()
    display.run()
