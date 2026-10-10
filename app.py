
import streamlit as st

st.set_page_config(
    page_title="Mi Calculadora Morada",
    page_icon="💜",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(145deg, #24102f, #673b85, #9561bd);
    color: white;
}
header[data-testid="stHeader"] {
    background: transparent;
}
h1, h2, p, label {
    color: white !important;
}
.calculadora {
    background: #21132b;
    border: 2px solid #d6b4ff;
    border-radius: 25px;
    padding: 25px 20px;
    text-align: right;
    margin-bottom: 18px;
}
.resultado {
    font-size: 48px;
    font-weight: bold;
    color: white;
    min-height: 65px;
    overflow-wrap: anywhere;
}
.stButton > button {
    width: 100%;
    height: 62px;
    border-radius: 15px;
    border: 1px solid #e4caff;
    background: #a875df;
    color: white;
    font-size: 23px;
    font-weight: 600;
}
.stButton > button:hover {
    background: #c69afa;
    color: #24102f;
    border-color: white;
}
div[data-testid="stHorizontalBlock"] {
    gap: 8px;
}
div[data-testid="stNumberInput"] input {
    background: #35213f;
    color: white;
}
</style>
""", unsafe_allow_html=True)

if "pantalla" not in st.session_state:
    st.session_state.pantalla = "0"

if "anterior" not in st.session_state:
    st.session_state.anterior = None

if "operacion" not in st.session_state:
    st.session_state.operacion = None

if "nuevo" not in st.session_state:
    st.session_state.nuevo = False

def numero(valor):
    try:
        return float(valor)
    except (ValueError, TypeError):
        return 0.0

def mostrar_numero(valor):
    if valor == int(valor):
        return str(int(valor))
    return f"{valor:.10g}"

def pulsar(tecla):
    s = st.session_state
    pantalla = s.pantalla

    if tecla == "C":
        s.pantalla = "0"
        s.anterior = None
        s.operacion = None
        s.nuevo = False
        return

    if tecla == "⌫":
        if not s.nuevo:
            s.pantalla = pantalla[:-1] or "0"
            if s.pantalla == "-":
                s.pantalla = "0"
        return

    if tecla == "±":
        if pantalla.startswith("-"):
            s.pantalla = pantalla[1:]
        else:
            s.pantalla = "-" + pantalla
        return

    if tecla == "%":
        s.pantalla = mostrar_numero(numero(pantalla) / 100)
        return

    if tecla in ["+", "−", "×", "÷"]:
        s.anterior = numero(pantalla)
        s.operacion = tecla
        s.nuevo = True
        return

    if tecla == "=":
        if s.operacion is not None and s.anterior is not None:
            a = s.anterior
            b = numero(pantalla)
            op = s.operacion

            if op == "+":
                r = a + b
            elif op == "−":
                r = a - b
            elif op == "×":
                r = a * b
            else:
                if b == 0:
                    s.pantalla = "Error"
                    s.operacion = None
                    s.anterior = None
                    s.nuevo = True
                    return
                r = a / b

            s.pantalla = mostrar_numero(r)
            s.operacion = None
            s.anterior = None
            s.nuevo = True
        return

    if tecla == ".":
        if s.nuevo or pantalla == "Error":
            s.pantalla = "0."
            s.nuevo = False
        elif "." not in pantalla:
            s.pantalla += "."
        return

    if tecla.isdigit():
        if s.nuevo or pantalla == "Error":
            s.pantalla = tecla
            s.nuevo = False
        elif pantalla == "0":
            s.pantalla = tecla
        else:
            s.pantalla += tecla

st.markdown(
    "<h1 style='text-align:center'>💜 Mi Calculadora</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center'>✨ Tu pequeño mundo lila ✨</p>",
    unsafe_allow_html=True
)

operacion_actual = st.session_state.operacion or ""
st.markdown(
    f"""<div class="calculadora">
    <p style="color:#d6b4ff !important">💜 Operación: {operacion_actual}</p>
    <div class="resultado">{st.session_state.pantalla}</div>
    </div>""",
    unsafe_allow_html=True
)

filas = [
    ["C", "⌫", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "−"],
    ["1", "2", "3", "+"],
    ["±", "0", ".", "="]
]

for fila in filas:
    columnas = st.columns(4)
    for columna, tecla in zip(columnas, fila):
        with columna:
            if st.button(tecla, key="boton_" + tecla):
                pulsar(tecla)
                st.rerun()

st.markdown(
    "<p style='text-align:center;color:#e4caff !important'>"
    "Hecha con 💜 y Python</p>",
    unsafe_allow_html=True
)
