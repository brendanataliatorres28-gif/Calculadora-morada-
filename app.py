import streamlit as st
st.set_page_config(
    page_title="Calculadora Morada",
    page_icon="💜",
    layout="centered"
)
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f3e5ff, #e0c3fc);
}
h1 {
    color: #7629a6;
    text-align: center;
}
div.stButton > button {
    width: 100%;
    height: 60px;
    border-radius: 14px;
    background-color: #c084fc;
    color: white;
    font-size: 22px;
    font-weight: bold;
    border: 2px solid #ffffff;
}
div.stButton > button:hover {
    background-color: #a855f7;
    color: white;
}
</style>
""", unsafe_allow_html=True)
st.markdown("# 💜 Calculadora")
if "expresion" not in st.session_state:
    st.session_state.expresion = ""
st.text_input(
    "Resultado y operación",
    key="expresion",
    placeholder="0"
)
filas = [
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "×"],
    ["1", "2", "3", "−"],
    ["C", "0", ".", "+"]
]
for fila in filas:
    columnas = st.columns(4, gap="small")
    for i, numero in enumerate(fila):
        if columnas[i].button(numero, key=f"{fila[0]}_{numero}"):
            if numero == "C":
                st.session_state.expresion = ""
            else:
                simbolo = numero
                if numero == "×":
                    simbolo = "*"
                elif numero == "÷":
                    simbolo = "/"
                elif numero == "−":
                    simbolo = "-"
                st.session_state.expresion += simbolo
            st.rerun()
if st.button("＝ CALCULAR", use_container_width=True):
    try:
        expresion = st.session_state.expresion
        permitidos = "0123456789.+-*/() "
        if not expresion or any(c not in permitidos for c in expresion):
            st.error("Escribe una operación válida.")
        else:
            resultado = eval(expresion, {"__builtins__": {}}, {})
            st.session_state.expresion = str(resultado)
            st.rerun()
    except Exception:
        st.error("No se pudo calcular. Revisa la operación.")
