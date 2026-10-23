import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Promoción 2026 - Futuro Tech", page_icon="🚀", layout="centered")

# Título y bienvenida
st.title("🚀 ¡Bienvenidos al Futuro Digital!")
st.subheader("Crea el software que cambiará el mundo")

# Formulario interactivo
with st.form("interaccion_form"):
    nombre = st.text_input("✍️ Escribe tu nombre o apodo:")
    interes = st.selectbox(
        "💡 ¿Qué área te causa más curiosidad?",
        ["Desarrollo de Videojuegos", "Inteligencia Artificial", "Ciberseguridad y Hackers", "Robótica y Apps"]
    )
    enviar = st.form_submit_button("🔥 ¡Enviar mi idea a la pantalla grande!")

# Reacción interactiva en tiempo real
if enviar:
    if nombre:
        st.balloons()  # Efecto visual de globos en pantalla
        st.success(f"¡Genial, **{nombre}**! Tu futuro en **{interes}** comienza hoy. 💻")
    else:
        st.warning("Escribe tu nombre para activar el sistema.")

# Sección visual para mostrar datos rápidos
st.markdown("---")
st.write("📊 **Encuesta rápida en vivo:**")
col1, col2 = st.columns(2)
col1.metric(label="Líneas de código ejecutadas", value="100%", delta="En tiempo real")
col2.metric(label="Posibilidades de crear tu propia App", value="∞", delta="Infinitas")