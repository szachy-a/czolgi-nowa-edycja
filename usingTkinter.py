from tkinter import *

import random

tk = Tk()
tk.overrideredirect(1)
tk.withdraw()

_COLORS = [None, 'deep sky blue', 'forest green', 'purple1']
_NAMES = [None, 'Częsty', 'Rzadki', 'Epicki']
_IMAGES = {x:PhotoImage(file=f'powerups/{x}.png') for x in ['predkosc', 'maxCooldown', 'maxWytrzymalosc', 'zadajeObrazen', 'odlegloscStrzalu']}

def askAndAdd(gracz):
    tk.deiconify()
    wybor = StringVar(tk)
    gfr = Frame()
    gfr.grid()
    l = Label(gfr, text='Wybierz ulepszenie')
    l.grid()
    fr = Frame(gfr)
    fr.grid()
    for i in range(3):
        attr = random.choice(['predkosc', 'maxCooldown', 'maxWytrzymalosc', 'zadajeObrazen', 'odlegloscStrzalu'])
        level = random.randint(1, 3)
        b = Button(fr, text=_NAMES[level], image=_IMAGES[attr], bg=_COLORS[level], command=lambda attr=attr, level=level: wybor.set(f'{attr} {level}'))
        b.grid(row=0, column=i)
    tk.wait_variable(wybor)
    tk.withdraw()
    attr, level = wybor.get().split()
    level = int(level)
    if attr == 'maxCooldown':
        level *= -30
    setattr(gracz, attr, getattr(gracz, attr) + level)
    gfr.destroy()

def wygrana():
    tk.overrideredirect(0)
    tk.attributes('-fullscreen', True)
    tk.deiconify()
    koniec = IntVar(tk)
    l = Label(tk, text='Ukraina wygrała z Rosją!!! Wygrałeś!!!', font=('', 40))
    l.grid()
    b = Button(tk, text='OK', font=('', 40), command=lambda: koniec.set(1))
    b.grid()
    tk.wait_variable(koniec)
    tk.withdraw()

def przegrana():
    tk.overrideredirect(0)
    tk.attributes('-fullscreen', True)
    tk.deiconify()
    koniec = IntVar(tk)
    l = Label(tk, text='Rosja zajmuje Ukrainę!!! Przegrałeś!!!', font=('', 40))
    l.grid()
    b = Button(tk, text='OK', font=('', 40), command=lambda: koniec.set(1))
    b.grid()
    tk.wait_variable(koniec)
    tk.withdraw()