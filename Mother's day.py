#pip install pygame
import pygame
from time import sleep
pygame.init()
window = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
#sleep(5)
pygame.mixer.init()
pygame.mixer.music.load('O Meri Maa project.mpeg')
pygame.mixer.music.play()
sleep(1.5)
image=pygame.image.load('mother7.png')
window.blit(image,(0,0))
pygame.display.update()
sleep(15)