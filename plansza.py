import pygame
import numpy
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
        self.pola_puste = [[Pionek(x, y, '-', self.ekran) for x in range((y + 1) % 2, self.KOLUMNY, 2)] for y in range(4, 6)]
        self.pola_pustych = list(chain.from_iterable(self.pola_puste))
        self.pola_czarne = [[Pionek(x, y, 'C', self.ekran) for x in range((y + 1) % 2, self.KOLUMNY, 2)] for y in range(0, 4)]
        self.pola_czarnych = list(chain.from_iterable(self.pola_czarne))
        self.pola_biale = [[Pionek(x, y, 'B', self.ekran) for x in range((y + 1) % 2, self.KOLUMNY, 2)] for y in range(6, 10)]
        self.pola_bialych = list(chain.from_iterable(self.pola_biale))
        self.wszystkie_pionki = self.pola_bialych.copy()
        self.wszystkie_pionki.extend(self.pola_czarnych)
        self.wszystkie_pionki.extend(self.pola_pustych)
        self.lista_miejsc_bicia = []
        self.wsp_puste = []
        self.wsp_biale = []
        self.wsp_czarne = []
        self.lista_ruchow = [[]]
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
    def zmien_gracza(self, gracz):
        if gracz == 1:
            gracz = 2
        elif gracz == 2:
            gracz = 1
    def sasiednie(self, pionek):
        self.lista_ruchow.clear()
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
        print(self.lista_ruchow)

    def ruch(self, pionek):
        s=s
