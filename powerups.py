from tkinter import *

import random

_COLORS = [None, 'deep sky blue', 'forest green', 'purple1']
_NAMES = [None, 'Częsty', 'Rzadki', 'Epicki']
_IMAGES = {x:PhotoImage(file=f'powerups/{x}.png') for x in ['predkosc', 'maxCooldown', 'maxWytrzymalosc', 'zadajeObrazen', 'odlegloscStrzalu']}

def askAndAdd(gracz):
    tk = Tk()
    tk.overrideredirect(1)
    wybor = StringVar(tk)
    l = Label(tk, text='Wybierz ulepszenie')
    l.grid()
    fr = Frame(tk)
    fr.grid()
    for i in range(3):
        attr = random.choice(['predkosc', 'maxCooldown', 'maxWytrzymalosc', 'zadajeObrazen', 'odlegloscStrzalu'])
        level = random.randint(1, 3)
        b = Button(tk, text=_NAMES[level], image=_IMAGES[attr], bg=_COLORS[level], command=lambda attr=attr, level=level: wybor.set(f'{attr} {level}'))
        b.grid(row=0, column=i)
    tk.wait_variable(wybor)
    attr, level = wybor.get().split()
    level = int(level)
    if attr == 'maxCooldown':
        level *= -30
    setattr(gracz, attr, getattr(gracz, attr) + level)