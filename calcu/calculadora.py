import tkinter as tk

def click_boton(valor):
    entrada_actual = str(entrada.get())
    entrada.delete(0, tk.END)
    entrada.insert(0, entrada_actual + valor)

def borrar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str("que bruto eres"))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora")

# Crear campo de entrada
entrada = tk.Entry(ventana, width=20, font=("Arial", 24), bd=5, relief=tk.RIDGE, justify='right')
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botones
botones = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (texto, fila, columna) in botones:
    if texto == "=":
        boton = tk.Button(ventana, text=texto, width=5, height=2, font=("Arial", 18),
                          command=calcular)
    else:
        boton = tk.Button(ventana, text=texto, width=5, height=2, font=("Arial", 18),
                          command=lambda t=texto: click_boton(t))
    boton.grid(row=fila, column=columna, padx=5, pady=5)

# Botón borrar
boton_borrar = tk.Button(ventana, text="C", width=5, height=2, font=("Arial", 18),
                         command=borrar)
boton_borrar.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="we")

ventana.mainloop()
