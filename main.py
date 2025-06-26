# IMPORTATION
import pyglet
import os

from pyglet.window import Window
from pyglet.window import mouse
from pyglet.media import load
player = pyglet.media.Player()
config = pyglet.gl.Config(double_buffer=True)
event_loop = pyglet.app.EventLoop()

# WINDOWSRIN
window = Window(config=config)
window.set_caption("SpeedWar - Menu principal")

# TITRE
titre = pyglet.resource.image('assets/image/titre.png')
width_titre, height_titre = titre.width, titre.height
x_titre = (window.width - width_titre)/2
y_titre = window.height - height_titre

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
sound_left = pyglet.resource.media("assets/music/gun-shot-1.mp3", streaming=False)
sound_right = pyglet.resource.media("assets/music/gun-shot-2.mp3", streaming=False)

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

    def set_values(self, unpressed, pressed, hover, x, y):
        self.unpressed = unpressed
        self.pressed = pressed
        self.height = self.pressed.height
        self.widht = self.pressed.width
        self.hover = hover
        self.x = x
        self.y = y
        self.xhover.append(self.x)
        self.xhover.append(self.x+self.widht)
        self.yhover.append(self.y)
        self.yhover.append(self.y+self.height)
        self.push = pyglet.gui.PushButton(
        self.x, self.y, pressed= self.pressed,
        unpressed= self.unpressed, batch=self.batch,
        )
    
    def set_batch(self, batch):
        self.batch = batch
    
    # fonctionnalité PORTE
    
    def set_hover(self):
        self.push = pyglet.gui.PushButton(
        self.x, self.y, pressed= self.pressed,
        unpressed= self.hover, batch=self.batch,
        )
        self.hoverBool = True
    
    def unset_hover(self):
        self.hoverBool = False
    
    def set_unpressed(self):
        self.push = pyglet.gui.PushButton(
        self.x, self.y, pressed= self.pressed,
        unpressed= self.unpressed, batch=self.batch,
        )

    # fonctionnalité MAISON

    def set_open(self):
        self.open = True

    def set_close(self):
        self.open = False

def my_on_press_handler(widget):
    print("Button Pressed!")
def my_on_release_handler(widget):
    print("Button Released...")
    if play.open == setting.open:
        if widget == play.push:
            play.set_open()
        if widget == setting.push:
            setting.set_open()
        if widget == exit.push:
            window.close()
    if widget == back.push:
        play.set_close()
        setting.set_close()


# play
play = button()
play.set_batch(batch)
play.set_values(pyglet.resource.image("assets/image/play_no_pressed.png"),
                pyglet.resource.image("assets/image/play_pressed.png"),
                pyglet.resource.image("assets/image/play_hover.png"),
                (window.width - play.widht)/2,
                (window.height - play.height)/2
)

# setting
setting = button()
setting.set_batch(batch)
setting.set_values(pyglet.resource.image("assets/image/setting_no_pressed.png"),
                pyglet.resource.image("assets/image/setting_pressed.png"),
                pyglet.resource.image("assets/image/setting_hover.png"),
                (window.width - setting.widht)/2,
                (window.height - setting.height - play.height*3)/2
)

# exit
exit = button()
exit.set_batch(batch)
exit.set_values(pyglet.resource.image("assets/image/exit_no_pressed.png"),
                pyglet.resource.image("assets/image/exit_pressed.png"),
                pyglet.resource.image("assets/image/exit_hover.png"),
                (window.width - exit.widht)/2,
                (window.height - exit.height - play.height*3 - setting.height*3)/2
)

# back
back = button()
back.set_batch(backch)
back.set_values(pyglet.resource.image("assets/image/exit_no_pressed.png"),
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
        play.set_hover()
        # print("hover play")
        window.push_handlers(play.push)
        play.push.set_handler('on_press', my_on_press_handler)
        play.push.set_handler('on_release', my_on_release_handler)
    else:
        play.set_unpressed()
        play.unset_hover()

    if (themouse[0] > setting.xhover[0] and themouse[0] < setting.xhover[1]) and (themouse[1] > setting.yhover[0] and themouse[1] < setting.yhover[1]) and setting.open == False:
        setting.set_hover()
        # print("hover setting")
        window.push_handlers(setting.push)
        setting.push.set_handler('on_press', my_on_press_handler)
        setting.push.set_handler('on_release', my_on_release_handler)
    else:
        setting.set_unpressed()
        setting.unset_hover()
    
    if (themouse[0] > exit.xhover[0] and themouse[0] < exit.xhover[1]) and (themouse[1] > exit.yhover[0] and themouse[1] < exit.yhover[1]) and exit.open == False:
        exit.set_hover()
        # print("hover exit")
        window.push_handlers(exit.push)
        exit.push.set_handler('on_press', my_on_press_handler)
        exit.push.set_handler('on_release', my_on_release_handler)
    else:
        exit.set_unpressed()
        exit.unset_hover()
    
    if (themouse[0] > back.xhover[0] and themouse[0] < back.xhover[1]) and (themouse[1] > back.yhover[0] and themouse[1] < back.yhover[1]) and back.open == False:
        back.set_hover()
        # print("hover back")
        window.push_handlers(back.push)
        back.push.set_handler('on_press', my_on_press_handler)
        back.push.set_handler('on_release', my_on_release_handler)
    else:
        back.set_unpressed()
        back.unset_hover()

# Souris
@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    print("Mouse is dragged")

@window.event
def on_mouse_press(x, y, button, modifiers):
    sound_left.play().volume = 0.0
    if button == mouse.LEFT:
         sound_left.play().volume
    if button == mouse.RIGHT:
        sound_right.play()

player.play()
# AFFICHAGE

@window.event
def on_draw():
    player.queue(music2.source)
    player.queue(music1.source)
    window.clear()
    if play.open == setting.open:
        titre.blit(x_titre,y_titre)
        batch.draw()
    elif play.open == True:
        window.remove_handlers(play.push)
        window.remove_handlers(setting.push)
        window.remove_handlers(exit.push)
        titre.blit(x_titre,y_titre)
        backch.draw()
    else :
        window.remove_handlers(play.push)
        window.remove_handlers(setting.push)
        window.remove_handlers(exit.push)
        titre.blit(x_titre,y_titre)
        backch.draw()


# LANCEMENT
pyglet.app.run()