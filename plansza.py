class plansza(object):
    CZARNY = 1
    BIALY = 0
    NOTDONE = -1
    def __init__(self,wysokosc,szerokosc, gracz1):
        self.wysokosc=wysokosc
        self.szerokosc=szerokosc
        self.polabialych = []
        self.polaczarnych = []
        for i in range(szerokosc)
            self.polaczarnych.append((i,(i+1)%2))
            self.polabialych.append((i,wysokosc - (i%2)-1))
        self.status = [[' ']* self.szerokosc for x in range(self.wysokosc)]
        self.wygrana = self.NOTDONE
        self.turn = gracz1