import math
import pygame

def obliczDystans(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


def utworzGraf(maska: pygame.mask.Mask):
    wid, hei = maska.get_size()
    cellMatrix = [[0 for x in range(40)] for y in range(40)]
    cellWid = wid // 40
    cellHei = hei // 40
    for i in range(hei):
        for j in range(wid):
            bit = maska.get_at((j,i))
            if bit == 1:
                cellMatrix[i//cellHei][j//cellWid] = 1
    graph = {}
    for y, row in enumerate(cellMatrix):
        for x, cell in enumerate(row):
            graph[(x,y)] = {}
            graph[(x,y)]["connections"] = []
            if cell == 0:
                if x > 0 and row[x-1] == 0:
                    graph[(x,y)]["connections"].append((x - 1, y))
                if y > 0 and cellMatrix[y-1][x] == 0:
                    graph[(x,y)]["connections"].append((x, y - 1))
                if x <= len(row) - 1 and row[x+1] == 0:
                    graph[(x,y)]["connections"].append((x + 1, y))
                if y <= len(cellMatrix) and cellMatrix[y+1][x] == 0:
                    graph[(x,y)]["connections"].append((x, y + 1))
    return graph

def znajdzSciezke(x1, y1, x2, y2, graf, szerokoscEkranu, wysokoscEkranu):
    x1 = x1//(szerokoscEkranu//30)
    inf = float("inf")
    for x in graf.keys():
        graf[x]["g"] = inf
        graf[x]["f"] = inf
    graf[(x1,y1)]["g"] = 0
    graf[(x1,y1)]["f"] = math.sqrt(((x1-x2)**2 + (y1-y2)**2) * 2)
    current = None
    prq = {(x1,y1)}
    pnd = {}
    while prq != {}:
        current = min(prq, key=lambda x:graf[x]["f"])
        if current == (x2,y2):
            return pnd, current
        prq.remove(current)
        for x in graf[current]["connections"]:
            tempG = graf[current]["g"] + 1
            if tempG < graf[x]["g"]:
                pnd[x] = current
                graf[x]["g"] = tempG
                graf[x]["f"] = graf[x]["g"] + math.sqrt(((x[0]-(x2,y2)[0])**2 + (x[1]-(x2,y2)[1])**2) * 2)
                if x not in prq:
                    prq.add(x)
    #raise RuntimeError("A* algorithm failed")
    return {}, (x1,y1)