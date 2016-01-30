# -*- coding: utf-8 -*-
# Прежде чем переходить к следующему шагу, выполните 4 задания (Задания в коде в виде TODO)
import os

import pygame


def load_image(name, alpha_cannel):
    fullname = os.path.join('Images', name)  # Указываем путь к папке с картинками

    image = pygame.image.load(fullname)  # Загружаем картинку и сохраняем поверхность (Surface)
    if alpha_cannel:
        image = image.convert_alpha()
    else:
        image = image.convert()

    return image


def move(event, x, y):
    print(event.key)
    if event.key == 276:
        x -= 10
    if event.key == 273:
        y -= 10
    if event.key == 274:
        y += 10
    if event.key == 275:
        x += 10
    # TODO(complete): Задание-3 Дописать функцию, для движения объекта во все 4 стороны
    return x, y


pygame.init()  # инициализация
display = pygame.display.set_mode((800, 600))  # создание окна
x = 50
y = 50

screen = pygame.display.get_surface()  # определяем поверхность для рисования
# TODO(complete): Задание-2 Загрузить и отобразить на сцене ещё несколько произвольных картинок
image_skeleton = load_image('skeleton.png', 1)  # загружаем картинку. Вторым аргументом указываем (есть/нет) альфа-канал
image_tree = load_image('Trees/trees_big_1.png', 1)

if image_skeleton:
    done = False
else:
    done = True

color = [(0, 0, 100), (100, 0, 0), (0, 100, 0)]
i = 0
while not done:  # главный цикл программы
    for e in pygame.event.get():  # цикл обработки очереди событий окна
        if e.type == pygame.QUIT:  # Обработка события "Закрытие окна"
            # TODO(complete): Задание-1 Дописать закрытие окна по нажатию клавиши Esc |"K_ESCAPE" - константа клавиши Esc
            done = True
        if e.type == pygame.KEYDOWN:  # Событие "Клавиша нажата"
            if e.key == pygame.K_ESCAPE:
                done = True
            if e.key == pygame.K_c:
                i += 1
                if i == 3:
                    i -= 3

            print('Key Down')
            coords = move(e, x, y)
            x = coords[0]
            y = coords[1]

        if e.type == pygame.KEYUP:  # Событие "Клавиша отпущена"
            print('Key Up')
        if e.type == pygame.MOUSEBUTTONDOWN:  # Событие "Клавиша мыши нажата"
            print('Mouse Down')
            # TODO(complete): Задание-4 При нажатии кнопки "c" реализуйте изменение цвета фона по кругу (бирюзовый,...
            # розовый, черный, бирюзовый ...)
    screen.fill(color[i])
    screen.blit(image_skeleton, (x, y))  # отрисовываем содержимое поверхности image на поверхность screen
    screen.blit(image_tree, (130, 100))
    pygame.display.flip()  # показываем на экране все что нарисовали на основной поверхности
