#Алгоритм Роджерса (или алгоритм отсечения невидимых граней по методу Роджерса) - это метод, который позволяет определить, 
#какие грани трехмерного объекта видны, а какие скрыты от наблюдателя. Этот алгоритм основывается на использовании проекций граней и их глубине. 

#Этот код создает трехмерный объект, проецирует его на двумерный экран, а затем использует алгоритм Роджерса для определения видимых граней и их отрисовки.

import pygame
from pygame.locals import *

# Инициализация Pygame
pygame.init()

# Размеры экрана
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Rogers Algorithm')

# Задание вершин и граней трехмерного объекта
vertices = [
    (100, 100, 100),  # Вершина A
    (300, 100, 100),  # Вершина B
    (300, 300, 100),  # Вершина C
    (100, 300, 100),  # Вершина D
    (100, 100, 300),  # Вершина E
    (300, 100, 300),  # Вершина F
    (300, 300, 300),  # Вершина G
    (100, 300, 300)   # Вершина H
]

# Грани трехмерного объекта
faces = [
    (0, 1, 2, 3),  # Грань ABCD
    (4, 5, 6, 7),  # Грань EFGH
    (0, 1, 5, 4),  # Грань ABEF
    (2, 3, 7, 6),  # Грань CDGH
    (1, 2, 6, 5),  # Грань BCGF
    (0, 3, 7, 4)   # Грань ADHE
]

# Параметры наблюдателя
viewer_position = (200, 200, -500)

# Функция для проецирования вершин трехмерного объекта на двумерный экран
def project_vertices(vertices):
    projected_vertices = []
    for vertex in vertices:
        x = vertex[0] + viewer_position[0]
        y = vertex[1] + viewer_position[1]
        z = vertex[2] + viewer_position[2]
        projected_vertices.append((x / z * 100 + width / 2, y / z * 100 + height / 2))
    return projected_vertices

# Функция для отрисовки трехмерного объекта с использованием алгоритма Роджерса
def draw_object(vertices, faces):
    for face in faces:
        visible = True
        for i in range(len(face)):
            # Вычисление вектора нормали для грани
            v1 = (vertices[face[(i + 1) % len(face)]] - vertices[face[i]])
            v2 = (vertices[face[(i + 2) % len(face)]] - vertices[face[i]])
            normal = (v1[1]*v2[2] - v1[2]*v2[1], v1[2]*v2[0] - v1[0]*v2[2], v1[0]*v2[1] - v1[1]*v2[0])

            # Вычисление вектора направления от грани к наблюдателю
            view_vector = (viewer_position[0] - vertices[face[i]][0], viewer_position[1] - vertices[face[i]][1],
                           viewer_position[2] - vertices[face[i]][2])

            # Проверка, направлен ли вектор нормали к наблюдателю
            dot_product = normal[0] * view_vector[0] + normal[1] * view_vector[1] + normal[2] * view_vector[2]
            if dot_product < 0:
                visible = False
                break

        if visible:
            pygame.draw.polygon(screen, (255, 255, 255), project_vertices([vertices[i] for i in face]))

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill((0, 0, 0))

    # Отрисовка трехмерного объекта
    draw_object(vertices, faces)

    pygame.display.flip()
    pygame.time.delay(10)

pygame.quit()
--------------------------------------------

import pygame
from pygame.locals import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Инициализация Pygame
pygame.init()

# Размеры экрана
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Rogers Algorithm')

# Параметры наблюдателя
viewer_position = (200, 200, -500)

# Функция для проецирования вершин трехмерного объекта на двумерный экран
def project_vertices(vertices):
    projected_vertices = []
    for vertex in vertices:
        x = vertex[0] + viewer_position[0]
        y = vertex[1] + viewer_position[1]
        z = vertex[2] + viewer_position[2]
        projected_vertices.append((x / z * 100 + width / 2, y / z * 100 + height / 2))
    return projected_vertices

# Функция для отрисовки трехмерного объекта с использованием алгоритма Роджерса
def draw_object(vertices):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Разбиение вершин объекта на отдельные списки координат
    x = [v[0] for v in vertices]
    y = [v[1] for v in vertices]
    z = [v[2] for v in vertices]

    # Отрисовка объекта
    ax.plot_trisurf(x, y, z)

    # Настройка осей
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

# Отрисовка трехмерного объекта
vertices = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
draw_object(vertices)
