import pyglet

from game.ui.menu import MenuScreen
from game.ui.windowing import window, windowSize

menu = MenuScreen(window, windowSize)

@window.event
def on_draw():
    menu.drawMenu()


pyglet.app.run()