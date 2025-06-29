import pyglet
from pyglet.media import load

IMG_PATH = "assets/image/titre.png"
MUSIC_PATH = "SpeedWar/assets/music/test.mp3"
NOISE_PATH = "assets/music/click.mp3"

# IMAGE
class img():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = pyglet.resource.image(IMG_PATH)
        self.width = self.image.width
        self.height = self.image.height

    def setPosition(self, x, y):
        self.x = x
        self.y = y
    
    def setImage(self,chemin):
        self.image = pyglet.resource.image(chemin)

# MUSIC
class music ():
    def __init__(self):
        self.source = MUSIC_PATH
    def setTitre(self, titre):
        self.source = titre

# NOISE
class sound():
    def __init__(self):
        self.titre = NOISE_PATH
        self.streaming = False
        self.media =  pyglet.resource.media(self.titre, self.streaming)

    def setTitre(self,titre):
        self. titre = titre
        self.media =  pyglet.resource.media(self.titre, self.streaming)

    def setStreaming(self,boolean):
        self.streaming = boolean
        self.media =  pyglet.resource.media(self.titre, self.streaming)

class button ():
    def __init__(self):
        # PORTE
        self.unpressed = pyglet.resource.image(IMG_PATH)
        self.pressed = pyglet.resource.image(IMG_PATH)
        self.hover = pyglet.resource.image(IMG_PATH)
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

# PLAYER
class MusicPlayer:
    def __init__(self):
        self.player = pyglet.media.Player()
        self.volume = 0.5
        self.player.volume = self.volume
        self.queue = []
    
    def set_volume(self, volume):
        self.volume = volume
        self.player.volume = volume
    
    def load_and_play(self, filepath, loop=False):
        source = pyglet.media.load(filepath)
        if loop:
            source = pyglet.media.SourceGroup(source.audio_format, None)
            source.queue(pyglet.media.load(filepath))
            self.player.queue(source)
        else:
            self.player.queue(source)
        self.player.play()

    def stop(self):
        self.player.pause()
        self.player.next_source()

    def is_playing(self):
        return self.player.playing