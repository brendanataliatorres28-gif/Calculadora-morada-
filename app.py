import tkinter as tk

ventana = tk\.Tk&#40;&#41;
ventana\.title&#40;"Calculadora"&#41;
ventana\.geometry&#40;"320x500"&#41;
ventana\.resizable&#40;False, False&#41;
ventana\.configure&#40;bg="\#EADCF8"&#41;

pantalla = tk\.Entry&#40;
    ventana,
    font=&#40;"Arial", 25&#41;,
    bg="\#F9F0FF",
    fg="\#7028A0",
    justify="right",
    bd=0
&#41;
pantalla\.pack&#40;fill="x", padx=15, pady=20, ipady=15&#41;

marco = tk\.Frame&#40;ventana, bg="\#EADCF8"&#41;
marco\.pack&#40;expand=True, fill="both", padx=10, pady=5&#41;

def pulsar&#40;valor&#41;:
    pantalla\.insert&#40;tk\.END, valor&#41;

def borrar&#40;&#41;:
    pantalla\.delete&#40;0, tk\.END&#41;

def calcular&#40;&#41;:
    try:
        resultado = eval&#40;pantalla\.get&#40;&#41;&#41;
        pantalla\.delete&#40;0, tk\.END&#41;
        pantalla\.insert&#40;0, str&#40;resultado&#41;&#41;
    except:
        pantalla\.delete&#40;0, tk\.END&#41;
        pantalla\.insert&#40;0, "Error"&#41;

botones = &#91;
        
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
