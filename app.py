import tkinter as tk
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("320x500")
ventana.resizable(False, False)
ventana.configure(bg="#EADCF8")
pantalla = tk.Entry(
    ventana,
    font=("Arial", 25),
    bg="#F9F0FF",
    fg="#7028A0",
    justify="right",
    bd=0
)
pantalla.pack(fill="x", padx=15, pady=20, ipady=15)
marco = tk.Frame(ventana, bg="#EADCF8")
marco.pack(expand=True, fill="both", padx=10, pady=5)
def pulsar(valor):
    pantalla.insert(tk.END, valor)
def borrar():
    pantalla.delete(0, tk.END)
def calcular():
    try:
        resultado = eval(pantalla.get())
        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(resultado))
    except:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "Error")
botones = [
    ("C", 0, 0, "#D8B4F8", borrar),
    ("(", 0, 1, "#D8B4F8", lambda: pulsar("(")),
    (")", 0, 2, "#D8B4F8", lambda: pulsar(")")),
    ("÷", 0, 3, "#C084FC", lambda: pulsar("/")),
    ("7", 1, 0, "#FFFFFF", lambda: pulsar("7")),
    ("8", 1, 1, "#FFFFFF", lambda: pulsar("8")),
    ("9", 1, 2, "#FFFFFF", lambda: pulsar("9")),
    ("×", 1, 3, "#C084FC", lambda: pulsar("*")),
    ("4", 2, 0, "#FFFFFF", lambda: pulsar("4")),
    ("5", 2, 1, "#FFFFFF", lambda: pulsar("5")),
    ("6", 2, 2, "#FFFFFF", lambda: pulsar("6")),
    ("−", 2, 3, "#C084FC", lambda: pulsar("-")),
    ("1", 3, 0, "#FFFFFF", lambda: pulsar("1")),
    ("2", 3, 1, "#FFFFFF", lambda: pulsar("2")),
    ("3", 3, 2, "#FFFFFF", lambda: pulsar("3")),
    ("+", 3, 3, "#C084FC", lambda: pulsar("+")),
    ("±", 4, 0, "#FFFFFF", lambda: pulsar("-")),
    ("0", 4, 1, "#FFFFFF", lambda: pulsar("0")),
    (".", 4, 2, "#FFFFFF", lambda: pulsar(".")),
    ("=", 4, 3, "#A855F7", calcular),
]
for texto, fila, columna, color, accion in botones:
    boton = tk.Button(
        marco,
        text=texto,
        font=("Arial", 16, "bold"),
        bg=color,
        fg="#54206F",
        activebackground="#E9B8FF",
        relief="flat",
        bd=0,
        command=accion
    )
    boton.grid(
        row=fila,
        column=columna,
        padx=4,
        pady=4,
        sticky="nsew"
    )
for fila in range(5):
    marco.rowconfigure(fila, weight=1)
for columna in range(4):
    marco.columnconfigure(columna, weight=1)
ventana.mainloop()
