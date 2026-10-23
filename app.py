import streamlit as st
import time

# Configuración de la página
st.set_page_config(page_title="Promoción 2026 - Futuro Tech", page_icon="💻", layout="centered")

# ==========================================
# ESTADO GLOBAL COMPARTIDO EN EL SERVIDOR
# ==========================================
@st.cache_resource
def obtener_estado_global():
    # Guarda el estado 'hackeado' de forma global para TODAS las computadoras
    return {"hackeado": False}

estado = obtener_estado_global()

# ==========================================
# PANEL DE CONTROL OCULTO (Solo para el expositor)
# ==========================================
with st.sidebar:
    st.write("⚙️ **Panel del Expositor**")
    
    # Para acceder al panel del expositor pides una contraseña simple
    clave = st.text_input("Clave de control:", type="password")
    
    if clave == "1234":  # Puedes cambiar esta clave
        if st.button("🔴 HACKEAR TODO EL LABORATORIO"):
            estado["hackeado"] = True
            st.rerun()
            
        if st.button("🟢 Restablecer Sistema"):
            estado["hackeado"] = False
            st.rerun()

# ==========================================
# PASO 2: PANTALLA DE CIBERSEGURIDAD / HACKEO
# ==========================================
if estado["hackeado"]:
    st.error("🚨 ¡ALERTA DE SEGURIDAD CRÍTICA EN LA RED! 🚨")
    
    st.markdown("""
    <h1 style='color: #ff2b2b; text-align: center; font-family: monospace;'>⚠️ TU MENSAJE HA SIDO HACKEADO ⚠️</h1>
    <h3 style='text-align: center; color: #ff8800;'>[ INTERCEPTADO EN EL LABORATORIO DE CÓDIGO ]</h3>
    """, unsafe_allow_html=True)
    
    st.warning("🔒 **Inyección de datos interceptada:** La comunicación entre este equipo y el servidor central fue manipulada sin cifrado SSL/TLS.")
    
    st.code("""
    [NETWORK_LOG] IP 192.168.1.X intercepted via ARP Spoofing.
    [PAYLOAD] Executing remote exploit script...
    [ALERT] Unauthorized access granted. Session compromised!
    """, language="bash")
    
    st.markdown("---")
    st.markdown("""
    ### 🛡️ ¿Qué acaba de pasar en las 20 computadoras?
    El expositor cambió el estado central en la nube y **todas las máquinas del laboratorio cayeron simultáneamente**. 
    
    * Crear software es genial, pero **asegurar redes y aplicaciones** es lo que mantiene funcionando a los bancos, hospitales y empresas.
    * **¿Te gustaría ser quien aprenda a detener estos ataques?** ¡Ingeniería de Sistemas te enseña Ciberseguridad!
    """)

# ==========================================
# PASO 1: PANTALLA NORMAL (Formulario)
# ==========================================
else:
    st.title("🚀 ¡Bienvenidos al Futuro Digital!")
    st.subheader("Laboratorio de Pruebas de Software")

    with st.form("interaccion_form"):
        nombre = st.text_input("✍️ Escribe tu nombre o apodo:")
        interes = st.selectbox(
            "💡 ¿Qué área de la tecnología te atrae más?",
            ["Desarrollo de Videojuegos", "Inteligencia Artificial", "Ciberseguridad y Hacking Ético", "Redes y Servidores"]
        )
        enviar = st.form_submit_button("🔥 ¡Enviar datos al servidor!")

    if enviar:
        if nombre:
            st.balloons()
            st.success(f"¡Excelente, **{nombre}**! Tus datos han sido registrados correctamente en la red.")
        else:
            st.warning("Escribe tu nombre antes de enviar.")

    st.markdown("---")
    st.caption("🟢 Estado del Servidor: En línea | Canal seguro de datos activa")

    # Bucle de actualización automática en segundo plano (Revisa cada 2 segundos)
    time.sleep(2)
    st.rerun()
