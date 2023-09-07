import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from PIL import Image, ImageTk


def mostrar_titulos(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        h2_tags = soup.find_all('h2')

        ventana_resultados = tk.Toplevel(root)
        ventana_resultados.title("LINK DE LA PAGINA")

        texto_resultados = scrolledtext.ScrolledText(
            ventana_resultados, wrap=tk.WORD)
        texto_resultados.pack(fill=tk.BOTH, expand=True)

        texto_resultados.insert(tk.END, f'SERIAS PARA VER {url}:\n\n')
        for h2_tag in h2_tags:
            texto_resultados.insert(tk.END, h2_tag.text + '\n')

        boton_cerrar = tk.Button(
            ventana_resultados, text="Cerrar", command=ventana_resultados.destroy)
        boton_cerrar.pack()

    else:
        messagebox.showerror(
            "Error", f'La solicitud a la página {url} no fue exitosa. Código de respuesta: {response.status_code}')


root = tk.Tk()
root.title("SERIES MOUSTROSAS")
root.geometry("300x500")

imagen_fondo = Image.open("img/collage-fondo-pelicula.jpg")
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

fondo_label = tk.Label(root, image=imagen_fondo)
fondo_label.place(relwidth=1, relheight=1)

boton_terror = tk.Button(root, text="TERROR", command=lambda: mostrar_titulos(
    'https://www.fotogramas.es/series-tv-noticias/g39290691/series-miedo-netflix/'))
boton_terror.grid(row=1, column=0, pady=20, padx=20)

boton_comedia = tk.Button(root, text="COMEDIA", command=lambda: mostrar_titulos(
    'https://www.fotogramas.es/series-tv-noticias/g19462352/mejores-series-comedia-netflix/'))
boton_comedia.grid(row=2, column=0, pady=20, padx=20)

boton_accion = tk.Button(root, text="ACCIÓN", command=lambda: mostrar_titulos(
    'https://www.fotogramas.es/series-tv-noticias/g40785295/mejores-series-accion-netflix/'))
boton_accion.grid(row=3, column=0, pady=20, padx=20)

boton_salir = tk.Button(root, text="Salir", command=root.quit)
boton_salir.grid(row=4, column=0, pady=20)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
