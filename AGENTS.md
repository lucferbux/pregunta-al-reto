# AGENTS.md · Pregunta al reto

## Qué es este proyecto

Asistente que responde dudas del reto de la asignatura Fundamentos de programación usando solo los documentos del curso, que están en `contenido/`. Lo usan alumnos sin perfil técnico durante cuatro semanas.

## Cómo está hecho

- Python 3.12, una sola pantalla.
- Interfaz: Streamlit, desplegada en Streamlit Community Cloud (ruta A del reto).
- IA: API de Gemini con el SDK `google-genai`. Los dos modelos están en las constantes `MODELO` y `MODELO_EMBEDDINGS` de `app.py`.
- Búsqueda: similitud coseno con numpy sobre los embeddings, en memoria. **No añadas Chroma ni ninguna base de datos vectorial**: Streamlit Cloud trae un sqlite más antiguo del que necesita chromadb y con cuarenta fragmentos no aporta nada.
- Archivos: `app.py`, `requirements.txt`, `contenido/*.md` y este fichero. La especificación completa está en `especificacion.md`, léela antes de proponer cambios.

## Reglas

- La clave va SIEMPRE en `st.secrets["GEMINI_API_KEY"]`. Nunca en el código, ni en el README, ni en el chat.
- Toda llamada a la API va en `try/except` y muestra un mensaje claro para el usuario.
- El indexado va dentro de `@st.cache_resource`: cada recarga no puede volver a pagar los embeddings.
- La app responde solo con el contexto recuperado. Si no está, dice que no lo encuentra y manda al foro.
- Textos en español de España, hablando de vosotros, frases cortas.
- Un cambio por petición, y al terminar explica qué has cambiado y por qué.

## Cómo comprobar que funciona

- `streamlit run app.py` con `.streamlit/secrets.toml` en local.
- Casos de prueba (entrada → lo que esperamos):
  1. "¿Qué entrego en el hito de la semana 2?" → la ficha de cinco líneas, citando el enunciado.
  2. "¿Qué nota saco si entrego tarde?" → dice que no está en los documentos.
  3. Clave inválida → mensaje claro, sin traza de error en pantalla.

## Qué no hacer

- No cambies los modelos ni metas una base de datos vectorial sin preguntar.
- No toques los ficheros de `contenido/`: son copias de los documentos oficiales del reto.
- No hagas push ni redespliegues sin avisar.
