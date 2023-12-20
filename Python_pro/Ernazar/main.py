from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController 


app = Ursina()
sky = Sky()

for i in range(0, 10, 1):
    cube = Entity(model='cube', color=hsv(20,1,1), scale= 2, collider='box', position = (i, 1, 10))
    cube = Entity(model='cube', color=hsv(20,1,1), scale= 2, collider='box', position = (10, 1, i))
    cube = Entity(model='cube', color=hsv(20,1,1), scale= 2, collider='box', position = (0, 1, i))
    cube = Entity(model='cube', color=hsv(20,1,1), scale= 2, collider='box', position = (i, 1, 0))

    cube = Entity(model='cube', color=hsv(20,1,1), scale= 2, collider='box', position = (i, 5, 10))
    cube = Entity(model='cube', color=hsv(20,1,1), scale= 2, collider='box', position = (10, 5, i))
    cube = Entity(model='cube', color=hsv(20,1,1), scale= 2, collider='box', position = (0, 5, i))
    cube = Entity(model='cube', color=hsv(20,1,1), scale= 2, collider='box', position = (i, 5, 0))

    cube = Entity(model='cube', color=hsv(80,1,1), scale= 2, collider='box', position = (i, 3, 10))
    cube = Entity(model='cube', color=hsv(80,1,1), scale= 2, collider='box', position = (10, 3, i))
    cube = Entity(model='cube', color=hsv(80,1,1), scale= 2, collider='box', position = (0, 3, i))
    cube = Entity(model='cube', color=hsv(80,1,1), scale= 2, collider='box', position = (i, 3, 0))

''' cube = Entity(model='cube', color=hsv(10,1,1), scale= 6, collider='box', position = (i, 1, 12))
    cube = Entity(model='cube', color=hsv(10,1,1), scale= 5, collider='box', position = (i, 1, 15))
    cube = Entity(model='cube', color=hsv(10,1,1), scale= 4, collider='box', position = (i, 1, 18))
    cube = Entity(model='cube', color=hsv(10,1,1), scale= 3, collider='box', position = (i, 1, 21))
    cube = Entity(model='cube', color=hsv(10,1,1), scale= 2, collider='box', position = (i, 1, 24))
    cube = Entity(model='cube', color=hsv(10,1,1), scale= 1, collider='box', position = (i, 0, 26))
'''



jer = Entity(model='plane', color=hsv(100,1,1), scale= 100, collider='mesh')
shar = Entity(model='sphera', color=hsv(200,1,1), scale= 2, collider='mesh', position = (0, 60, 0))

men = FirstPersonController()

def update():
    men_x = men.position[0]
    men_z = men.position[2]
    shar.position = (men_x, 20, men_z)

app.run()
