# -*- coding: utf-8 *-*
# Множина мандельброту на python
# Використовуватимемо бібліотеку pygame
import pygame # іпортуємо її
pygame.init() # ініціалізуємо

win = pygame.display.set_mode((600, 600)) # створюємо вікно 600х600 пікселів

pygame.display.set_caption("Mandelbrot set,MAN_STRILETS_ANDRIY") # надамо ім'я вікну

# Все працює, але повільно, тому винесемо обробку точок за головний цикл,
# він тільки все малюватиме
for x in range(600):
	for y in range(600):
		i, j = (x - 300) / 150, (y - 300) / 150 # Дійсна та уявна частини числа
		c = (i + j*((-1)**.5))

		In_Mandelbrot = True
		z = 0 #значення z
		for i in range(50): # Кількість ітерацій нашої множини

			z = z**2 + c # скористаємося формулою
			if abs(z) >= 2:
				In_Mandelbrot = False
				break
		color = round(255 * min(abs(c)/2, 1))
		if In_Mandelbrot:
			pygame.draw.line(win, (color, color, color), (x, y), (x, y), 1)

RUN = True
while RUN: # Головний цикл для обробки подій
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			RUN = False # При натисканні кнопки вихід виходимо із головного циклу
	
	# Малюємо осі дійсних і Уявних чисел
	pygame.draw.line(win, (255, 255, 255), (0, 300), (600, 300), 1) # Real - x
	pygame.draw.line(win, (255, 255, 255), (300, 0), (300, 600), 1) # Imaginary - y

	
	pygame.display.update() # Малюємо координатну площину
	pygame.time.delay(33) # Робимо затримку після малювання кадру

pygame.quit()
