import pygame

class Plansza(object):
    CZARNY = 1
    BIALY = 0
    NOTDONE = -1
    KOLUMNY = 10
    WIERSZE = 10
    BIALE_POLE = (255, 255, 255)
    CZARNE_POLE = (100, 99, 45)
    def __init__(self, wysokosc, szerokosc, ekran):
        self.ekran = ekran
        self.wysokosc = wysokosc
        self.szerokosc = szerokosc
        self.pola_bialych = []
        self.pola_czarnych = []
        self.gracze = ['C', 'B'];
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


        for i in range(szerokosc):
            self.pola_czarnych.append((i, (i + 1) % 2))
            self.pola_bialych.append((i, wysokosc - (i % 2) - 1))
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
        #czcionka = pygame.font.SysFont("timesnewroman", 20, bold = True)
        #czcionka_kolor= BLACK_COLOR

    def draw_background(self):
        '''
        Draws background for the board
        '''
