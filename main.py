import pygame
from plansza import Plansza
# Uruchomienie programu
pygame.init()

#Pionki
bialy = pygame.image.load("assets/bialy_pionek.png")
czarny = pygame.image.load("assets/czarny_pionek.png")
gracz1x = 200
gracz1y = 200
gracz2x = 100
gracz2y=150

#def pionek():

#def damka():
def gracz1():
    ekran.blit(bialy, (gracz1x, gracz1y))
def gracz2():
    ekran.blit(czarny, (gracz2x, gracz2y))
# Ekran gry
szerokosc=800
wysokosc=800
kolor_tla=(10,150,30)
ekran = pygame.display.set_mode((wysokosc,szerokosc))
planszowka= Plansza(wysokosc,szerokosc,ekran)


#Tytul i ikona
pygame.display.set_caption("Warcaby Polskie by Maciej Walczyk")
ikona = pygame.image.load("assets/ikona.png")
pygame.display.set_icon(ikona)


wlaczony = 1
while wlaczony:
    ekran.fill(kolor_tla)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            wlaczony = 0
    gracz1()
    gracz2()
    planszowka.rysuj()
    pygame.display.update()

def checkboard(x):
    list = [[(j + i) % 2 for j in range(1, x + 1)] for i in range(x)]
    return list

