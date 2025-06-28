# IMPORTATION
import pyglet
import os

from pyglet.window import Window
from pyglet.window import mouse
from pyglet.media import load

import game
from game import ui
from game.ui import play as menu_play
from game.ui import setting as menu_setting

player = pyglet.media.Player()
config = pyglet.gl.Config(double_buffer=True)
event_loop = pyglet.app.EventLoop()


# TAILLE
class taille ():

    def __init__(self):
        self.width = 0
        self.height = 0
    
    def resize(self,width,height):
        self.width = width
        self.height = height
windowSize = taille()
windowSize.resize(1280,720)

# WINDOWSRIN
window = Window(width=windowSize.width, height=windowSize.height, resizable=True, config=config)
window.set_caption("SpeedWar - Menu principal")

# SCREEN
class current():
    def __init__(self):
        self.screen = "menu"
    
    def setScreen(self, screen):
        self.screen = screen
current_screen= current()

play_screen = menu_play.load_play_scene(window)
setting_screen = menu_setting.load_setting_scene(window)

# IMAGE
class img():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = pyglet.resource.image('assets/image/titre.png')
        self.width = self.image.width
        self.height = self.image.height

    def setPosition(self, x, y):
        self.x = x
        self.y = y
    
    def setImage(self,chemin):
        self.image = pyglet.resource.image(chemin)

# TITRE
titre = img()
titre.setImage('assets/image/titre.png')
titre.setPosition((windowSize.width - titre.width)/2, windowSize.height - titre.height)

# BACKGROUND
fond = pyglet.resource.image("assets/image/retro-bg.png")
fond.width = window.width
fond.height = window.height

# MUSIQUE  
class music ():
    def __init__(self):
        self.source = load("SpeedWar/assets/music/test.mp3")
    def set_titre(self, titre):
        self.source = load(titre)
music1 = music()
music1.set_titre("SpeedWar/assets/music/test.mp3")
music2 = music()
music2.set_titre("SpeedWar/assets/music/warspeed_music.mp3")

# BRUIT SOURIS
class sound():
    def __init__(self):
        self.titre = "assets/music/click.mp3"
        self.streaming = False
        self.media =  pyglet.resource.media(self.titre, self.streaming)

    def setTitre(self,titre):
        self. titre = titre
        self.media =  pyglet.resource.media(self.titre, self.streaming)

    def setStreaming(self,boolean):
        self.streaming = boolean
        self.media =  pyglet.resource.media(self.titre, self.streaming)

sound_left = sound()
sound_left.setTitre("assets/music/click.mp3")

sound_effect = sound()
sound_effect.setTitre("assets/music/button-click.mp3")

# BOUTON
batch = pyglet.graphics.Batch()
backch = pyglet.graphics.Batch()

class button ():
    def __init__(self):
        # PORTE
        self.unpressed = pyglet.resource.image("assets/image/play_no_pressed.png")
        self.pressed = pyglet.resource.image("assets/image/play_pressed.png")
        self.hover = pyglet.resource.image("assets/image/play_hover.png")
        self.height = self.pressed.height
        self.widht = self.pressed.width
        self.batch = None
        self.x = 0
        self.y = 0
        self.xhover = []
        self.yhover = []
        self.push = pyglet.gui.PushButton(
        self.x, self.y, pressed= self.pressed,
        unpressed= self.unpressed, batch=self.batch,
        )
        self.hoverBool = False

        # MAISON
        self.open = False

    def setValues(self, unpressed, pressed, hover, x, y):
        self.unpressed = unpressed
        self.pressed = pressed
        self.height = self.pressed.height
        self.widht = self.pressed.width
        self.hover = hover
        self.x = x
        self.y = y
        self.xhover = []
        self.yhover = []
        self.xhover.append(self.x)
        self.xhover.append(self.x+self.widht)
        self.yhover.append(self.y)
        self.yhover.append(self.y+self.height)
        self.push = pyglet.gui.PushButton(
        self.x, self.y, pressed= self.pressed,
        unpressed= self.unpressed, batch=self.batch,
        )
    
    def setBatch(self, batch):
        self.batch = batch
    
    # fonctionnalité PORTE

    def setPostion(self, x, y):
        self.x = x
        self.y = y
        self.xhover = []
        self.yhover = []
        self.xhover.append(self.x)
        self.xhover.append(self.x+self.widht)
        self.yhover.append(self.y)
        self.yhover.append(self.y+self.height)
        self.push = pyglet.gui.PushButton(
        self.x, self.y, pressed= self.pressed,
        unpressed= self.unpressed, batch=self.batch,
        )
    
    def setHover(self):
        self.push = pyglet.gui.PushButton(
        self.x, self.y, pressed= self.pressed,
        unpressed= self.hover, batch=self.batch,
        )
        self.hoverBool = True
    
    def unsetHover(self):
        self.hoverBool = False
    
    def setUnpressed(self):
        self.push = pyglet.gui.PushButton(
        self.x, self.y, pressed= self.pressed,
        unpressed= self.unpressed, batch=self.batch,
        )

    # fonctionnalité MAISON

    def setOpen(self):
        self.open = True

    def setClose(self):
        self.open = False

def my_on_press_handler(widget):
    pass
def my_on_release_handler(widget):
    print("Button Released...")
    sound_effect.media.play()
    if play.open == setting.open:
        if widget == play.push:
            play.setOpen()
            current_screen.setScreen("play")
        if widget == setting.push:
            setting.setOpen()
            current_screen.setScreen("setting")
        if widget == exit.push:
            window.close()
    if widget == back.push:
        current_screen.setScreen("menu")
        play.setClose()
        setting.setClose()


