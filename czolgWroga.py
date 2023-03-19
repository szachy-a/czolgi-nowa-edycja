import pygame
import czolg
import abc
import algorytmy
import math
import czolgGracza as cg
import pocisk

class CzolgWroga(czolg.Czolg):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.maxWytrzymalosc = 3
        self.odlegloscStrzalu = 1
        self.zadajeObrazen = 1
        self.hp = self.maxWytrzymalosc
    def podejmijDecyzje(self, wszystko: pygame.sprite.Group, szerokoscEkranu, wysokoscEkranu, graf):
        for x in wszystko.sprites():
            if type(x) == cg.CzolgGracza:
                czolgGracza = x
                break
        sciezka = algorytmy.znajdzSciezke(self.x, self.y, czolgGracza.x, czolgGracza.y, graf, szerokoscEkranu, wysokoscEkranu)
        if sciezka == "sciana":
            for x in graf.keys():
                if algorytmy.obliczDystans(self.x, self.y, x[0], x[1]) <= math.sqrt((szerokoscEkranu//40)**2 + (wysokoscEkranu//40)**2):
                    sciezka = [(x[0], x[1])]
                    break
        elif sciezka == "graczNiedostepny":
            for x in graf.keys():
                if algorytmy.obliczDystans(czolgGracza.x, czolgGracza.y, x[0], x[1]) <= math.sqrt((szerokoscEkranu//40)**2 + (wysokoscEkranu//40)**2):
                    sciezka = algorytmy.znajdzSciezke(self.x, self.y, x[0], x[1], graf, szerokoscEkranu, wysokoscEkranu)
                    break
        if algorytmy.obliczDystans(self.x, self.y, czolgGracza.x, czolgGracza.y) >= self.odlegloscStrzalu * 10:
            kat = algorytmy.obliczKat(self.x,self.y,sciezka[1][0], sciezka[1][1])
            if self.kat <= kat-3:
                return czolg.CZOLG_W_LEWO
            elif self.kat >= kat+3:
                return czolg.CZOLG_W_PRAWO
            else:
                if algorytmy.obliczDystans(self.x, self.y, sciezka[1][0], sciezka[1][1]) >= 3:
                    return czolg.CZOLG_W_PRZOD
        else:
            kat = algorytmy.obliczKat(self.x,self.y,sciezka[0][0], sciezka[0][1])
            if self.kat <= kat-3:
                return czolg.CZOLG_W_LEWO
            elif self.kat >= kat+3:
                return czolg.CZOLG_W_PRAWO
            else:
                return czolg.STRZAL
    def update(self, wszystko, szerokoscEkranu, wysokoscEkranu, graf):
        self.ruch(wszystko, szerokoscEkranu, wysokoscEkranu, graf)
    def ruch(self, wszystko, szerokoscEkranu, wysokoscEkranu, graf):
        match self.podejmijDecyzje(wszystko, szerokoscEkranu, wysokoscEkranu, graf):
            case czolg.CZOLG_W_LEWO:
                self.kat += 3
                if self.kat >= 360:
                    self.kat -= 360
                self.surf = pygame.transform.rotate(self.orgSurf, self.kat)
                self.rect = self.surf.get_rect(center=self.rect.center)
                self.wektor = czolg.WEKTORY[self.kat]
                self.mask = pygame.mask.from_surface(self.surf)
            case czolg.CZOLG_W_PRAWO:
                self.kat -= 3
                if self.kat <= -360:
                    self.kat += 360
                self.surf = pygame.transform.rotate(self.orgSurf, self.kat)
                self.rect = self.surf.get_rect(center=self.rect.center)
                self.wektor = czolg.WEKTORY[self.kat]
                self.mask = pygame.mask.from_surface(self.surf)
            case czolg.CZOLG_W_PRZOD:
                self.rect.x += self.wektor.x * 3
                self.rect.y += self.wektor.y * 3
            case czolg.CZOLG_W_TYL:
                self.rect.x -= self.wektor.x * 3
                self.rect.y -= self.wektor.y * 3
            case czolg.STRZAL:
                wszystko.add(pocisk.Pocisk(*self.rect.center, self.wektor, self.odlegloscStrzalu, self.zadajeObrazen))


