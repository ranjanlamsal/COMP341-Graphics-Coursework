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

    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y - height)
    glVertex2f(x, y - height)
    glEnd()

def draw_axis(x, y, X_max, Y_max):
    glColor3f(0,0,0)
    
    glBegin(GL_LINES)
    glVertex2f(x, y+1)
    glVertex2f(X_max, y+1)
    glEnd()
    
    glBegin(GL_LINES)
    glVertex2f(x , y)
    glVertex2f(x, Y_max)
    glEnd()

        
if __name__ == "__main__":
    freq = [1,5,10,4,8]
    hist = histogram(freq)
    print(hist.frequencies)
