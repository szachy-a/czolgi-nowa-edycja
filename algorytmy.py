import math
import pygame

def obliczDystans(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


def utworzGraf(maskaPoziomu: pygame.mask.Mask):
    wid, hei = maskaPoziomu.get_size()
    cellMatrix = [[0 for x in range(30)] for y in range(30)]
    cellWid = wid // 30
    cellHei = hei // 30
    for i in range(hei):
        for j in range(wid):
            bit = maskaPoziomu.get_at((j,i))
            if bit == 1:
                cellMatrix[i//cellHei][j//cellWid] = 1


def znajdzSciezke(x1, y1, x2, y2, poziom):
    inf = float("inf")
    for x in poziom.keys():
        poziom[x]["g"] = inf
        poziom[x]["f"] = inf
    poziom[(x1,y1)]["g"] = 0
    poziom[(x1,y1)]["f"] = math.sqrt(((x1-x2)**2 + (y1-y2)**2) * 2)
    current = None
    prq = {(x1,y1)}
    pnd = {}
    while prq != {}:
        current = min(prq, key=lambda x:poziom[x]["f"])
        if current == (x2,y2):
            return pnd, current
        prq.remove(current)
        for x in poziom[current]["connections"]:
            tempG = poziom[current]["g"] + 1
            if tempG < poziom[x]["g"]:
                pnd[x] = current
                poziom[x]["g"] = tempG
                poziom[x]["f"] = poziom[x]["g"] + math.sqrt(((x[0]-(x2,y2)[0])**2 + (x[1]-(x2,y2)[1])**2) * 2)
                if x not in prq:
                    prq.add(x)
    #raise RuntimeError("A* algorithm failed")
    return {}, (x1,y1)