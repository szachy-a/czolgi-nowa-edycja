import pygame
import czolg
import abc
import algorytmy
import math
import czolgGracza as cg

import __main__

class CzolgWroga(czolg.Czolg):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.maxWytrzymalosc = 3
        self.odlegloscStrzalu = 1
        self.zadajeObrazen = 1
        self.hp = self.maxWytrzymalosc
    def podejmijDecyzje(self):
        graf = __main__.graf
        wszystko = __main__.wszystko
        szerokoscEkranu = __main__.screen.get_width()
        wysokoscEkranu = __main__.screen.get_height()
        for x in wszystko:
            if type(x) == cg.CzolgGracza:
                czolgGracza = x
                break
        sciezka = algorytmy.znajdzSciezke(self.rect.centerx, self.rect.centery, czolgGracza.rect.centerx, czolgGracza.rect.centery, graf, szerokoscEkranu, wysokoscEkranu)
        if sciezka == "sciana":
            for x in graf.keys():
                if algorytmy.obliczDystans(self.rect.centerx, self.rect.centery, x[0], x[1]) <= math.sqrt((szerokoscEkranu//40)**2 + (wysokoscEkranu//40)**2):
                    sciezka = [0, (x[0], x[1])]
                    break
        elif sciezka == "graczNiedostepny":
            for x in graf.keys():
                if algorytmy.obliczDystans(czolgGracza.rect.centerx, czolgGracza.rect.centery, x[0], x[1]) <= math.sqrt((szerokoscEkranu//40)**2 + (wysokoscEkranu//40)**2):
                    sciezka = algorytmy.znajdzSciezke(self.rect.centerx, self.rect.centery, x[0], x[1], graf, szerokoscEkranu, wysokoscEkranu)
                    break
        if algorytmy.obliczDystans(self.rect.centerx, self.rect.centery, czolgGracza.rect.centerx, czolgGracza.rect.centery) >= self.odlegloscStrzalu * 10:
            kat = algorytmy.obliczKat(self.rect.centerx,self.rect.centery,sciezka[1][0], sciezka[1][1])
            if self.kat <= kat-3:
                return czolg.CZOLG_W_LEWO
            elif self.kat >= kat+3:
                return czolg.CZOLG_W_PRAWO
            else:
                if algorytmy.obliczDystans(self.rect.centerx, self.rect.centery, sciezka[1][0], sciezka[1][1]) >= 3:
                    return czolg.CZOLG_W_PRZOD
        else:
            kat = algorytmy.obliczKat(self.rect.centerx,self.rect.centery,sciezka[0][0], sciezka[0][1])
            if self.kat <= kat-3:
                return czolg.CZOLG_W_LEWO
            elif self.kat >= kat+3:
                return czolg.CZOLG_W_PRAWO
            else:
                return czolg.STRZAL