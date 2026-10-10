
import streamlit as st

st.set_page_config(
    page_title="Calculadora Morada",
    page_icon="💜",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(160deg, #f8efff, #e9d5ff, #d8b4fe);
}

.block-container {
    max-width: 390px;
    padding-top: 2rem;
}

h1 {
    color: #7027a0;
    text-align: center;
    font-size: 32px;
}

.calculadora {
    background: #ffffff;
    padding: 22px;
    border-radius: 28px;
    box-shadow: 0 8px 25px #8950a655;
}

.resultado {
    background: #f5eaff;
    color: #4c176b;
    padding: 22px 12px;
    border-radius: 18px;
    text-align: right;
    font-size: 34px;
    font-weight: bold;
    margin-bottom: 18px;
}

.stButton > button {
    width: 100%;
    height: 58px;
    border-radius: 17px;
    border: none;
    background: #f0dcff;
    color: #572078;
    font-size: 23px;
    font-weight: bold;
    transition: 0.2s;
}

.stButton > button:hover {
    background: #d8b4fe;
    color: #42145c;
    border: 2px solid #a855f7;
}

button[kind="primary"] {
    background: #8b3fc7 !important;
    color: white !important;
}

footer {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

if "pantalla" not in st.session_state:
    st.session_state.pantalla = "0"

if "nuevo_numero" not in st.session_state:
    st.session_state.nuevo_numero = True

if "anterior" not in st.session_state:
    st.session_state.anterior = None

if "operacion" not in st.session_state:
    st.session_state.operacion = None

def numero(valor):
    if st.session_state.nuevo_numero:
        st.session_state.pantalla = valor
        st.session_state.nuevo_numero = False
    else:
        if st.session_state.pantalla == "0":
            st.session_state.pantalla = valor
        else:
            st.session_state.pantalla += valor

def elegir_operacion(op):
    try:
        st.session_state.anterior = float(st.session_state.pantalla)
        st.session_state.operacion = op
        st.session_state.nuevo_numero = True
    except ValueError:
        st.session_state.pantalla = "Error"

def calcular():
    try:
        a = st.session_state.anterior
        b = float(st.session_state.pantalla)
        op = st.session_state.operacion

        if a is None or op is None:
            return

        if op == "+":
            resultado = a + b
        elif op == "−":
            resultado = a - b
        elif op == "×":
            resultado = a * b
        elif op == "÷":
            if b == 0:
                st.session_state.pantalla = "No se puede dividir por 0"
                st.session_state.nuevo_numero = True
                return
            resultado = a / b
        else:
            return

        if resultado == int(resultado):
            st.session_state.pantalla = str(int(resultado))
        else:
            st.session_state.pantalla = str(round(resultado, 8))

        st.session_state.anterior = None
        st.session_state.operacion = None
        st.session_state.nuevo_numero = True

    except (ValueError, TypeError):
        st.session_state.pantalla = "Error"
        st.session_state.nuevo_numero = True

def limpiar():
    st.session_state.pantalla = "0"
    st.session_state.nuevo_numero = True
    st.session_state.anterior = None
    st.session_state.operacion = None

st.title("💜 Calculadora")

st.markdown(
    '<div class="resultado">' + st.session_state.pantalla + '</div>',
    unsafe_allow_html=True
)

fila1 = st.columns(4, gap="small")
if fila1[0].button("AC"):
    limpiar()
    st.rerun()
if fila1[1].button("±"):
    try:
        st.session_state.pantalla = str(
            -float(st.session_state.pantalla)
        )
    except ValueError:
        pass
    st.rerun()
if fila1[2].button("%"):
    try:
        st.session_state.pantalla = str(
            float(st.session_state.pantalla) / 100
        )
    except ValueError:
        pass
    st.rerun()
if fila1[3].button("÷", type="primary"):
    elegir_operacion("÷")
    st.rerun()

fila2 = st.columns(4, gap="small")
for i, valor in enumerate(["7", "8", "9", "×"]):
    if fila2[i].button(
        valor,
        type="primary" if valor == "×" else "secondary"
    ):
        if valor in ["7", "8", "9"]:
            numero(valor)
        else:
            elegir_operacion(valor)
        st.rerun()

fila3 = st.columns(4, gap="small")
for i, valor in enumerate(["4", "5", "6", "−"]):
    if fila3[i].button(
        valor,
        type="primary" if valor == "−" else "secondary"
    ):
        if valor in ["4", "5", "6"]:
            numero(valor)
        else:
            elegir_operacion(valor)
        st.rerun()

fila4 = st.columns(4, gap="small")
for i, valor in enumerate(["1", "2", "3", "+"]):
    if fila4[i].button(
        valor,
        type="primary" if valor == "+" else "secondary"
    ):
        if valor in ["1", "2", "3"]:
            numero(valor)
        else:
            elegir_operacion(valor)
        st.rerun()

fila5 = st.columns(4, gap="small")
if fila5[0].button("⌫"):
    if len(st.session_state.pantalla) > 1:
        st.session_state.pantalla = st.session_state.pantalla[:-1]
    else:
        st.session_state.pantalla = "0"
    st.rerun()

if fila5[1].button("0"):
    numero("0")
    st.rerun()

if fila5[2].button("."):
    if "." not in st.session_state.pantalla:
        st.session_state.pantalla += "."
    st.rerun()

if fila5[3].button("=", type="primary"):
    calcular()
    st.rerun()

st.markdown(
    "<p style='text-align:center;color:#7027a0;"
    "margin-top:20px;'>Hecha con 💜 para ti</p>",
    unsafe_allow_html=True
)
