# IMPORTAMOS LIBRERIAS
from tkinter import ttk
from tkinter import *
#para conectarnos al modulo de SQLITE3
import sqlite3


 # Creamos la clase para administrar los productos
class product:
    def __init__(self,window):
        self.wind = window # aca almacenamos la ventana como propiedad
        self.wind.title(' Aplicacion de productos ') # Acá  le damos el titulo a nuestra aplicacion
        
        # Creamos un frame que sera un contenedor
        frame=LabelFrame (self.wind,text= 'Registra un nuevo producto') # creamos el frame, lo enviamos a la ventana, le damos un titulo y despues lo guardamos en una variable para utilizarla despues
        frame.grid(row= 0, column=0, columnspan=3, pady= 10) # utilizando la variable frame que se creo anteriormente, empezamos a ubicarlo por me dio de la grilla (grid), le damos valores de posicion y de espaciado
        
        # Input Nombre
        Label(frame, text='Nombre: ').grid( row=1, column=0) #Utilizamos el metodo Label, elcual nos permite crear una etiqueta la cual tendra un titulo nombre y le damos valores de posicion
        self.name=Entry(frame) # Acá creamos el cuadro de texto donde el usuario itroducira la informacion guardamos  la caja de texto en una variable (atributo) para posicionarla y utilizarla ya que tendra datos de usuario
        self.name.focus() # esto para cuando entremos a la aplicaicon, el cursor pardee en la caja de nombre
        self.name.grid(row=1, column=1) # Acá la hubicamos al lado de la etiqueta
        
        # Input precio  Acá repetimos el paso de arriba
        Label(frame, text = ' Precio: ').grid(row=2, column=0)
        self.price = Entry(frame)
        self.price.grid(row=2, column=1)
        # crando boton agregar producto
        
        ttk.Button(frame,text =' Guardar producto').grid(row=3, columnspan=2, sticky = W+E)# Creamos el botón con  ttk.Button de tkinter, lo guardamos en frame, le damos un titulo y despues le damos una posicion y un  tamaño
        
         
# creamos el comprobador de arranque        
if __name__ == '__main__':
    window= Tk()  # Creamos variable window en la cual guardaremos Tk que es el inicializador y la raiz principal para manejar todos los archivos
    application=product(window) #   para tener el codigo ordenado  le pasaremos la ventana a la clase product como un atributo (parametro) y lo guardaremos en una variable (application) por si devuelve algun dato
    window.mainloop() # aca ejecutamos la ventana pra que nos muestre  la pequeña ventana de la aplicacion
         