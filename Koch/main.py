# Librerias necesarias.
import pygame 
import os
from segment import vector2, Segment
import math
import colorsys

# Definimos una función.
def hsv_to_rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

# Determinamos el posicionamiento y su configuración.
os.environ["SDL_VIDEO_CENTERED"]='1'
width, height = 1024, 768
size = (width, height)
black, green = (0,0,0), (71, 228, 187)
pygame.init()
pygame.display.set_caption("Koch Snowflake Fractal ")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

# Configuraciones externas sobre las iteraciones y recursividad.
hue = 0.1
max = 7
speed = 0.1
counter = 0
iterations = 0
segments = []
a = vector2(300, 150)
b = vector2(700, 150)
magnitude = math.sqrt((a.x-b.x)**2 + (a.y-b.y)**2)
height = magnitude * math.sqrt(3)/2
c = vector2(a.x + (b.x-a.x)/2, 300 + height)
s1 = Segment(a, b)
s2 = Segment(b, c)
s3 = Segment(c, a)
segments.append(s1)
segments.append(s2)
segments.append(s3)

# Función de las iteraciones y los parametros de recursividad.
def iteration():
    global segments
    next_gen = []
    for s in segments:
        childs = s.generate();
        next_gen = childs+next_gen
    segments = next_gen

run = True
while run:
    screen.fill(black)
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    if counter > 10 and iterations is not max:
        iteration()
        counter = 0
        iterations += 1
    for s in segments:
        s.Display(screen, hsv_to_rgb(hue, 1, 1))
    hue += 0.002
    counter += speed
    pygame.display.update()

pygame.quit()
