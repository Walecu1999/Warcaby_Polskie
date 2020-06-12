import pygame
from Pionek import Pionek
from plansza import Plansza

# Uruchomienie programu
pygame.init()
##
# Ekran gry
SZEROKOSC = 1200
WYSOKOSC = 1200
SZEROKOSC_PLANSZY = 800
WYSOKOSC_PLANSZY = 800
CZARNE_POLE = (150, 80, 40)
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

#Tytul i ikona
pygame.display.set_caption("Warcaby Polskie by Maciej Walczyk")
IKONA = pygame.image.load("assets/ikona.png")
pygame.display.set_icon(IKONA)
GRACZ_BIALY = 1
GRACZ_CZARNY = 2
GRACZ_OBECNY = GRACZ_BIALY
RED= (255, 15, 10)
WLACZONY = 1
EKRAN.fill(KOLOR_TLA)
PLANSZOWKA.rysuj_poczatek()
prawda = True
# TESTY
#PLANSZOWKA.dodaj_czarny_pionek(Pionek(3, 4, 'B', EKRAN))
#PLANSZOWKA.rysuj_poczatek()
#PLANSZOWKA.przesuwaj(PLANSZOWKA.pola_bialych[2])
#PLANSZOWKA.bicie_pionkiem(PLANSZOWKA.pola_bialych[0][1])
#WSPOLRZEDNE_PIONKOW

while WLACZONY:
    wybrany_pionek = None
    #PLANSZOWKA.rysuj_poczatek()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            WLACZONY = 0
        elif event.type == pygame.MOUSEBUTTONDOWN:
            myszka = pygame.mouse.get_pos()
            x = myszka[0]
            y = myszka[1]
            wsp_x = x // (SZEROKOSC_PLANSZY // PLANSZOWKA.KOLUMNY)
            wsp_y = y // (WYSOKOSC_PLANSZY // PLANSZOWKA.WIERSZE)

            if PLANSZOWKA.czy_mozna_ruszyc(GRACZ_OBECNY, wsp_x, wsp_y) == True:
                if GRACZ_OBECNY == 1:
                    for pioneczek in PLANSZOWKA.pola_bialych:
                        if pioneczek.wsp_x == wsp_x and pioneczek.wsp_y == wsp_y:
                            wybrany_pionek = pioneczek
                            print("JESTEM TU")
                            PLANSZOWKA.podswietlaj(wybrany_pionek)
                            prawda = True
                if GRACZ_OBECNY == 2:
                    for pioneczek in PLANSZOWKA.pola_czarnych:
                        if pioneczek.wsp_x == wsp_x and pioneczek.wsp_y == wsp_y:
                            wybrany_pionek = pioneczek
                            print("JESTEM TU")
                            PLANSZOWKA.podswietlaj(wybrany_pionek)
                            prawda = True
                while prawda:
                    event = pygame.event.wait()
                    if event.type == pygame.QUIT:
                        WLACZONY = 0
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        PLANSZOWKA.podswietlaj(wybrany_pionek)
                        pole_ruchu = pygame.mouse.get_pos()
                        pole_x = pole_ruchu[0] // (SZEROKOSC_PLANSZY // PLANSZOWKA.KOLUMNY)
                        pole_y = pole_ruchu[1] // (SZEROKOSC_PLANSZY // PLANSZOWKA.KOLUMNY)

                        if PLANSZOWKA.czy_mozna_bic(wybrany_pionek) == True:
                            temp = wybrany_pionek.wsp_x
                            PLANSZOWKA.bicie_pionkiem(GRACZ_OBECNY, wybrany_pionek, pole_x, pole_y)
                            PLANSZOWKA.czy_krolowa(GRACZ_OBECNY, wybrany_pionek)
                            prawda = False
                            if PLANSZOWKA.czy_mozna_bic(wybrany_pionek) == True:
                                print("WCIAZ MASZ JESZCZE BICIE")
                            if temp != wybrany_pionek.wsp_x:
                                if PLANSZOWKA.czy_mozna_bic(wybrany_pionek) == False:
                                    if GRACZ_OBECNY == GRACZ_BIALY:
                                        if PLANSZOWKA.pola_czarnych == []:
                                            print("KONIEC GRY, WYGRALY BIALE")
                                            WLACZONY = 0
                                        else:
                                            GRACZ_OBECNY = GRACZ_CZARNY
                                            prawda = False
                                    else:
                                        if PLANSZOWKA.pola_bialych == []:
                                            print("KONIEC GRY, WYGRALY CZARNE")

                                            WLACZONY = 0
                                        else:
                                            GRACZ_OBECNY = GRACZ_BIALY
                                            prawda = False
                            else:
                                print("MASZ BICIE! WYKONAJ JE :)")


                        elif PLANSZOWKA.czy_mozna_postawic(wybrany_pionek, pole_x, pole_y):
                            pomocnicza = wybrany_pionek.wsp_x
                            PLANSZOWKA.rusz_pionkiem(wybrany_pionek, pole_x, pole_y)
                            PLANSZOWKA.czy_krolowa(GRACZ_OBECNY, wybrany_pionek)
                            prawda = False
                            if pomocnicza != wybrany_pionek.wsp_x:
                                if GRACZ_OBECNY == GRACZ_BIALY:
                                    if PLANSZOWKA.pola_czarnych == []:
                                        print("KONIEC GRY, WYGRALY BIALE")
                                        WLACZONY = 0
                                    else:
                                        GRACZ_OBECNY = GRACZ_CZARNY
                                        prawda = False
                                else:
                                    if PLANSZOWKA.pola_bialych == []:
                                        print("KONIEC GRY, WYGRALY CZARNE")
                                        WLACZONY = 0
                                    else:
                                        GRACZ_OBECNY = GRACZ_BIALY
                                        prawda = False
                        elif PLANSZOWKA.czy_mozna_postawic(wybrany_pionek, pole_x, pole_y) == False:
                            print("DOKONALES NIEPOPRAWNEGO RUCHU, LEPIEJ GO PRZEMYSL ;) ")
                            prawda = False
            PLANSZOWKA.rysuj_poczatek()
            print(x)
            print(y)
            print(wsp_x, " ", wsp_y)

    pygame.display.update()

