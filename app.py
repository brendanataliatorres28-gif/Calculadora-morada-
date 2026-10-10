
import streamlit as st

st.set_page_config(
    page_title="Mi Calculadora Morada",
    page_icon="💜",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #1b102b, #392052, #7652a5);
    color: white;
}
h1 {
    color: #f0d9ff;
    text-align: center;
}
p {
    color: #f5eaff;
}
.resultado {
    background: #2b173e;
    padding: 18px;
    border-radius: 18px;
    text-align: center;
    border: 2px solid #c9a4ff;
}
div.stButton > button {
    background-color: #a879e8;
    color: white;
    border-radius: 12px;
    border: 1px solid #e5d0ff;
}
</style>
""", unsafe_allow_html=True)

st.title("💜 Mi Calculadora")
st.write("✨ Tus cuentas, con estilo ✨")

st.markdown("### 🪻 Escribe tus números")

numero1 = st.number_input(
    "Primer número",
    value=0.0,
    key="numero1"
)

operacion = st.selectbox(
    "Elige una operación",
    ["➕ Sumar", "➖ Restar", "✖️ Multiplicar", "➗ Dividir"]
)

numero2 = st.number_input(
    "Segundo número",
    value=0.0,
    key="numero2"
)

if st.button("💜 CALCULAR 💜", use_container_width=True):
    if operacion == "➕ Sumar":
        resultado = numero1 + numero2
    elif operacion == "➖ Restar":
        resultado = numero1 - numero2
    elif operacion == "✖️ Multiplicar":
        resultado = numero1 * numero2
    else:
        resultado = None if numero2 == 0 else numero1 / numero2

    if resultado is None:
        st.error("🪻 No se puede dividir entre cero.")
    else:
        st.markdown(
            f'<div class="resultado"><h3>✨ Resultado ✨</h3>'
            f'<h2>{resultado:g}</h2></div>',
            unsafe_allow_html=True
        )

st.caption("Hecha con 💜 y Python")

