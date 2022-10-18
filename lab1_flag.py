from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import * 
import numpy

def drawRectangle(x, y, xof, yof):
    glBegin(GL_QUADS)
    glVertex3f(-x+xof, y+yof, 0)
    glVertex3f(x+xof, y+yof, 0)
    glVertex3f(x+xof, -y+yof, 0)
    glVertex3f(-x+xof, -y+yof, 0)
    glEnd()

def DrawCircle(radius, side_num, edge_only):
    if(edge_only):
        glBegin(GL_LINE_LOOP)
    else:
        glBegin(GL_POLYGON)
    
    for vertex in range(0, side_num):
        angle  = float(vertex) * 2.0 * numpy.pi / side_num
        glVertex2f(numpy.cos(angle)*radius, numpy.sin(angle)*radius)
    glEnd()

def DrawStar(radius, edge_num, edge_only):
    
    if(edge_only):
        glBegin(GL_LINE_LOOP)
    else:
        glBegin(GL_POLYGON)
    edge_num =edge_num*2
    for vertex in range(0, edge_num):
        angle  = float(vertex) * 2.0 * numpy.pi / edge_num
        if (vertex % 2 == 1):
            glVertex2f(numpy.cos(angle)*radius, numpy.sin(angle)*radius)
        else:
            glVertex2f(numpy.cos(angle)*radius/2, numpy.sin(angle)*radius/2)
    glEnd()


def draw():
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
    glClearColor(0.0, 0.0, 0.0,0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glTranslatef(0.0, 0, 1)

    glColor3f(0, 0, 194.0/255.0)
    drawRectangle(0.5, 0.1, 0, 0.2)
    glColor3f(252/255,2/255,3/255)
    drawRectangle(0.5, 0.1, 0,0)
    glColor3f(15/255,212/255,85/255)
    drawRectangle(0.5, 0.1, 0, -0.2)
    
    glTranslatef(-0.05, 0, 0)
    glColor3f(1,1,1)
    DrawCircle(0.09, 60, False)
    glTranslatef(0.018, 0, 0)
    glColor3f(252/255,2/255,3/255)
    DrawCircle(0.075, 60, False)
    glTranslatef(0.05-0.018, 0, 0)

    glTranslatef(0.07, 0, 0)
    glRotatef(20,0,0, 1)
    glColor3f(1,1,1)
    DrawStar(0.04, 8, False)
    glTranslatef(-0.07, 0, 0)
    glRotatef(-20,0,0, 1)

    glFlush()
    glutSwapBuffers()

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB) 
glutInitWindowSize(1000, 1000)
glutInitWindowPosition(50, 50)
glutInit(sys.argv)
glutCreateWindow(b"Azerbaidjan")
glutDisplayFunc(draw)
glutMainLoop()