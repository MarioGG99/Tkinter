# Importamos tkinter y math
import tkinter as tk
import math

# Creamos la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x400")
ventana.rowconfigure(0, weight=1)
ventana.columnconfigure(0, weight=1)
# Creamos una variable para almacenar la expresión matemática
expresion = ""

# Creamos una función para actualizar la expresión en la pantalla
def presionar(num):
    global expresion
    expresion = expresion + str(num)
    pantalla.set(expresion)

# Creamos una función para evaluar la expresión y mostrar el resultado
def igual():
    global expresion
    try:
        resultado = str(eval(expresion))
        pantalla.set(resultado)
        expresion = ""
    except:
        pantalla.set("Error")
        expresion = ""

# Creamos una función para borrar la pantalla y la expresión
def borrar():
    global expresion
    expresion = ""
    pantalla.set("")

# Creamos un objeto StringVar para mostrar la pantalla de la calculadora
pantalla = tk.StringVar()

# Creamos un campo de texto para mostrar la pantalla de la calculadora
campo_texto = tk.Entry(ventana, textvariable=pantalla)
campo_texto.grid(columnspan=4, ipadx=70)

# Creamos los botones numéricos y los colocamos en la ventana usando grid
boton1 = tk.Button(ventana, text=" 1 ", command=lambda: presionar(1), height=2, width=7)
boton1.grid(row=2, column=0)

boton2 = tk.Button(ventana, text=" 2 ", command=lambda: presionar(2), height=2, width=7)
boton2.grid(row=2, column=1)

boton3 = tk.Button(ventana, text=" 3 ", command=lambda: presionar(3), height=2, width=7)
boton3.grid(row=2, column=2)

boton4 = tk.Button(ventana, text=" 4 ", command=lambda: presionar(4), height=2, width=7)
boton4.grid(row=3, column=0)

boton5 = tk.Button(ventana, text=" 5 ", command=lambda: presionar(5), height=2, width=7)
boton5.grid(row=3, column=1)

boton6 = tk.Button(ventana, text=" 6 ", command=lambda: presionar(6), height=2,
width=7) 
boton6.grid(row=3,column=2) 
boton7 =tk.Button(ventana,text=" 7 ",command=lambda:presionar(7),height=2,width=7)
boton7.grid(row=4,column=0) 
boton8 =tk.Button(ventana,text=" 8 ",command=lambda:presionar(8),height=2,width=7)
boton8.grid(row=4,column=1)
boton9 =tk.Button(ventana,text=" 9 ",command=lambda:presionar(9),height=2,width=7)
boton9.grid(row=4, column=2)
boton0 = tk.Button(ventana, text=" 0 ", command=lambda: presionar(0), height=1, width=7)
boton0.grid(row=5, column=0)

# Creamos los botones de operaciones y los colocamos en la ventana usando grid
boton_suma = tk.Button(ventana, text=" + ", command=lambda: presionar("+"), height=1,width=7)
boton_suma.grid(row=2,column=3) 
boton_resta =tk.Button(ventana,text=" - ",command=lambda:presionar("-"),height=1,width=7)

boton_resta.grid(row=3,column=3)
boton_multi =tk.Button(ventana,text=" * ",command=lambda:presionar("*"),height=1,width=7)
boton_multi.grid(row=4,column=3) 
boton_divi =tk.Button(ventana,text=" / ",command=lambda:presionar("/"),height=1,width=7)

boton_divi.grid(row=5, column=3)

boton_igual = tk.Button(ventana, text=" = ", command=igual, height=1, width=7)
boton_igual.grid(row=5, column=2)

boton_borrar = tk.Button(ventana, text="C", command=borrar, height=1,width=7) 
boton_borrar.grid(row=6,column=0)
boton_pi =tk.Button(ventana,text="π",command=lambda:presionar(math.pi),height=1,width=7)
boton_pi.grid(row=6,column=1)
boton_e =tk.Button(ventana,text="e",command=lambda:presionar(math.e),height=1,width=7)
boton_e.grid(row=5,column=1)

boton_punto =tk.Button(ventana,text=".",command=lambda:presionar("."),height=1,width=7)
boton_punto.grid(row=6,column=2)

boton_log =tk.Button(ventana,text="log",command=lambda:presionar("log("),height=1,width=7)
boton_log.grid(row=7,column=3)
boton_parentesis =tk.Button(ventana,text="(",command=lambda:presionar("("),height=1,width=7)
boton_parentesis.grid(row=6, column=3)
boton_parentesiss =tk.Button(ventana,text=")",command=lambda:presionar(")"),height=1,width=7)
boton_parentesiss.grid(row=6, column=4)

ventana.bind("1", lambda event: presionar(1)) 
ventana.bind("2", lambda event: presionar(2)) 
ventana.bind("3", lambda event: presionar(3)) 
ventana.bind("4", lambda event: presionar(4)) 
ventana.bind("5", lambda event: presionar(5)) 
ventana.bind("6", lambda event: presionar(6)) 
ventana.bind("7", lambda event: presionar(7)) 
ventana.bind("8", lambda event: presionar(8)) 
ventana.bind("9", lambda event: presionar(9)) 
ventana.bind("0", lambda event: presionar(0)) 
ventana.bind("+", lambda event: presionar("+"))
ventana.bind("-", lambda event: presionar("-"))
ventana.bind("/", lambda event: presionar("/"))
ventana.bind(".", lambda event: presionar("."))
ventana.bind("*", lambda event: presionar("*"))
ventana.bind("e", lambda event: presionar(math.e))
ventana.bind("p", lambda event: presionar(math.pi))
ventana.bind("<Alt-8>", lambda event: presionar("("))
ventana.bind("<Alt-9>", lambda event: presionar(")"))
ventana.bind("<Return>", lambda event: igual())
ventana.bind("<BackSpace>", lambda event: borrar())

# Iniciamos el bucle principal de la ventana
ventana.mainloop()