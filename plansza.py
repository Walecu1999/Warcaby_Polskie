import pygame

class Plansza(object):
    CZARNY = 1
    BIALY = 0
    NOTDONE = -1
    KOLUMNY = 10
    WIERSZE = 10
    Biale_pole = (0, 0, 0)
    Czarne_pole = (205, 205, 205)
    def __init__(self,wysokosc,szerokosc,ekran):
        self.ekran=ekran
        self.wysokosc=wysokosc
        self.szerokosc=szerokosc
        self.pola_bialych = []
        self.pola_czarnych = []
        self.gracze=['C','B'];
        self.tablica = [['-', 'C', '-', 'C', '-', 'C', '-', 'C', '-','C'],
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
        k=0
        x, y = 0,0
        a=0
        for i in range(0,self.WIERSZE):
            for j in range(0,self.KOLUMNY):
                if (k+a)%2:
                    k=k+1
                    pygame.draw.rect(self.ekran,self.Czarne_pole, pygame.Rect(x,y,self.szerokosc/10,self.wysokosc/10))
                else:
                    k=k+1
                    pygame.draw.rect(self.ekran,self.Biale_pole, pygame.Rect(x, y, self.szerokosc / 10, self.wysokosc / 10))
                x+=self.szerokosc/10
            y+=self.wysokosc/10
            x = 0
            a+=1
        czcionka= pygame.font.SysFont("timesnewroman",20,bold = True)
        #czcionka_kolor= BLACK_COLOR

    def draw_background(self):
        '''
        Draws background for the board
        '''
        #font= pygame.font.SysFont("timesnewroman",20,bold = True)
        #pygame.draw.rect(self.game.screen, LIGHT_GREY_COLOR, pygame.Rect(0, 0, self.width, self.height))