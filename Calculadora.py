#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 14:25:40 2021

@author: rodrigo
"""


import tkinter as tk
#from tkinter.constants import *
raiz = tk.Tk()
raiz.title("Calculadora")
raiz.geometry("600x600")

#creo las etiquetas de los botones que va a tener la calculadora
lista = (0 , 1 , 2,3,4,5,6,7,8,9,"+", "-" , "*" , "/" , "=" , "(" , ")", "^", "AC")
operaciones = tk.StringVar(value = "")
#operaciones.set("rtrtrt")


def botones(txt , ix ,iy):
    txt = tk.Button(raiz, text = txt, command = lambda:comando(txt.cget("text")), 
                       height = 3, width = 3)
    txt.place(x=ix,y=iy)
    

def comando(msj):    
    var = operaciones.get()
    if (msj == "="):
        operaciones.set(eval(var))
    else:
        operaciones.set(var + str(msj))
    #entrada.insert(str(msj))

boton = tk.Button(raiz , text ="hola" , command = lambda : comando ("hhh"))
boton.place(x=0 , y=0)

y = 100
x = 0
for l in lista:
    l = botones(l , x , y)
    x = x + 50
    if (x>450):
        x = 0
        y = y +50



entrada = tk.Entry(raiz ,  width = 450, font = "Bookman 20" , textvariable = operaciones)
entrada.place(x=0 , y = 50)    




tk.mainloop()


