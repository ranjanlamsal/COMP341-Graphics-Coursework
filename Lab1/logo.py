import pygame
from pygame.locals import *
from OpenGL.GL import *
import numpy as np
import math
from OpenGL.GLU import gluOrtho2D


class Logo():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720), DOUBLEBUF|OPENGL)
        self.clock = pygame.time.Clock()
        self.show_screen()
        
    def show_screen(self):
        glClearColor(0.5, 1, 1, 1)
        glOrtho(0, 1280, 720, 0, -1, 1)
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    quit()

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glColor3f(10.0, 0.0, 0.0)
            draw_filled_circle((585.0, 320.0),225.16660498395404, color=(1,1,0), segments=50000)
            
            vertices = draw_upside_down_triangle()
            draw_u_shape(x=350, y=10, width=20, height=71, space=48)
            draw_rectangle(527, 264, 19, 132)
            center, radius = draw_circumcircle(vertices)
            print(center, radius)
            

            draw_circle_stroke((585.0, 320.0),225.16660498395404, (0,0,0))
            draw_stroked_triangle()
            draw_filled_circle((vertices[0][0], vertices[0][1]), 5, color=(0.6627, 0.77647, 0.8941176), segments=50000)
            draw_circle_stroke((vertices[0][0], vertices[0][1]), 5, color=(0, 0, 0), segments=50000)

            draw_filled_circle((vertices[1][0], vertices[1][1]), 5, color=(0.6627, 0.77647, 0.8941176), segments=50000)
            draw_circle_stroke((vertices[1][0], vertices[1][1]), 5, color=(0, 0, 0), segments=50000)

            draw_filled_circle((vertices[2][0], vertices[2][1]), 5, color=(0.6627, 0.77647, 0.8941176), segments=50000)
            draw_circle_stroke((vertices[2][0], vertices[2][1]), 5, color=(0, 0, 0), segments=50000)

            draw_floral_pattern((585.0, 320.0),225.16660498395404, 12, 20)
            pygame.display.flip()
            self.clock.tick(60)

            

def draw_rectangle(x, y, width, height):
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()

def draw_u_shape(**kwargs):
    glColor3f(0.0, 0.0, 0.0)
    x = kwargs['x']
    y = kwargs['y']
    width = kwargs['width']
    height = kwargs['height']
    space = kwargs['space']
    
    glPushMatrix()
    glTranslatef(x + width / 2, y + height / 2, 0)
    glRotatef(45, 0, 0, 1)
    glTranslatef(-width / 2, -height / 2, 0)
    
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x+width, y)
    glVertex2f(x+width, y+height+width)
    glVertex2f(x, y+height+width)
    glVertex2f(x, y)
    glEnd()
    
    glBegin(GL_QUADS)
    glVertex2f(x+width+space, y)
    glVertex2f(x+width+space+width, y)
    glVertex2f(x+width+space+width, y+height+width)
    glVertex2f(x+width+space, y+height+width)
    glVertex2f(x+width+space, y)
    glEnd()
    
    glBegin(GL_QUADS)
    glVertex2f(x, y+height+width)
    glVertex2f(x+width+space+width, y+height+width)
    glVertex2f(x+width+space+width, y+height)
    glVertex2f(x, y+height)
    glVertex2f(x, y+height+width)
    glEnd()
    
    glPopMatrix()

def draw_upside_down_triangle():
    # Fill color with hex (FDAEAC)
    glColor3f(1,0,0)
    glColor(0.9921568627450981,0.6823529411764706,0.6745098039215687)
    # Calculate the centroid of the U-shape
    centroid_x = 585
    centroid_y = 320
    
    # Calculate the length of each side of the triangle
    triangle_side_length = 390
    
    # Calculate the vertices of the triangle
    vertices = [
        (centroid_x - triangle_side_length / 2, centroid_y - triangle_side_length / (2 * np.sqrt(3))),  # Top vertex
        (centroid_x + triangle_side_length / 2, centroid_y - triangle_side_length / (2 * np.sqrt(3))),  # Right vertex
        (centroid_x, centroid_y + triangle_side_length / np.sqrt(3))  # Bottom vertex
    ]
    
    # Draw the filled triangle
    glBegin(GL_TRIANGLES)
    for vertex in vertices:
        glVertex2f(*vertex)
    
    glEnd()

    # Draw the outline of the triangle
    glColor3f(0.0, 0.0, 0.0)  # Black color for outline
    # glBegin(GL_LINE_LOOP)
    # for vertex in vertices:
    #     glVertex2f(*vertex)
    # glEnd()
    
     # Draw the thicker stroke
    glLineWidth(10)  # Set the line width to 5
    glBegin(GL_LINE_LOOP)
    for vertex in vertices:
        glVertex2f(*vertex)
    glEnd()
    return vertices

def draw_filled_circle(center, radius, color=(1.0, 1.0, 1.0), segments=10000):
    glColor3f(*color)
    glBegin(GL_POLYGON)
    for i in range(segments):
        angle = 2.0 * np.pi * i / segments
        x = center[0] + radius * np.cos(angle)
        y = center[1] + radius * np.sin(angle)
        glVertex2f(x, y)
    glEnd()


def draw_circle_stroke(center, radius,color=(1.0,1.0,1.0), segments=5000):
    glColor3f(*color)
    glBegin(GL_LINE_LOOP)
    for i in range(segments):
        angle = 2.0 * np.pi * i / segments
        x = center[0] + radius * np.cos(angle)
        y = center[1] + radius * np.sin(angle)
        glVertex2f(x, y)
    glEnd()

