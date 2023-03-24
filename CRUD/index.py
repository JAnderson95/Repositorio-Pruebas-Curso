#Libreria
from tkinter import ttk
from tkinter import *
# Modulo de conexion
import sqlite3 

#clase que tendra todos los metodos de las ventanas
class product:
    def __init__(self,window):
        self.wind=window
        self.wind.title('Products app')
        



if __name__ == '__main__':
    window = Tk()
    application=product(window)
    window.mainloop()
    



