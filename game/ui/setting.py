import pyglet

def load_setting_scene(window):
    
    label = pyglet.text.Label(
        "Choisissez votre véhicule",
        x=window.width//2,
        y=window.height//2,
        anchor_x='center',
        anchor_y='center',
    )

    return label