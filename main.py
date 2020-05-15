import pygame

#Pionki
bialy= pygame.image.load("assets/bialy_pionek.png")
czarny= pygame.image.load("assets/czarny_pionek.png")
gracz1x = 1200
gracz1y = 600
gracz2x = 400
gracz2y=350
# Uruchomienie programu
pygame.init()

def gracz1():
    ekran.blit(bialy, (gracz1x, gracz1y))
def gracz2():
    ekran.blit(czarny, (gracz2x, gracz2y))
# Ekran gry

ekran = pygame.display.set_mode((1800,1000))

#Tytul i ikona
pygame.display.set_caption("Warcaby Polskie by Maciej Walczyk")
ikona = pygame.image.load("assets/ikona.png")
pygame.display.set_icon(ikona)
wlaczony = 1
while wlaczony:
    ekran.fill((205,205,205))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            wlaczony = 0
    gracz1()
    gracz2()
    pygame.display.update()