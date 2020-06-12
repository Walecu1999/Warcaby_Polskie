import pygame
import time
from Pionek import Pionek
from plansza import Plansza
def main():
# Uruchomienie programu
    pygame.init()
##
# Ekran gry
    SZEROKOSC = 1400
    WYSOKOSC = 800
    SZEROKOSC_PLANSZY = 800
    WYSOKOSC_PLANSZY = 800
    CZARNE_POLE = (150, 80, 40)
    KOLOR_TLA = (255, 229, 180)
    EKRAN = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
    PLANSZOWKA = Plansza(WYSOKOSC_PLANSZY, SZEROKOSC_PLANSZY, EKRAN)

    BIALY = pygame.image.load("assets/bialy_pionek.png")
    CZARNY = pygame.image.load("assets/czarny_pionek.png")

#Tytul i ikona
    pygame.display.set_caption("Warcaby Polskie by Maciej Walczyk")
    IKONA = pygame.image.load("assets/ikona.png")
    pygame.display.set_icon(IKONA)
    ODSWIEZ = 0
    GRACZ_BIALY = 1
    GRACZ_CZARNY = 2
    GRACZ_OBECNY = GRACZ_BIALY
    KOLOR = (155, 105, 10)
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
    NUMER = 0


# WYPISYWANIE WIADOMOSCI NA EKRAN
    font = pygame.font.SysFont(None, 25)
    def wiadomosc(tresc, kolor, liczba):
        wspol_x = 810
        wspol_y = 40 + (30 * liczba)
        tekst = font.render(tresc, True, kolor)
        EKRAN.blit(tekst, [wspol_x, wspol_y])
        if liczba <= 10:
            liczba += 1
        else:
            liczba = 0
    def wiadomosc2(tresc, kolor):
        wspol_x = 1060
        wspol_y = 40
        tekst = font.render(tresc, True, KOLOR)
        EKRAN.blit(tekst, [wspol_x, wspol_y])
    wiadomosc("Hej! Życzę miłej gry! ", KOLOR, -1)
    if GRACZ_OBECNY == 1:
        wiadomosc("Teraz kolej gracza Bialych.", KOLOR, 0)
    else:
        wiadomosc2("Teraz kolej gracza Czarnych.", KOLOR)

    # GLOWNA PETLA W KTOREJ TOCZY SIE GRA

    while WLACZONY:
        wybrany_pionek = None
    #PLANSZOWKA.rysuj_poczatek()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                WLACZONY = 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                myszka = pygame.mouse.get_pos()
                wspolrzedna_x = myszka[0]
                wspolrzedna_y = myszka[1]
                wsp_x = wspolrzedna_x // (SZEROKOSC_PLANSZY // PLANSZOWKA.KOLUMNY)
                wsp_y = wspolrzedna_y // (WYSOKOSC_PLANSZY // PLANSZOWKA.WIERSZE)

                if PLANSZOWKA.czy_mozna_ruszyc(GRACZ_OBECNY, wsp_x, wsp_y) == True:
                    if GRACZ_OBECNY == 1:
                        for pioneczek in PLANSZOWKA.pola_bialych:
                            if pioneczek.wsp_x == wsp_x and pioneczek.wsp_y == wsp_y:
                                wybrany_pionek = pioneczek
                                PLANSZOWKA.podswietlaj(wybrany_pionek)
                                prawda = True
                    if GRACZ_OBECNY == 2:
                        for pioneczek in PLANSZOWKA.pola_czarnych:
                            if pioneczek.wsp_x == wsp_x and pioneczek.wsp_y == wsp_y:
                                wybrany_pionek = pioneczek
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
                                EKRAN.fill(KOLOR_TLA)
                                PLANSZOWKA.rysuj_poczatek()
                                PLANSZOWKA.czy_krolowa(GRACZ_OBECNY, wybrany_pionek)
                                prawda = False
                                if PLANSZOWKA.czy_mozna_bic(wybrany_pionek) == True:
                                    wiadomosc("Wciąż masz jeszcze bicie! Tak, tak, zrób to!", KOLOR, 3)

                                if temp != wybrany_pionek.wsp_x:
                                    if PLANSZOWKA.czy_mozna_bic(wybrany_pionek) == False:
                                        if GRACZ_OBECNY == GRACZ_BIALY:
                                            if PLANSZOWKA.pola_czarnych == []:
                                                wiadomosc("Koniec gry, wygrały Białe! Gratuluję :)", KOLOR, 4)
                                                pygame.display.update()
                                                time.sleep(6)
                                                WLACZONY = 0
                                            else:
                                                GRACZ_OBECNY = GRACZ_CZARNY
                                                EKRAN.fill(KOLOR_TLA)
                                                PLANSZOWKA.rysuj_poczatek()
                                                wiadomosc2("Teraz kolej gracza Czarnych.", KOLOR)
                                                pygame.display.update()
                                                prawda = False
                                        else:
                                            if PLANSZOWKA.pola_bialych == []:
                                                EKRAN.fill(KOLOR_TLA)
                                                PLANSZOWKA.rysuj_poczatek()
                                                wiadomosc("Koniec gry, wygrały Białe! Gratuluję :)", KOLOR, 5)
                                                pygame.display.update()
                                                time.sleep(6)
                                                WLACZONY = 0
                                            else:
                                                GRACZ_OBECNY = GRACZ_BIALY
                                                EKRAN.fill(KOLOR_TLA)
                                                PLANSZOWKA.rysuj_poczatek()
                                                wiadomosc("Teraz kolej gracza Bialych.", KOLOR, 0)
                                                pygame.display.update()
                                                prawda = False
                                else:
                                    EKRAN.fill(KOLOR_TLA)
                                    PLANSZOWKA.rysuj_poczatek()
                                    wiadomosc("Masz bicie, zrób je! Na komputerze "
                                              "przecież wolno bić innych!", KOLOR, 6)
                                    pygame.display.update()

                            elif PLANSZOWKA.czy_mozna_postawic(wybrany_pionek, pole_x, pole_y):
                                pomocnicza = wybrany_pionek.wsp_x
                                PLANSZOWKA.rusz_pionkiem(wybrany_pionek, pole_x, pole_y)
                                PLANSZOWKA.czy_krolowa(GRACZ_OBECNY, wybrany_pionek)
                                prawda = False
                                if pomocnicza != wybrany_pionek.wsp_x:
                                    if GRACZ_OBECNY == GRACZ_BIALY:
                                        if PLANSZOWKA.pola_czarnych == []:
                                            EKRAN.fill(KOLOR_TLA)
                                            PLANSZOWKA.rysuj_poczatek()
                                            wiadomosc("Koniec gry, wygrały Białe! Gratuluję :)", KOLOR, 7)
                                            pygame.display.update()
                                            time.sleep(6)
                                            WLACZONY = 0
                                        else:
                                            EKRAN.fill(KOLOR_TLA)
                                            PLANSZOWKA.rysuj_poczatek()
                                            wiadomosc2("Teraz kolej gracza Czarnych.", KOLOR)
                                            pygame.display.update()
                                            GRACZ_OBECNY = GRACZ_CZARNY
                                            prawda = False
                                    else:
                                        if PLANSZOWKA.pola_bialych == []:
                                            wiadomosc("Koniec gry, wygrały Czarne! Gratuluję :)", KOLOR, 7)
                                            pygame.display.update()
                                            time.sleep(6)
                                            WLACZONY = 0
                                        else:
                                            GRACZ_OBECNY = GRACZ_BIALY
                                            EKRAN.fill(KOLOR_TLA)
                                            PLANSZOWKA.rysuj_poczatek()
                                            wiadomosc("Teraz kolej gracza Bialych.", KOLOR, 0)
                                            pygame.display.update()
                                            prawda = False
                            elif PLANSZOWKA.czy_mozna_postawic(wybrany_pionek, pole_x, pole_y) == False:
                                EKRAN.fill(KOLOR_TLA)
                                PLANSZOWKA.rysuj_poczatek()
                                wiadomosc("Wykonałeś nie do końca poprawny ruch, "
                                          "no ale dam Ci szansę ;) ", KOLOR, 8)
                                pygame.display.update()
                                prawda = False
                PLANSZOWKA.rysuj_poczatek()


        pygame.display.update()

if __name__ == '__main__':
    main()