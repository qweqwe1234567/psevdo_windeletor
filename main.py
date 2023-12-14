from time import sleep
import pygame

pygame.init()

screen = pygame.display.set_mode((850, 150))
pygame.display.set_caption('WINDELETOR')
pygame_icon = pygame.image.load('icon.jpeg')
pygame.display.set_icon(pygame_icon)
font = pygame.font.SysFont("Lucida Console", 35)
label = font.render("Поздравляю с загрузкой WINDELETOR", 1, (12, 140, 0, 1))


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			#sleep(0.1)
			#screen = pygame.display.set_mode((850, 150))
			#pygame.display.set_caption('ТАК НЕ ЗЯ УДАЛИТЬ WINDELETOR')

	screen.fill((0, 0, 0))
	screen.blit(label, (60, 50))
	pygame.display.update()