def draw_circumcircle(vertices):
    side_midpoints = [
        ((vertices[0][0] + vertices[1][0]) / 2, (vertices[0][1] + vertices[1][1]) / 2),  # Midpoint of side 1-2
        ((vertices[1][0] + vertices[2][0]) / 2, (vertices[1][1] + vertices[2][1]) / 2),  # Midpoint of side 2-3
        ((vertices[2][0] + vertices[0][0]) / 2, (vertices[2][1] + vertices[0][1]) / 2)   # Midpoint of side 3-1
    ]
    
    # Circumcenter is the intersection point of the perpendicular bisectors of the sides
    circumcenter_x = (side_midpoints[0][0] + side_midpoints[1][0] + side_midpoints[2][0]) / 3
    circumcenter_y = (side_midpoints[0][1] + side_midpoints[1][1] + side_midpoints[2][1]) / 3
    
    # Calculate the radius of the circumcircle
    circumradius = np.sqrt((circumcenter_x - vertices[0][0]) ** 2 + (circumcenter_y - vertices[0][1]) ** 2)
    
    color = (0.6627, 0.77647,0.8941176)
    # Draw the outer stroke of the circumcircle
    draw_circle_stroke((circumcenter_x, circumcenter_y), circumradius + 5, color = color,segments=500)
    draw_circle_stroke((circumcenter_x, circumcenter_y), circumradius + 10, color = color,segments=500)
    draw_circle_stroke((circumcenter_x, circumcenter_y), circumradius + 15, color = color,segments=500)
    draw_circle_stroke((circumcenter_x, circumcenter_y), circumradius + 20, color = color,segments=500)
    draw_circle_stroke((circumcenter_x, circumcenter_y), circumradius + 25, color = color,segments=500)
    draw_circle_stroke((circumcenter_x, circumcenter_y), circumradius + 30, color = color,segments=500)
    draw_circle_stroke((circumcenter_x, circumcenter_y), circumradius + 35, color = color,segments=500)
    draw_circle_stroke((circumcenter_x, circumcenter_y), circumradius + 40, color = color,segments=500)
    draw_circle_stroke((circumcenter_x, circumcenter_y), circumradius + 45, color = color,segments=500)
    draw_circle_stroke((circumcenter_x, circumcenter_y), circumradius + 50, color = (0,0,0),segments=500)

    # Draw the circumcircle
    draw_circle_stroke((circumcenter_x, circumcenter_y), circumradius,color = color, segments=500)

    return (circumcenter_x, circumcenter_y), circumradius

def draw_stroked_triangle():
    # Calculate the centroid of the U-shape
    centroid_x = 585
    centroid_y = 325
    
    # Calculate the length of each side of the triangle
    triangle_side_length = 390
    
    # Calculate the vertices of the triangle
    vertices = [
        (centroid_x - triangle_side_length / 2, centroid_y + triangle_side_length / (2 * np.sqrt(3))),  # Top vertex
        (centroid_x + triangle_side_length / 2, centroid_y + triangle_side_length / (2 * np.sqrt(3))),  # Right vertex
        (centroid_x, centroid_y - triangle_side_length / np.sqrt(3))  # Bottom vertex
    ]

    # Draw the thicker stroke
    glColor3f(1.0, 1.0, 1.0)  # White color for outline
    glLineWidth(20)  # Set the line width
    
    glBegin(GL_LINES)
    for i in range(len(vertices)):
        # Connect each vertex to the next one and back to the first one
        glVertex2f(*vertices[i])
        next_index = (i + 1) % len(vertices)
        glVertex2f(*vertices[next_index])
    glEnd()
    
    #FOR STROKE
    # Draw thick lines manually using polygons inside the filled triangle
    glBegin(GL_POLYGON)
    glVertex2f(vertices[0][0], vertices[0][1] +5 )  
    glVertex2f(vertices[1][0], vertices[1][1]+5)
    glVertex2f(vertices[1][0], vertices[1][1] - 20)  
    glVertex2f(vertices[0][0], vertices[0][1] - 20)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(vertices[1][0], vertices[1][1] + 20)  
    glVertex2f(vertices[2][0], vertices[2][1] + 20)
    glVertex2f(vertices[2][0], vertices[2][1] - 20)  
    glVertex2f(vertices[1][0], vertices[1][1] - 20)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(vertices[2][0], vertices[2][1] + 20)  
    glVertex2f(vertices[0][0], vertices[0][1] + 20)
    glVertex2f(vertices[0][0], vertices[0][1] - 20)  
    glVertex2f(vertices[2][0], vertices[2][1] - 20)
    glEnd()

    draw_filled_circle((vertices[0][0], vertices[0][1]), 30,color=(1,1,1),segments = 500)
    draw_filled_circle((vertices[1][0], vertices[1][1]), 30,color=(1,1,1),segments = 500)
    draw_filled_circle((vertices[2][0], vertices[2][1]), 30,color=(1,1,1),segments = 500)

def draw_floral_pattern(origin=(0,0),radius=255, num_petals=12, petal_radius=20, color=(1, 0, 0)):
    for i in range(num_petals):
        angle = 2 * math.pi * i / num_petals
        x = origin[0] + radius * math.cos(angle)
        y = origin[1] + radius * math.sin(angle)
        draw_filled_circle(x, y, petal_radius, color)

        
if __name__ == "__main__":
    Logo()
