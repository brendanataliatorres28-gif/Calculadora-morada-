
import streamlit as st

st.set_page_config(
    page_title="Calculadora Morada",
    page_icon="💜",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(160deg, #180d2b, #49246b, #9b70d6);
    color: white;
}
.block-container {
    max-width: 420px;
    padding-top: 2rem;
}
h1 {
    text-align: center;
    color: #f3e5ff;
}
.pantalla {
    background: #211331;
    border: 2px solid #d5b4ff;
    border-radius: 20px;
    padding: 22px;
    text-align: right;
    margin-bottom: 18px;
}
div.stButton > button {
    background: #a879e8;
    color: white;
    border: 1px solid #e8d7ff;
    border-radius: 15px;
    min-height: 55px;
    font-size: 22px;
    font-weight: bold;
}
div.stButton > button:hover {
    background: #c49af5;
    color: #211331;
    border-color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("💜 Calculadora")
st.caption("✨ Mi pequeño mundo lila ✨")

if "expresion" not in st.session_state:
    st.session_state.expresion = ""
if "resultado" not in st.session_state:
    st.session_state.resultado = ""

st.markdown(
    f'<div class="pantalla"><div>💜 Operación</div>'
    f'<h2>{st.session_state.expresion or "0"}</h2>'
    f'<div>Resultado: {st.session_state.resultado}</div></div>',
    unsafe_allow_html=True
)

def pulsar(valor):
    if valor == "C":
        st.session_state.expresion = ""
        st.session_state.resultado = ""
    elif valor == "⌫":
        st.session_state.expresion = st.session_state.expresion[:-1]
    elif valor == "=":
        try:
            expr = st.session_state.expresion
            permitido = set("0123456789.+-*/() ")
            if not expr or any(c not in permitido for c in expr):
                raise ValueError
            respuesta = eval(expr, {"__builtins__": {}}, {})
            st.session_state.resultado = str(respuesta)
        except Exception:
            st.session_state.resultado = "Error"
    else:
        st.session_state.expresion += valor

filas = [
    ["C", "⌫", "(", ")"],
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "×"],
    ["1", "2", "3", "−"],
    ["0", ".", "=", "+"],
]

for fila in filas:
    columnas = st.columns(4)
    for columna, valor in zip(columnas, fila):
        with columna:
            if st.button(valor, key="boton_" + valor + "_" + str(filas.index(fila)),
                         use_container_width=True):
                traduccion = {"÷": "/", "×": "*", "−": "-"}
                pulsar(traduccion.get(valor, valor))
                st.rerun()

st.markdown(
    "<p style='text-align:center;color:#ead8ff'>Hecha con 💜 y Python</p>",
    unsafe_allow_html=True
)