#        if self.lista_ruchow

    def czy_jest_bicie_pionkiem(self, pionek):
        self.lista_pionow_do_bicia.clear()
        self.lista_miejsc_bicia.clear()
        if pionek.kolor == 'B':
            if pionek.wsp_x + 2 < 10 and pionek.wsp_y - 2 > 0:
                listunia = self.pola_czarnych.copy()
                for pioneczek in listunia:
                    if pioneczek.wsp_x == pionek.wsp_x + 1 and pioneczek.wsp_y == pionek.wsp_y - 1:
                        for j in self.pola_pustych:
                            if j.wsp_x == pionek.wsp_x + 2 and j.wsp_y == pionek.wsp_y -2:
                                self.lista_pionow_do_bicia.append((pionek.wsp_x + 1, pionek.wsp_y - 1))
                                self.lista_miejsc_bicia.append((pionek.wsp_x +2, pionek.wsp_y -2))
                               # print(pionek.wsp_x, pionek.wsp_y)
                                #print("LISTA: ", self.lista_pionow_do_bicia)
            if pionek.wsp_x - 2 >= 0 and pionek.wsp_y - 2 > 0:
                listunia = self.pola_czarnych.copy()
                for pioneczek in listunia:
                    if pioneczek.wsp_x == pionek.wsp_x - 1 and pioneczek.wsp_y == pionek.wsp_y - 1:
                        for j in self.pola_pustych:
                            if j.wsp_x == pionek.wsp_x - 2 and j.wsp_y == pionek.wsp_y -2:
                                self.lista_pionow_do_bicia.append((pionek.wsp_x -1, pionek.wsp_y - 1))
                                self.lista_miejsc_bicia.append((pionek.wsp_x - 2, pionek.wsp_y - 2))
                                #print(pionek.wsp_x, pionek.wsp_y)
                               # print("LISTA: ", self.lista_pionow_do_bicia)
        if pionek.kolor == 'C':
            if pionek.wsp_x + 2 < self.WIERSZE and pionek.wsp_y + 2 < self.KOLUMNY:
                listunia = self.pola_bialych.copy()
                for pioneczek in listunia:
                    if pioneczek.wsp_x == pionek.wsp_x + 1 and pioneczek.wsp_y == pionek.wsp_y + 1:
                        for j in self.pola_pustych:
                            if j.wsp_x == pionek.wsp_x + 2 and j.wsp_y == pionek.wsp_y + 2:
                                self.lista_pionow_do_bicia.append((pionek.wsp_x + 1, pionek.wsp_y + 1))
                                self.lista_miejsc_bicia.append((pionek.wsp_x + 2, pionek.wsp_y + 2))
                               # print("LISTA: ", self.lista_pionow_do_bicia)
            if pionek.wsp_x - 2 >= 0 and pionek.wsp_y + 2 < self.KOLUMNY:
                listunia = self.pola_bialych.copy()
                for pioneczek in listunia:
                    if pioneczek.wsp_x == pionek.wsp_x - 1 and pioneczek.wsp_y == pionek.wsp_y + 1:
                        for j in self.pola_pustych:
                            if j.wsp_x == pionek.wsp_x - 2 and j.wsp_y == pionek.wsp_y + 2:
                                self.lista_pionow_do_bicia.append((pionek.wsp_x - 1, pionek.wsp_y + 1))
                                self.lista_miejsc_bicia.append((pionek.wsp_x - 2, pionek.wsp_y + 2))
                                #print("LISTA: ", self.lista_pionow_do_bicia)

    def rusz_pionkiem(self, pionek, wsp_x, wsp_y):
        for x in self.pola_pustych:
            if x.wsp_x == wsp_x and x.wsp_y == wsp_y:
                temp1 = pionek.wsp_x
                temp2 = pionek.wsp_y
                pionek.wsp_x = x.wsp_x
                pionek.wsp_y = x.wsp_y
                x.wsp_x = temp1
                x.wsp_y = temp2

    def wybierz_pionek(self, gracz, wsp_x, wsp_y):
        if gracz == 1:
            for pionek in self.pola_bialych:
                if pionek.wsp_x == wsp_x and pionek.wsp_y == wsp_y:
                    zwroc_pionka = pionek
        if gracz == 2:
            for pionek in self.pola_czarnych:
                if pionek.wsp_x == wsp_x and pionek.wsp_y == wsp_y:
                    zwroc_pionka = pionek
        return zwroc_pionka

    def czy_mozna_ruszyc(self, gracz, wsp_x, wsp_y):
        s = 0
        if gracz == 1:
            for pionek in self.pola_bialych:
                if pionek.wsp_x == wsp_x and pionek.wsp_y == wsp_y:
                    self.sasiednie(pionek)
                    if self.lista_ruchow != []:
                        s = 1
                    self.czy_jest_bicie_pionkiem(pionek)
                    if self.czy_mozna_bic(pionek) == True:
                        s = 1
        if gracz == 2:
            for pionek in self.pola_czarnych:
                if pionek.wsp_x == wsp_x and pionek.wsp_y == wsp_y:
                    self.sasiednie(pionek)
                    if self.lista_ruchow != []:
                        s = 1
                    self.czy_jest_bicie_pionkiem(pionek)
                    if self.czy_mozna_bic(pionek) == True:
                        s = 1

        if s == 1:
            return True
        else:
            return False
    def czy_mozna_postawic(self, pionek, wsp_x, wsp_y):
        s = 0
        for x in self.lista_ruchow:
                if x[0] == wsp_x and x[1] == wsp_y:
                    s = 1
        if s == 1:
            return True
        else:
            return False

    def dodaj_bialy_pionek(self, pionek):
        self.pola_bialych.append(Pionek(pionek.wsp_x, pionek.wsp_y, 'B', self.ekran))
        wymiar_pola = self.szerokosc / 10
        self.ekran.blit(BIALY, (pionek.wsp_x * wymiar_pola - 360, pionek.wsp_y * wymiar_pola - 360))
        #print(self.pola_bialych)

    def dodaj_czarny_pionek(self, pionek):
        self.pola_czarnych.append((pionek.wsp_x, pionek.wsp_y, 'C', self.ekran))
        wymiar_pola = self.szerokosc / 10
        self.ekran.blit(CZARNY, (pionek.wsp_x * wymiar_pola - 360, pionek.wsp_y * wymiar_pola - 360))
      #  print(self.pola_bialych)
       # for i in self.pola_pustych:
         #   if i.wsp_x == pionek.wsp_x and i.wsp_y == pionek.wsp_y:
             #   self.pola_pustych.pop(i)

       # print("Lista ruchow:  ", self.lista_ruchow)
        #print(pionek.wsp_x)
        #print(pionek.wsp_y)
        #print(self.pola_pustych[6].wsp_x)
       #print(self.pola_pustych[6].wsp_y)
    def czy_mozna_bic(self, pionek):

        if self.lista_pionow_do_bicia != []:
            return True
        else:
            return False
    def bicie_pionkiem(self, gracz, pionek, wsp_x, wsp_y):
        s = 0
        if gracz == 1:
            for x in self.lista_miejsc_bicia:
                if wsp_x == x[0] and wsp_y == x[1]:
                    for y in self.pola_czarnych:
                        if y.wsp_x == self.lista_pionow_do_bicia[s][0]:
                            if y.wsp_y == self.lista_pionow_do_bicia[s][1]:
                                y.kolor = '-'
                                self.pola_pustych.append(y)
                                self.pola_czarnych.remove(y)
                                for z in self.pola_pustych:
                                    if z.wsp_x == wsp_x and z.wsp_y == wsp_y:
                                        temp1 = pionek.wsp_x
                                        temp2 = pionek.wsp_y
                                        pionek.wsp_x = z.wsp_x
                                        pionek.wsp_y = z.wsp_y
                                        z.wsp_x = temp1
                                        z.wsp_y = temp2
                else:
                    s += 1
        if gracz == 2:
            for x in self.lista_miejsc_bicia:
                if wsp_x == x[0] and wsp_y == x[1]:
                    for y in self.pola_bialych:
                        if y.wsp_x == self.lista_pionow_do_bicia[s][0]:
                            if y.wsp_y == self.lista_pionow_do_bicia[s][1]:
                                y.kolor = '-'
                                self.pola_pustych.append(y)
                                self.pola_bialych.remove(y)
                                for z in self.pola_pustych:
                                    if z.wsp_x == wsp_x and z.wsp_y == wsp_y:
                                        temp1 = pionek.wsp_x
                                        temp2 = pionek.wsp_y
                                        pionek.wsp_x = z.wsp_x
                                        pionek.wsp_y = z.wsp_y
                                        z.wsp_x = temp1
                                        z.wsp_y = temp2
                else:
                    s+= 1
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
        lista_pionkow.extend(self.pola_pustych)
      #  print(self.pola_czarnych)
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
        pionek.wsp_x -= 1
        pionek.wsp_y -= 1
        if pionek.kolor == 'C':
            self.ekran.blit(CZARNY, (pionek.wsp_x * wymiar_pola - 360, pionek.wsp_y * wymiar_pola - 360))
            pygame.draw.rect(self.ekran, self.CZARNE_POLE,
                             pygame.Rect((pionek.wsp_x+1) * wymiar_pola, (pionek.wsp_y+1) * wymiar_pola, self.szerokosc / 10,
                                         self.wysokosc / 10))
        elif pionek.kolor == 'B':
            self.ekran.blit(BIALY, (pionek.wsp_x * wymiar_pola - 360 , pionek.wsp_y * wymiar_pola - 360 ))
            pygame.draw.rect(self.ekran, self.CZARNE_POLE,
                             pygame.Rect((pionek.wsp_x+1) * wymiar_pola, (pionek.wsp_y+1)*wymiar_pola, self.szerokosc / 10, self.wysokosc / 10))
        czcionka = pygame.font.SysFont("timesnewroman", 20, bold = True)
        #czcionka_kolor= BLACK_COLOR
    def zbicie_bialego_piona(self, pionek):
        pionek.kolor = '-'
    def ruchy(self, pionek):
        if pionek.wsp_x + 1 and pionek.wsp_y + 1:
            pionek.wsp_x += 1
            pionek.wsp_y += 1
    def rysuj(self,pionek):
        wymiar_pola = self.szerokosc / 10
        self.ekran.blit(CZARNY, (pionek.wsp_x * wymiar_pola - 360, pionek.wsp_y * wymiar_pola - 360))
    def czy_krolowa(self, gracz, pionek, damka):
        if gracz == 1:
            if pionek.wsp_y == 0:
                if damka == False:
                    damka = True
        if gracz == 2:
            if pionek.wsp_y == 9:
                if damka == False:
                    damka = True
    def draw_background(self):
        '''
        Draws background for the board
        '''
