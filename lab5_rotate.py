from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

no_mat = (0.0, 0.0, 0.0, 1.0)
mat_ambient = (0.7, 0.7, 0.7, 1.0)# Параметры фонового освещения
mat_ambient_color = (0.8, 0.8, 0.2, 1.0)
mat_diffuse = (0, 1, 0, 1.0)
mat_diffuse2 = (1,0,0,1)
mat_specular = (1.0, 1.0, 1.0, 1.0)# Цвет блика белый
no_shininess = 0.0 # Размер блика (обратная пропорция)
low_shininess = (5.0) # Размер блика (большая площадь)
high_shininess = (100.0) # Размер блика (маленькая площадь - большой фокус)
mat_emission = (0.8, 0.0, 0.2, 0.0)# Красноватое излучение
white_light = (1.0, 1.0, 1.0, 1.0)# Цвет и интенсивность 
                  # освещения, генерируемого источником
light_position = (1.0, 1.0, 0.0, 0.0)# Расположение источника
lmodel_ambient = (0.5, 0.5, 0.5, 1.0)# Параметры фонового освещения
  
isBecomeDiff = False

def SetLightMultiMaterial():

  glClearColor(0.0, 0.0, 0.0, 1.0)
  glShadeModel(GL_SMOOTH)
  
  glLightfv(GL_LIGHT0, GL_POSITION, light_position)
  glLightfv(GL_LIGHT0, GL_DIFFUSE, white_light)
  glLightfv(GL_LIGHT0, GL_SPECULAR, white_light)
  glLightModelfv(GL_LIGHT_MODEL_AMBIENT, lmodel_ambient)
  
  glEnable(GL_LIGHTING)
  glEnable(GL_LIGHT0)
  glEnable(GL_DEPTH_TEST)

  

def RenderSceneMultiMaterial():
  global xRot

  global yRot

  global zRot

  global w, h

  global isBecomeDiff
  # Сбрасываем буфер цвета и буфер глубины
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  
  ## Рисуем левую верхнюю сферу
  #glPushMatrix()#Сохранить матрицу преобразования модели
  #glTranslatef(-.75, 0.75, 0.0)
  #glRotatef(xRot, 1.0, 0.0, 0.0)
  #glRotatef(yRot, 0.0, 1.0, 0.0)
  #glRotatef(zRot, 0.0, 0.0, 1.0)
  #glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient_color)
  #glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
  #glMaterialfv(GL_FRONT, GL_SPECULAR, no_mat)
  #glMaterialfv(GL_FRONT, GL_SHININESS, no_shininess)
  #glMaterialfv(GL_FRONT, GL_EMISSION, no_mat)
  #glutSolidSphere(0.75, 16, 16) # Диаметр, число параллелей и меридиан
  #glPopMatrix()# Восстановить матрицу преобразования модели
  
  # Рисуем правую верхнюю сферу
#   glPushMatrix()# Сохранить матрицу преобразования модели
#   glTranslatef(0.75, 0.75, 0.0)
#   glRotatef(xRot, 1.0, 0.0, 0.0)
#   glRotatef(yRot, 0.0, 1.0, 0.0)
#   glRotatef(zRot, 0.0, 0.0, 1.0)
#   glMaterialfv(GL_FRONT, GL_AMBIENT, (0.1,0.1,0.1)) #(0.5,0.8,0,5) (0.3,0.3,0.3)
#   glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
#   glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
#   glMaterialfv(GL_FRONT, GL_SHININESS, low_shininess)
#   glMaterialfv(GL_FRONT, GL_EMISSION, no_mat)
#   glutSolidTeapot(0.3) # Диаметр, число параллелей и меридиан
#   glPopMatrix()# Восстановить матрицу преобразования модели
  
  # Рисуем левую нижнюю сферу
  glPushMatrix()# Сохранить матрицу преобразования модели
  glTranslatef(-0.75, -0.75, 0.0)
  glRotatef(xRot, 1.0, 0.0, 0.0)
  glRotatef(yRot, 0.0, 1.0, 0.0)
  glRotatef(zRot, 0.0, 0.0, 1.0)
  if (not isBecomeDiff):
    glMaterialfv(GL_FRONT, GL_AMBIENT, (0.1,0.1,0.1)) #(0.5,0.8,0,5) (0.3,0.3,0.3)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse2)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, low_shininess)
    glMaterialfv(GL_FRONT, GL_EMISSION, no_mat)
  else:
      glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)  
  glutSolidSphere(0.5, 16, 16) # Диаметр, число параллелей и меридиан
  glPopMatrix()# Восстановить матрицу преобразования модели
  
  ## Рисуем правую нижнюю сферу
  glPushMatrix()# Сохранить матрицу преобразования модели
  glTranslatef(0.75, -0.75, 0.0)
  glRotatef(xRot, -1.0, 0.0, 0.0)
  glRotatef(yRot, 0.0, -1.0, 0.0)
  glRotatef(zRot, 0.0, 0.0, -1.0)
  if (not isBecomeDiff):
    glMaterialfv(GL_FRONT, GL_AMBIENT, (0.1,0.1,0.1)) #(0.5,0.8,0,5) (0.3,0.3,0.3)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, low_shininess)
    glMaterialfv(GL_FRONT, GL_EMISSION, no_mat)
  else:
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse2) 
  glutSolidSphere(0.5, 16, 16) # Диаметр, число параллелей и меридиан
  glPopMatrix()# Восстановить матрицу преобразования модели
  
  yRot += 1.0
  glutSwapBuffers()
  
  glFlush()

  

