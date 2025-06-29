import pyglet
from pyglet.window import Window

# TAILLE
class size():

    def __init__(self):
        self.width = 0
        self.height = 0
    
    def resize(self,width,height):
        self.width = width
        self.height = height

# CURRENT SCREEN AND MORE
class current():
    def __init__(self):
        self.screen = "menu"
    
    def setScreen(self, screen):
        self.screen = screen

# CONFIG WINDOW
config = pyglet.gl.Config(double_buffer=True)
event_loop = pyglet.app.EventLoop()

#WINDOW SIZE
windowSize = size()
windowSize.resize(1280,720)

# WINDOWSRIN
window = Window(width=windowSize.width, height=windowSize.height, resizable=True, config=config)