# play
play = button()
play.setBatch(batch)
play.setValues(pyglet.resource.image("assets/image/play_no_pressed.png"),
                pyglet.resource.image("assets/image/play_pressed.png"),
                pyglet.resource.image("assets/image/play_hover.png"),
                (window.width - play.widht)/2,
                (window.height - play.height)/2
)

# setting
setting = button()
setting.setBatch(batch)
setting.setValues(pyglet.resource.image("assets/image/setting_no_pressed.png"),
                pyglet.resource.image("assets/image/setting_pressed.png"),
                pyglet.resource.image("assets/image/setting_hover.png"),
                (window.width - setting.widht)/2,
                (window.height - setting.height - play.height*3)/2
)

# exit
exit = button()
exit.setBatch(batch)
exit.setValues(pyglet.resource.image("assets/image/exit_no_pressed.png"),
                pyglet.resource.image("assets/image/exit_pressed.png"),
                pyglet.resource.image("assets/image/exit_hover.png"),
                (window.width - exit.widht)/2,
                (window.height - exit.height - play.height*3 - setting.height*3)/2
)

# back
back = button()
back.setBatch(backch)
back.setValues(pyglet.resource.image("assets/image/exit_no_pressed.png"),
                pyglet.resource.image("assets/image/exit_pressed.png"),
                pyglet.resource.image("assets/image/exit_hover.png"),
                (window.width - exit.widht)/2,
                (window.height - exit.height - play.height*3 - setting.height*3 - exit.height*3)/2
)

# INTERACTION
# log
event_logger = pyglet.window.event.WindowEventLogger()
window.push_handlers(event_logger)

def on_eos():
    print("[event] on_eos: end of file")

@player.event
def on_player_eos():
    player.play()
    print("[event] on_player_eos: end of queue")

@window.event
def on_mouse_motion(x,y,dx,dy):
    themouse = [x,y]
    if (themouse[0] > play.xhover[0] and themouse[0] < play.xhover[1]) and (themouse[1] > play.yhover[0] and themouse[1] < play.yhover[1]) and play.open == False:
        play.setHover()
        # print("hover play")
        window.push_handlers(play.push)
        play.push.set_handler('on_press', my_on_press_handler)
        play.push.set_handler('on_release', my_on_release_handler)
    else:
        play.setUnpressed()
        play.unsetHover()

    if (themouse[0] > setting.xhover[0] and themouse[0] < setting.xhover[1]) and (themouse[1] > setting.yhover[0] and themouse[1] < setting.yhover[1]) and setting.open == False:
        setting.setHover()
        # print("hover setting")
        window.push_handlers(setting.push)
        setting.push.set_handler('on_press', my_on_press_handler)
        setting.push.set_handler('on_release', my_on_release_handler)
    else:
        setting.setUnpressed()
        setting.unsetHover()
    
    if (themouse[0] > exit.xhover[0] and themouse[0] < exit.xhover[1]) and (themouse[1] > exit.yhover[0] and themouse[1] < exit.yhover[1]) and exit.open == False:
        exit.setHover()
        # print("hover exit")
        window.push_handlers(exit.push)
        exit.push.set_handler('on_press', my_on_press_handler)
        exit.push.set_handler('on_release', my_on_release_handler)
    else:
        exit.setUnpressed()
        exit.unsetHover()
    
    if (themouse[0] > back.xhover[0] and themouse[0] < back.xhover[1]) and (themouse[1] > back.yhover[0] and themouse[1] < back.yhover[1]) and back.open == False:
        back.setHover()
        # print("hover back")
        window.push_handlers(back.push)
        back.push.set_handler('on_press', my_on_press_handler)
        back.push.set_handler('on_release', my_on_release_handler)
    else:
        back.setUnpressed()
        back.unsetHover()

# Souris
@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    print("Mouse is dragged")

@window.event
def on_mouse_press(x, y, button, modifiers):
    sound_left.media.play().volume = 0.0
    if button == mouse.LEFT:
         sound_left.media.play().volume
    if button == mouse.RIGHT:
        sound_left.media.play()

@window.event
def on_resize(width,height):
    windowSize.resize(width,height)
    play.setPostion((window.width - play.widht)/2,(window.height - play.height)/2)
    setting.setPostion((window.width - setting.widht)/2,(window.height - setting.height - play.height*3)/2)
    exit.setPostion((window.width - exit.widht)/2,(window.height - exit.height - play.height*3 - setting.height*3)/2)
    back.setPostion((window.width - exit.widht)/2,(window.height - exit.height - play.height*3 - setting.height*3 - exit.height*3)/2)
    titre.setPosition((windowSize.width - titre.width)/2, windowSize.height - titre.height)

player.play()

# AFFICHAGE
@window.event
def on_draw():
    player.queue(music2.source)
    player.queue(music1.source)
    window.clear()
    fond.blit(0,0, width=window.width, height=window.height)
    if current_screen.screen == "menu":
        titre.image.blit(titre.x,titre.y)
        window.remove_handlers(back.push)
        batch.draw()
    elif current_screen.screen == "play":
        window.remove_handlers(play.push)
        window.remove_handlers(setting.push)
        window.remove_handlers(exit.push)
        titre.image.blit(titre.x,titre.y)
        play_screen.draw()
        backch.draw()
    elif current_screen.screen == "setting":
        window.remove_handlers(play.push)
        window.remove_handlers(setting.push)
        window.remove_handlers(exit.push)
        titre.image.blit(titre.x,titre.y)
        setting_screen.draw()
        backch.draw()


# LANCEMENT
pyglet.app.run()