def ChangeSizeMultiMaterial(width, height):

  # Индивидуальные настройки освещения
    SetLightMultiMaterial()
  
  # Предотвращаем деление на нуль
    if(height == 0):
        height = 1
  
  # Устанавливаем поле просмотра с размерами окна
    glViewport(0, 0, width, height)
  
  # Устанавливает матрицу преобразования в режим проецирования
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
  
  # Устанавливаем размеры ортогонального отсекающего объема
    aspectRatio = width / height# Для соблюдения пропорций
  
    if (width <= height):
        glOrtho (-1.5, 1.5, -1.5 / aspectRatio, 1.5 / aspectRatio, -10.0, 10.0)
    else:
        glOrtho (-1.5 * aspectRatio, 1.5 * aspectRatio, -1.5, 1.5, -10, 10)
  
  # Восстановливает матрицу преобразования в исходный режим вида
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

  
choice = 1
  

global xRot
xRot = 0.0
global yRot
yRot = 0.0
global zRot
zRot = 0.0
global w, h 
  

def ExecuteMenu():

    global xRot
    global yRot
    global zRot
    global w, h

    xRot = yRot = zRot = 0
  
    glDisable(GL_LIGHTING)
   
    ChangeSizeMultiMaterial(w, h)
     
    glutPostRedisplay()

  
def RenderScene():

  # Сохранить прежние настройки OpenGL в стеке атрибутов
    glPushAttrib(GL_LIGHTING_BIT)
    RenderSceneMultiMaterial()
    glPopAttrib()
  

def ChangeSize(width, height):
    global w, h 
    w = width
    h = height
    ChangeSizeMultiMaterial(width, height)


def TimerFunc(value):

  glutPostRedisplay() 
  glutTimerFunc(30, TimerFunc, 1)
 

def SpecialKeys( key,  x,  y):
    global isBecomeDiff
    global xRot
    global yRot
    global zRot

    if(key == GLUT_KEY_UP):  # Стрелка вверх
        xRot -= 5.0 
    if(key == GLUT_KEY_DOWN):# Стрелка вниз
        xRot += 5.0 
    if(key == GLUT_KEY_LEFT):# Стрелка влево
        yRot -= 5.0 
    if(key == GLUT_KEY_RIGHT):# Стрелка вправо
        yRot += 5.0
    if (key == GLUT_KEY_RIGHT):
        isBecomeDiff = True
    if (key == GLUT_KEY_LEFT):
        isBecomeDiff = False

    glutPostRedisplay()

  

  #glutInit(&argc, argv)
glutInit()
  # Двойная буферизация, цветовая модель RGB, буфер глубины
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(800, 800)    # Начальные размеры окна
glutCreateWindow("TEAPOTS")  # Заголовок окна
glutDisplayFunc(RenderScene)  # Обновление сцены при разрушении окна
glutReshapeFunc(ChangeSize)  # При изменении размера окна
glutTimerFunc(100, TimerFunc, 1)  # Создали таймер
glutSpecialFunc(SpecialKeys)    # Для управления с клавиатуры

glutMainLoop()  # Цикл сообщений графического окна