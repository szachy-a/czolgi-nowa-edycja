import pygame
import czolg
import abc
import algorytmy

class CzolgWroga(czolg.Czolg):
    def __init__(self, x, y):
        super.__init__(x,y)
        self.typAi = "zbalansowany"
    def znajdzSciezke(self, x, y):
        pass
    def podejmijDecyzje(self, czolgGracza):
        match self.typAi:
            case "zbalansowany":
                pass
            case "agresywny":
                pass
            case "snajper":
                pass
            case _:
                raise NotImplementedError(f"Nieznany typ ai: '{self.typAi}'")
