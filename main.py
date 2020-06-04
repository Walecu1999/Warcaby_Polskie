import pygame
from plansza import Plansza
# Uruchomienie programu
pygame.init()
##
# Ekran gry
SZEROKOSC = 1200
WYSOKOSC = 1200
SZEROKOSC_PLANSZY = 800
WYSOKOSC_PLANSZY = 800

KOLOR_TLA = (10, 150, 30)
EKRAN = pygame.display.set_mode((WYSOKOSC, SZEROKOSC))
PLANSZOWKA = Plansza(WYSOKOSC_PLANSZY, SZEROKOSC_PLANSZY, EKRAN)
#Pionki
BIALY = pygame.image.load("assets/bialy_pionek.png")
CZARNY = pygame.image.load("assets/czarny_pionek.png")
GRACZ_1X = -360
GRACZ_1Y = 360
GRACZ_2X = -280
GRACZ_2Y = -360

#def pionek():

#def damka():
def gracz1():
    g1_x = GRACZ_1X
    g1_y = GRACZ_1Y
    for i in range(0, 4):
        for j in range(0, 10):
            EKRAN.blit(BIALY, (g1_x, g1_y))
            g1_x = g1_x + SZEROKOSC_PLANSZY / 5
        if i % 2 == 0:
            g1_x = GRACZ_1X + SZEROKOSC_PLANSZY / 10
            g1_y = g1_y - WYSOKOSC_PLANSZY / 10
        else:
            g1_x = GRACZ_1X
            g1_y = g1_y - WYSOKOSC_PLANSZY / 10
def gracz2():
    g2_x = GRACZ_2X
    g2_y = GRACZ_2Y
    for i in range(0, 4):
        for j in range(0, 10):
            EKRAN.blit(CZARNY, (g2_x, g2_y))

            g2_x = g2_x + SZEROKOSC_PLANSZY / 5
        if i % 2 == 0:
            g2_x = GRACZ_1X
            g2_y = g2_y + WYSOKOSC_PLANSZY / 10
        else:
            g2_x = GRACZ_1X - SZEROKOSC_PLANSZY / 10
            g2_y = g2_y + WYSOKOSC_PLANSZY / 10




#Tytul i ikona
pygame.display.set_caption("Warcaby Polskie by Maciej Walczyk")
IKONA = pygame.image.load("assets/ikona.png")
pygame.display.set_icon(IKONA)


WLACZONY = 1
plansza = Plansza(WYSOKOSC_PLANSZY, SZEROKOSC_PLANSZY, EKRAN)
while WLACZONY:
    EKRAN.fill(KOLOR_TLA)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            WLACZONY = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            print( mx,  my)
    #gracz1()
    #gracz2()
    PLANSZOWKA.rysuj()
    #gracz1()
    #gracz2()

    pygame.display.update()

def checkboard(x):
    list = [[(j + i) % 2 for j in range(1, x + 1)] for i in range(x)]
    return list
