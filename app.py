"""Pregunta al reto · asistente del curso Fundamentos de programación (Python para IA).

Responde dudas sobre el reto usando solo los documentos del curso: el enunciado,
la rúbrica y las pautas. Es la app que enseño en la sesión 1 y que desmonto en la
sesión 4, y es exactamente el patrón RAG de la sesión 3.

Por qué no usa Chroma: Streamlit Community Cloud trae una versión de sqlite más
antigua de la que necesita chromadb, así que la búsqueda por similitud son treinta
líneas de numpy. Con cuarenta fragmentos va sobrado, y hay una pieza menos que falle.
"""

from __future__ import annotations

import re
from pathlib import Path

import numpy as np
import streamlit as st
from google import genai
from google.genai import types

MODELO = "gemini-3.8-flash"
MODELO_EMBEDDINGS = "gemini-embedding-001"
CARPETA = Path(__file__).parent / "contenido"
TROZO = 900          # caracteres por fragmento
VECINOS = 4          # fragmentos que se le pasan al modelo

INSTRUCCIONES = """Eres el asistente del reto de la asignatura Fundamentos de programación
(Python para IA) del Máster en Inteligencia Artificial de OBS Business School.

Respondes dudas del alumnado sobre el reto usando SOLO el contexto que te paso.

Reglas:
- Si la respuesta no está en el contexto, di que no lo encuentras en los documentos del
  reto y sugiere preguntar a Lucas en el foro. No te inventes plazos, notas ni requisitos.
- Responde en español de España, en dos o cuatro frases, y hablando de vosotros.
- Cuando cites un requisito concreto, di de qué documento sale.
- No des tu opinión sobre lo que deberían construir: eso lo decide cada persona."""


# --- carga y troceado de los documentos --------------------------------------
def trocear(texto: str, fuente: str) -> list[dict]:
    """Parte un documento por secciones y luego por tamaño, guardando el titular."""
    trozos: list[dict] = []
    seccion = "Introducción"
    buffer: list[str] = []

    def cerrar() -> None:
        cuerpo = "\n".join(buffer).strip()
        if not cuerpo:
            return
        for i in range(0, len(cuerpo), TROZO):
            trozos.append({"fuente": fuente, "seccion": seccion, "texto": cuerpo[i : i + TROZO]})

    for linea in texto.splitlines():
        if re.match(r"^#{1,3} ", linea):
            cerrar()
            buffer = []
            seccion = linea.lstrip("# ").strip()
        else:
            buffer.append(linea)
    cerrar()
    return trozos


@st.cache_resource(show_spinner="Indexando los documentos del reto...")
def indexar(api_key: str) -> tuple[list[dict], np.ndarray, genai.Client]:
    """Trocea los documentos, los convierte en vectores y los deja listos en memoria."""
    cliente = genai.Client(api_key=api_key)
    trozos: list[dict] = []
    for ruta in sorted(CARPETA.glob("*.md")):
        trozos += trocear(ruta.read_text(encoding="utf-8"), ruta.stem.replace("_", " "))
    if not trozos:
        raise RuntimeError(f"no hay documentos en {CARPETA}")

    vectores = []
    for inicio in range(0, len(trozos), 20):   # el API acepta lotes
        lote = [t["texto"] for t in trozos[inicio : inicio + 20]]
        respuesta = cliente.models.embed_content(model=MODELO_EMBEDDINGS, contents=lote)
        vectores += [e.values for e in respuesta.embeddings]

    matriz = np.array(vectores, dtype="float32")
    matriz /= np.linalg.norm(matriz, axis=1, keepdims=True)   # normalizar: el coseno es un producto
    return trozos, matriz, cliente


def buscar(pregunta: str, trozos: list[dict], matriz: np.ndarray, cliente: genai.Client) -> list[dict]:
    """Devuelve los fragmentos más parecidos a la pregunta."""
    consulta = cliente.models.embed_content(model=MODELO_EMBEDDINGS, contents=pregunta)
    vector = np.array(consulta.embeddings[0].values, dtype="float32")
    vector /= np.linalg.norm(vector)
    similitud = matriz @ vector
    return [trozos[i] | {"similitud": float(similitud[i])} for i in similitud.argsort()[::-1][:VECINOS]]


def responder(pregunta: str, contexto: list[dict], cliente: genai.Client) -> str:
    bloques = [f"[{c['fuente']} · {c['seccion']}]\n{c['texto']}" for c in contexto]
    prompt = "Contexto:\n\n" + "\n\n---\n\n".join(bloques) + f"\n\nPregunta del alumno: {pregunta}"
    try:
        respuesta = cliente.models.generate_content(
            model=MODELO,
            contents=prompt,
            config=types.GenerateContentConfig(system_instruction=INSTRUCCIONES, temperature=0.2),
        )
        return respuesta.text or "No he recibido respuesta del modelo. Probad otra vez."
    except Exception as error:   # cuota agotada, red caída, clave mal puesta
        return f"⚠️ Ahora mismo no puedo responder ({error}). Probad en un minuto."


# --- interfaz -----------------------------------------------------------------
st.set_page_config(page_title="Pregunta al reto", page_icon="🧭")
st.title("🧭 Pregunta al reto")
st.caption(
    "Asistente del reto de Fundamentos de programación. Responde solo con el enunciado, "
    "la rúbrica y las pautas, así que si algo no está ahí, os lo dirá."
)

try:
    CLAVE = st.secrets["GEMINI_API_KEY"]
except Exception:
    st.error("Falta el secreto GEMINI_API_KEY. Se añade en Settings → Secrets de la app.")
    st.stop()

try:
    TROZOS, MATRIZ, CLIENTE = indexar(CLAVE)
except Exception as error:
    st.error(f"No he podido indexar los documentos: {error}")
    st.stop()

st.success(f"{len(TROZOS)} fragmentos indexados de {len(list(CARPETA.glob('*.md')))} documentos del reto.")

EJEMPLOS = [
    "¿Qué tengo que entregar en el hito de la semana 2?",
    "¿Dónde despliego mi app si mi cuenta de Hugging Face es nueva?",
    "¿Qué pasa si el día de la corrección mi app no carga?",
]
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

with st.sidebar:
    st.subheader("Preguntas de ejemplo")
    for ejemplo in EJEMPLOS:
        if st.button(ejemplo, use_container_width=True):
            st.session_state.pendiente = ejemplo
    st.divider()
    st.caption("Construida en la sesión 4 con un agente, a partir de la especificación y del AGENTS.md.")

for mensaje in st.session_state.mensajes:
    with st.chat_message(mensaje["role"]):
        st.markdown(mensaje["content"])
        if mensaje.get("fuentes"):
            with st.expander("De dónde sale"):
                for fuente in mensaje["fuentes"]:
                    st.markdown(f"**{fuente['fuente']} · {fuente['seccion']}** ({fuente['similitud']:.2f})")
                    st.caption(fuente["texto"][:300] + "…")

pregunta = st.chat_input("¿Qué quieres saber del reto?") or st.session_state.pop("pendiente", None)
if pregunta:
    st.session_state.mensajes.append({"role": "user", "content": pregunta})
    with st.chat_message("user"):
        st.markdown(pregunta)
    fuentes = buscar(pregunta, TROZOS, MATRIZ, CLIENTE)
    texto = responder(pregunta, fuentes, CLIENTE)
    with st.chat_message("assistant"):
        st.markdown(texto)
    st.session_state.mensajes.append({"role": "assistant", "content": texto, "fuentes": fuentes})
