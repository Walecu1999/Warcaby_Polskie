import pygame
from Pionek import Pionek
from itertools import chain
BIALY = pygame.image.load("assets/bialy_pionek.png")
CZARNY = pygame.image.load("assets/czarny_pionek.png")
class Plansza(object):
    CZARNY = 1
    NOTDONE = -1
    KOLUMNY = 10
    WIERSZE = 10
    BIALE_POLE = (255, 255, 255)
    CZARNE_POLE = (100, 99, 45)
    def __init__(self, wysokosc, szerokosc, ekran):
        self.ekran = ekran
        self.wysokosc = wysokosc
        self.szerokosc = szerokosc
        self.gracze = ['C', 'B']
        self.pola_puste =  [[Pionek(x, y, '-', self.ekran) for x in range((y + 1) % 2, 10, 2)] for y in range(0, 4)]
        self.pola_pustych = list(chain.from_iterable(self.pola_puste))
        self.pola_czarne = [[Pionek(x, y, 'C', self.ekran) for x in range((y + 1) % 2, self.KOLUMNY, 2)] for y in range(4,5)]
        self.pola_czarnych = list(chain.from_iterable(self.pola_czarne))
        self.pola_biale = [[Pionek(x, y, 'B', self.ekran) for x in range((y + 1) % 2, self.KOLUMNY, 2)] for y in range(5, self.WIERSZE)]
        self.pola_bialych = list(chain.from_iterable(self.pola_biale))

        self.wsp_puste = []
        self.wsp_biale = []
        self.wsp_czarne = []
        self.lista_ruchow = []
        self.lista_pionow_do_bicia = []
       # for i in range(4):
          #  for j in range(4):
         #       print(lista_pionkow_b[i][j].wsp_x ," ", lista_pionkow_b[i][j].wsp_y)
        self.tablica = [['-', 'C', '-', 'C', '-', 'C', '-', 'C', '-', 'C'],
                        ['C', '-', 'C', '-', 'C', '-', 'C', '-', 'C', '-'],
                        ['-', 'C', '-', 'C', '-', 'C', '-', 'C', '-', 'C'],
                        ['C', '-', 'C', '-', 'C', '-', 'C', '-', 'C', '-'],
                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                        ['-', 'B', '-', 'B', '-', 'B', '-', 'B', '-', 'B'],
                        ['B', '-', 'B', '-', 'B', '-', 'B', '-', 'B', '-'],
                        ['-', 'B', '-', 'B', '-', 'B', '-', 'B', '-', 'B'],
                        ['B', '-', 'B', '-', 'B', '-', 'B', '-', 'B', '-']]


    def checkboard(x):
        list = [[(j + i) % 2 for j in range(1, x + 1)] for i in range(x)]
        return list
    def tworz_plansze(self):
        tablica = [[i for kolumna in range(self.KOLUMNY)]
                   for wiersz in range(self.WIERSZE)]
        return tablica
    def sasiednie(self, pionek):
        if pionek.kolor == 'B':
            for i in self.pola_pustych:
                if i.wsp_x == pionek.wsp_x + 1 and i.wsp_y == pionek.wsp_y - 1:
                    self.lista_ruchow.append((pionek.wsp_x + 1, pionek.wsp_y - 1))
                if i.wsp_x == pionek.wsp_x - 1 and i.wsp_y == pionek.wsp_y -1:
                    self.lista_ruchow.append((pionek.wsp_x - 1, pionek.wsp_y - 1))
        if pionek.kolor == 'C':
            for i in self.pola_pustych:
                if i.wsp_x == pionek.wsp_x + 1 and i.wsp_y == pionek.wsp_y + 1:
                    self.lista_ruchow.append((pionek.wsp_x + 1, pionek.wsp_y + 1))
                if i.wsp_x == pionek.wsp_x - 1 and i.wsp_y == pionek.wsp_y + 1:
                    self.lista_ruchow.append((pionek.wsp_x - 1, pionek.wsp_y + 1))
    def bicie_pionkiem(self,pionek):
        if pionek.kolor == 'B':
            if pionek.wsp_x + 2 < 10 and pionek.wsp_y - 2 > 0:
                listunia = self.pola_czarnych.copy()
                for pioneczek in listunia:
                    if pioneczek.wsp_x == pionek.wsp_x + 1 and pioneczek.wsp_y == pionek.wsp_y - 1:
                        for j in self.pola_pustych:
                            if j.wsp_x == pionek.wsp_x + 2 and j.wsp_y == pionek.wsp_y -2:
                                self.lista_pionow_do_bicia.append((pionek.wsp_x + 1, pionek.wsp_y - 1))
                                print(pionek.wsp_x, pionek.wsp_y)
                                print("LISTA: ", self.lista_pionow_do_bicia)
            if pionek.wsp_x - 2 >= 0 and pionek.wsp_y - 2 > 0:
                listunia = self.pola_czarnych.copy()
                for pioneczek in listunia:
                    if pioneczek.wsp_x == pionek.wsp_x - 1 and pioneczek.wsp_y == pionek.wsp_y - 1:
                        for j in self.pola_pustych:
                            if j.wsp_x == pionek.wsp_x - 2 and j.wsp_y == pionek.wsp_y -2:
                                self.lista_pionow_do_bicia.append((pionek.wsp_x -1, pionek.wsp_y - 1))
                                print(pionek.wsp_x, pionek.wsp_y)
                                print("LISTA: ", self.lista_pionow_do_bicia)
        if pionek.kolor == 'C':
            if pionek.wsp_x + 2 < self.WIERSZE and pionek.wsp_y + 2 < self.KOLUMNY:
                listunia = self.pola_bialych.copy()
                for pioneczek in listunia:
                    if pioneczek.wsp_x == pionek.wsp_x + 1 and pioneczek.wsp_y == pionek.wsp_y + 1:
                        for j in self.pola_pustych:
                            if j.wsp_x == pionek.wsp_x + 2 and j.wsp_y == pionek.wsp_y + 2:
                                self.lista_pionow_do_bicia.append((pionek.wsp_x + 1, pionek.wsp_y + 1))
                                print("LISTA: ", self.lista_pionow_do_bicia)
            if pionek.wsp_x - 2 >= 0 and pionek.wsp_y + 2 < self.KOLUMNY:
                listunia = self.pola_bialych.copy()
                for pioneczek in listunia:
                    if pioneczek.wsp_x == pionek.wsp_x - 1 and pioneczek.wsp_y == pionek.wsp_y + 1:
                        for j in self.pola_pustych:
                            if j.wsp_x == pionek.wsp_x - 2 and j.wsp_y == pionek.wsp_y + 2:
                                self.lista_pionow_do_bicia.append((pionek.wsp_x - 1, pionek.wsp_y + 1))
                                print("LISTA: ", self.lista_pionow_do_bicia)

    def dodaj_bialy_pionek(self, pionek):
        self.pola_bialych.append(Pionek(pionek.wsp_x, pionek.wsp_y, 'B', self.ekran))
        wymiar_pola = self.szerokosc / 10
        self.ekran.blit(BIALY, (pionek.wsp_x * wymiar_pola - 360, pionek.wsp_y * wymiar_pola - 360))
        print(self.pola_bialych)

    def dodaj_czarny_pionek(self, pionek):
        self.pola_czarnych.append((pionek.wsp_x, pionek.wsp_y, 'C', self.ekran))
        wymiar_pola = self.szerokosc / 10
        self.ekran.blit(CZARNY, (pionek.wsp_x * wymiar_pola - 360, pionek.wsp_y * wymiar_pola - 360))
        print(self.pola_bialych)
       # for i in self.pola_pustych:
         #   if i.wsp_x == pionek.wsp_x and i.wsp_y == pionek.wsp_y:
             #   self.pola_pustych.pop(i)

       # print("Lista ruchow:  ", self.lista_ruchow)
        #print(pionek.wsp_x)
        #print(pionek.wsp_y)
        #print(self.pola_pustych[6].wsp_x)
       #print(self.pola_pustych[6].wsp_y)

    def rysuj_poczatek(self):
        #kolor_planszy=self.checkboard()
        kolor_pola = 0
        kolor_pola2 = 0
        wsp_x, wsp_y = 0, 0
        wymiar_pola = self.szerokosc / 10

        for i in range(0, self.WIERSZE):
            for j in range(0, self.KOLUMNY):
                if (kolor_pola + kolor_pola2) % 2:
                    kolor_pola = kolor_pola+1
                    pygame.draw.rect(self.ekran, self.CZARNE_POLE, pygame.Rect(wsp_x, wsp_y, self.szerokosc / 10, self.wysokosc / 10))
                else:
                    kolor_pola = kolor_pola+1
                    pygame.draw.rect(self.ekran, self.BIALE_POLE, pygame.Rect(wsp_x, wsp_y, self.szerokosc / 10, self.wysokosc / 10))
                wsp_x += self.szerokosc / 10
            wsp_y += self.wysokosc/10
            wsp_x = 0
            kolor_pola2 += 1

        lista_pionkow = self.pola_bialych.copy()
        lista_pionkow.extend(self.pola_czarnych)
        lista_pionkow.extend(self.pola_puste)
        print(self.pola_czarnych)
        for pionek in lista_pionkow:
            try:
                if pionek.kolor == 'C':
                    self.ekran.blit(CZARNY, (pionek.wsp_x*wymiar_pola - 360, pionek.wsp_y*wymiar_pola - 360))
                    self.wsp_czarne.extend(pionek.wsp_x, pionek.wsp_y)
                elif pionek.kolor == 'B':
                    self.ekran.blit(BIALY, (pionek.wsp_x * wymiar_pola - 360, pionek.wsp_y * wymiar_pola - 360))
                    self.wsp_biale.extend(pionek.wsp_x, pionek.wsp_y)
                else:
                    pygame.draw.rect(self.ekran, self.CZARNE_POLE,
                                         pygame.Rect(wsp_x, wsp_y, self.szerokosc / 10, self.wysokosc / 10))
                    self.wsp_puste.extend(pionek.wsp_x, pionek.wsp_y)
            except Exception:
                pass

    def przesuwaj(self, pionek):
        wymiar_pola = self.szerokosc / 10
        if pionek.kolor == 'C':
            self.ekran.blit(CZARNY, (pionek.wsp_x * wymiar_pola - 360, pionek.wsp_y * wymiar_pola - 360))
            pygame.draw.rect(self.ekran, self.CZARNE_POLE,
                             pygame.Rect(pionek.wsp_x * wymiar_pola, pionek.wsp_y * wymiar_pola, self.szerokosc / 10,
                                         self.wysokosc / 10))
        elif pionek.kolor == 'B':
            self.ekran.blit(BIALY, (pionek.wsp_x * wymiar_pola - 360, pionek.wsp_y * wymiar_pola - 360))
            pygame.draw.rect(self.ekran, self.CZARNE_POLE,
                             pygame.Rect(pionek.wsp_x * wymiar_pola, pionek.wsp_y*wymiar_pola, self.szerokosc / 10, self.wysokosc / 10))
        czcionka = pygame.font.SysFont("timesnewroman", 20, bold = True)
        #czcionka_kolor= BLACK_COLOR
    def zbicie_bialego_piona(self, pionek):
        pionek.kolor = '-'
    def ruchy(self, pionek):
        if pionek.wsp_x + 1 and pionek.wsp_y + 1:
            pionek.wsp_x += 1
            pionek.wsp_y += 1
    def draw_background(self):
        '''
        Draws background for the board
        '''
