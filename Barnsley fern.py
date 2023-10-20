# -*- coding: utf-8 -*-
import pygame
pygame.init() # Імпортуємо бібліотеку pygame
import numpy as np
import random # також імпортуємо інші потрібні бібліотеки pygame

# Створимо функцію, яка визначатиме точки папороті,
# які ми малюватимемо

# Оголосимо масив із потрібними нам коефіцієнтами
Koeficients = [[0, 0, 0, .16, 0, 0],
				 [.85, .04, -.04, .85, 0, 1.6], 
				 [.2, -.26, .23, .22, 0, 1.6],
				 [-.15, .28, .26, .24, 0, .44]]

def f(x, y, a, b, c, d, e, f):
	'''
Ця функція вважатиме нову точку нашої папороті,
за старими координатами x, y та аргументами a, b, c, d, e, f
'''
	return np.matrix([[a, b], [c, d]]) * np.matrix([[x], [y]]) + np.matrix([[e], [f]])

win = pygame.display.set_mode((600, 600)) # Створимо вікно 600х600
pygame.display.set_caption("Barnsley fern,MAN_ANDRIY_STRILETS") # Визначимо ім'я вікна

x, y = 0, 0 # Початкові Координати
RUN = True

while RUN:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			RUN = False
			#При натисканні кнопки вихід закриватимемо вікно

	P = random.randint(0, 100) #Виходячи з ймовірності обчислюватимемо нові координати

	if P == 0:
		XY = f(x, y, *Koeficients[0])
	elif P < 85:
		XY = f(x, y, *Koeficients[1])
	elif P < 93:
		XY = f(x, y, *Koeficients[2])
	else: 
		XY = f(x, y, *Koeficients[3])

	x = XY[0].item()
	y = XY[1].item()

	# Малюємо точки нашої папороті
	pygame.draw.line(win, (0, 255, 0), (x * 60 + 300, y * 60), 
                     (x * 60 + 300, y * 60), 1)
	pygame.display.update()

pygame.quit()