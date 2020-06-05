
class Pionek:
    def __init__(self, wsp_x, wsp_y, kolor, ekran):
        self.wsp_x = wsp_x
        self.wsp_y = wsp_y
        self.kolor = kolor
        self.ekran = ekran

    def ruchy(self):
        temp = '-'
        if Pionek(wsp_x, wsp_y).kolor == 'B':
            if Pionek(wsp_x+1, wsp_y+1).kolor == '-':
                temp = Pionek(wsp_x+1, wsp_y+1).kolor
                Pionek(wsp_x + 1, wsp_y + 1).kolor = 'B'
                Pionek(wsp_x, wsp_y).kolor = temp
    def bicia(self):
        pass
        # def ruchy_ziomeczkow(self):




   # def zbity(self):

