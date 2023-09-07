def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

resultado1 = suma(1, 2)
resultado2 = resta(2, 1)

import tkinter as tk

def mostrar_mensaje():
    etiqueta.config(text="El resultado de su suma: " + str(resultado1))

def center_window(window, width, height):
    # Obtiene el ancho y alto de la pantalla
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calcula las coordenadas X e Y para centrar la ventana
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Ubica la ventana en el centro de la pantalla
    window.geometry(f"{width}x{height}+{x}+{y}")    

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Sumas y restas de primario")
width = 800
height = 200

# Centrar la ventana
center_window(ventana, width, height)


# Crear etiqueta
etiqueta = tk.Label(ventana, text="¡Bienvenido a tu aplicación de escritorio!", font=("Arial", 16))
etiqueta.pack(pady=20)

# Crear botón
boton = tk.Button(ventana, text="Haz clic aquí", command=mostrar_mensaje)
boton.pack()

# Iniciar el bucle del evento principal
ventana.mainloop()