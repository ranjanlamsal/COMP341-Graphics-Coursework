import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import gluOrtho2D
import random
from freetype import Face
import numpy as np

X_start = 400
Y_start = 600
cost = 40
width = 60


class histogram():
    frequencies = []
    def __init__(self, frequencies):
        self.frequencies = frequencies
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720), DOUBLEBUF|OPENGL)
        self.clock = pygame.time.Clock()
        self.show_screen()
        
    def show_screen(self):
        glClearColor(1,1,1,1)
        glOrtho(0, 1280, 720, 0, -1, 1)
        
        color = [0]*(len(self.frequencies))
        for i in range(len(self.frequencies)):
            color[i] = random.random()
        
        
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    quit()

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            draw_axis(X_start, Y_start, X_max = 1000, Y_max = 100)
            
            for i in range(len(self.frequencies)):
                x = X_start + i*width
                # draw_axis_points(X_start, Y_start)
                draw_rectangle(x, Y_start, width, self.frequencies[i]*cost, color = (color[i], color[i], color[i]))
            pygame.display.flip()
            self.clock.tick(60)
            
        
def draw_rectangle(x, y, width, height, color):
    glColor3f(*color)

    # Draw top and bottom lines using Bresenham algorithm
    draw_line(x, y, x + width, y, color)
    draw_line(x, y - height, x + width, y - height, color)

    # Draw left and right lines using Bresenham algorithm
    draw_line(x, y, x, y - height, color)
    draw_line(x + width, y, x + width, y - height, color)

    # Fill the rectangle using Bresenham algorithm
    fill_rectangle(x, y, width, height, color)
    
    
def draw_line(x1, y1, x2, y2, color):
    # Bresenham's Line Drawing Algorithm
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    steep = dy > dx

    if steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    offx = 1 if x2 > x1 else -1
    offy = 1 if y2 > y1 else -1

    err = dx / 2.0
    y = y1

    for x in range(x1, x2 + 1):
        if steep:
            glColor3f(*color)
            glBegin(GL_POINTS)
            glVertex2f(y, x)
            glEnd()
        else:
            glColor3f(*color)
            glBegin(GL_POINTS)
            glVertex2f(x, y)
            glEnd()

        err -= dy
        if err < 0:
            y += offy
            err += dx
            
            
def draw_axis(x, y, X_max, Y_max):
    glColor3f(0, 0, 0)

    # Draw X-axis
    draw_line(x, y + 1, X_max, y + 1, (0, 0, 0))

    # Draw Y-axis
    draw_line(x, y, x, Y_max, (0, 0, 0))


def fill_rectangle(x, y, width, height, color):
    for i in range(height):
        draw_line(x, y - i, x + width, y - i, color)
        
if __name__ == "__main__":
    freq = [1,5,10,4,8]
    hist = histogram(freq)
    print(hist.frequencies)
