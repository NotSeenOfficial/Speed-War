# IMPORTATION

# MODULE
import pyglet
from pyglet.window import mouse

# CLASS
# WINDOW CORE
from game.ui.windowing import current
from game.ui.windowing import window, windowSize
# RESSOURCE
from game.ui.assets import img
from game.ui.assets import music
from game.ui.assets import sound
from game.ui.assets import button
from game.ui.assets import MusicPlayer

# SCREEN
import game.ui.play as Play
import game.ui.setting as Setting

# WINDOWSRIN


class MenuScreen:
    def __init__(self, window, windowSize):
        
        self.ok = False
        self.window = window
        self.windowSize = windowSize
        self.player = MusicPlayer()

        self.window.set_caption("SpeedWar - Menu principal")

        # CURRENT
        self.current_screen = current()
        self.current_screen.setScreen("menu")

        # TITRE
        self.titre = img()
        self.titre.setImage('assets/image/titre.png')
        self.titre.setPosition((self.windowSize.width - self.titre.width)/2, self.windowSize.height - self.titre.height)

        # BACKGROUND
        self.fond = pyglet.resource.image("assets/image/retro-bg.png")
        self.fond.width = self.window.width
        self.fond.height = self.window.height

                # MUSIQUE  
        self.music2 = music()
        self.music2.setTitre("SpeedWar/assets/music/warspeed_music.mp3")

        # NOISE
        self.sound_left = sound()
        self.sound_left.setTitre("assets/music/click.mp3")
        self.sound_effect = sound()
        self.sound_effect.setTitre("assets/music/button-click.mp3")

        # BUTTON
        self.batch = pyglet.graphics.Batch()
        self.backch = pyglet.graphics.Batch()

        # play
        self.play = button()
        self.play.setBatch(self.batch)
        self.play.setValues(pyglet.resource.image("assets/image/play_no_pressed.png"),
                        pyglet.resource.image("assets/image/play_pressed.png"),
                        pyglet.resource.image("assets/image/play_hover.png"),
                        (self.window.width - self.play.widht)/2,
                        (self.window.height - self.play.height)/2
        )

        # setting
        self.setting = button()
        self.setting.setBatch(self.batch)
        self.setting.setValues(pyglet.resource.image("assets/image/setting_no_pressed.png"),
                        pyglet.resource.image("assets/image/setting_pressed.png"),
                        pyglet.resource.image("assets/image/setting_hover.png"),
                        (self.window.width - self.setting.widht)/2,
                        (self.window.height - self.setting.height - self.play.height*3)/2
        )

        # exit
        self.exit = button()
        self.exit.setBatch(self.batch)
        self.exit.setValues(pyglet.resource.image("assets/image/exit_no_pressed.png"),
                        pyglet.resource.image("assets/image/exit_pressed.png"),
                        pyglet.resource.image("assets/image/exit_hover.png"),
                        (self.window.width - self.exit.widht)/2,
                        (self.window.height - self.exit.height - self.play.height*3 - self.setting.height*3)/2
        )

        # back
        self.back = button()
        self.back.setBatch(self.backch)
        self.back.setValues(pyglet.resource.image("assets/image/exit_no_pressed.png"),
                        pyglet.resource.image("assets/image/exit_pressed.png"),
                        pyglet.resource.image("assets/image/exit_hover.png"),
                        (self.window.width - self.exit.widht)/2,
                        (self.window.height - self.exit.height - self.play.height*3 - self.setting.height*3 - self.exit.height*3)/2
        )

        # INTERACTION
        # log
        self.event_logger = pyglet.window.event.WindowEventLogger()
        self.window.push_handlers(self.event_logger)

        self.register_events()
   
    def register_events(self):

        def my_on_press_handler(widget):
            pass
        def my_on_release_handler(widget):
            print("Button Released...")
            self.sound_effect.media.play()
            if self.play.open == self.setting.open:
                self.window.remove_handlers(self.back.push)
                if widget == self.play.push:
                    self.play.setOpen()
                    self.current_screen.setScreen("play")
                if widget == self.setting.push:
                    self.setting.setOpen()
                    self.current_screen.setScreen("setting")
                if widget == self.exit.push:
                    self.window.close()
            if widget == self.back.push:
                self.window.remove_handlers(self.play.push,self.setting.push,self.exit.push)
                self.current_screen.setScreen("menu")
                self.play.setClose()
                self.setting.setClose()
                
     
        def on_eos():
            print("[event] on_eos: end of file")

        @self.player.player.event
        def on_player_eos():
            self.player.player.play()
            print("[event] on_self.player_eos: end of queue")

        @self.window.event
        def on_mouse_motion(x,y,dx,dy):
            themouse = [x,y]
            if self.current_screen.screen == "menu":
                if (themouse[0] > self.play.xhover[0] and themouse[0] < self.play.xhover[1]) and (themouse[1] > self.play.yhover[0] and themouse[1] < self.play.yhover[1]) and self.play.open == False:
                    self.play.setHover()
                    # print("hover self.play")
                    self.window.push_handlers(self.play.push)
                    self.play.push.set_handler('on_press', my_on_press_handler)
                    self.play.push.set_handler('on_release', my_on_release_handler)
                else:
                    self.play.setUnpressed()
                    self.play.unsetHover()

                if (themouse[0] > self.setting.xhover[0] and themouse[0] < self.setting.xhover[1]) and (themouse[1] > self.setting.yhover[0] and themouse[1] < self.setting.yhover[1]) and self.setting.open == False:
                    self.setting.setHover()
                    # print("hover setting")
                    self.window.push_handlers(self.setting.push)
                    self.setting.push.set_handler('on_press', my_on_press_handler)
                    self.setting.push.set_handler('on_release', my_on_release_handler)
                else:
                    self.setting.setUnpressed()
                    self.setting.unsetHover()
          
                if (themouse[0] > self.exit.xhover[0] and themouse[0] < self.exit.xhover[1]) and (themouse[1] > self.exit.yhover[0] and themouse[1] < self.exit.yhover[1]) and self.exit.open == False:
                    self.exit.setHover()
                    # print("hover exit")
                    self.window.push_handlers(self.exit.push)
                    self.exit.push.set_handler('on_press', my_on_press_handler)
                    self.exit.push.set_handler('on_release', my_on_release_handler)
                else:
                    self.exit.setUnpressed()
                    self.exit.unsetHover()
            
            else :
                if (themouse[0] > self.back.xhover[0] and themouse[0] < self.back.xhover[1]) and (themouse[1] > self.back.yhover[0] and themouse[1] < self.back.yhover[1]) and self.back.open == False:
                    self.back.setHover()
                    # print("hover back")
                    self.window.push_handlers(self.back.push)
                    self.back.push.set_handler('on_press', my_on_press_handler)
                    self.back.push.set_handler('on_release', my_on_release_handler)
                else:
                    self.back.setUnpressed()
                    self.back.unsetHover()
            

        # Souris
        @self.window.event
        def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
            print("Mouse is dragged")

        @self.window.event
        def on_mouse_press(x, y, button, modifiers):
            self.sound_left.media.play().volume = 0.0
            if button == mouse.LEFT:
                self.sound_left.media.play().volume
            if button == mouse.RIGHT:
                self.sound_left.media.play()

        @self.window.event
        def on_resize(width,height):
            self.windowSize.resize(width,height)
            self.play.setPostion((self.window.width - self.play.widht)/2,(self.window.height - self.play.height)/2)
            self.setting.setPostion((self.window.width - self.setting.widht)/2,(self.window.height - self.setting.height - self.play.height*3)/2)
            self.exit.setPostion((self.window.width - self.exit.widht)/2,(self.window.height - self.exit.height - self.play.height*3 - self.setting.height*3)/2)
            self.back.setPostion((self.window.width - self.exit.widht)/2,(self.window.height - self.exit.height - self.play.height*3 - self.setting.height*3 - self.exit.height*3)/2)
            self.titre.setPosition((self.windowSize.width - self.titre.width)/2, self.windowSize.height - self.titre.height)

    def drawMenu(self):

            self.window.clear()
            self.player.load_and_play(self.music2.source)
            self.fond.blit(0,0, width=self.window.width, height=self.window.height)
            if self.current_screen.screen == "menu":
                self.titre.image.blit(self.titre.x,self.titre.y)
                self.window.remove_handlers(self.back.push)
                self.batch.draw()
            elif self.current_screen.screen == "play":
                self.play_screen = Play.load_play_scene(self.window)
                self.window.remove_handlers(self.play.push , self.setting.push , self.exit.push)
                self.titre.image.blit(self.titre.x,self.titre.y)
                self.play_screen.draw()
                self.backch.draw()
            elif self.current_screen.screen == "setting":
                self.setting_screen = Setting.load_setting_scene(self.window)
                self.window.remove_handlers(self.play.push , self.setting.push , self.exit.push)
                self.titre.image.blit(self.titre.x,self.titre.y)
                self.setting_screen.draw()
                self.backch.draw()



menu = MenuScreen(window,windowSize)

window.push_handlers(menu)