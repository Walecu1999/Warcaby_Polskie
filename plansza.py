import pygame
from Pionek import Pionek

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
        self.pola_puste =  [[Pionek(x, y, '-', self.ekran) for x in range((y + 1) % 2, 10, 2)] for y in range(4, 6)]
        self.pola_czarnych = [[Pionek(x, y, 'C', self.ekran) for x in range((y + 1) % 2, 10, 2)] for y in range(4)]
        self.pola_bialych = [[Pionek(x, y, 'B', self.ekran) for x in range((y + 1) % 2, 10, 2)] for y in range(6, 10)]
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
      #  def ruchy(pionek):
           # ruch[]
           # if tablica


       # for i in range(szerokosc):
         #   self.pola_czarnych.append((i, (i + 1) % 2))
           # self.pola_bialych.append((i, wysokosc - (i % 2) - 1))
        self.status = [[' ' for i in range(self.szerokosc)] for x in range(self.wysokosc)]
        self.wygrana = self.NOTDONE


    def checkboard(x):
        list = [[(j + i) % 2 for j in range(1, x + 1)] for i in range(x)]
        return list
    def tworz_plansze(self):
        tablica = [[i for kolumna in range(self.KOLUMNY)]
                   for wiersz in range(self.WIERSZE)]
        return tablica

    def rysuj(self):
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
        for lista in lista_pionkow:
            for pionek in lista:
                try:
                    if pionek.kolor == 'C':
                        self.ekran.blit(CZARNY, (pionek.wsp_x*wymiar_pola - 360, pionek.wsp_y*wymiar_pola - 360))
                    elif pionek.kolor == 'B':
                        self.ekran.blit(BIALY, (pionek.wsp_x * wymiar_pola - 360, pionek.wsp_y * wymiar_pola - 360))
                except Exception:
                    print(Exception)


        #czcionka = pygame.font.SysFont("timesnewroman", 20, bold = True)
        #czcionka_kolor= BLACK_COLOR

    def draw_background(self):
        '''
        Draws background for the board
        '''
