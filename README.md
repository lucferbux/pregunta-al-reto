# 🧭 Pregunta al reto

Asistente que responde dudas sobre el reto de la asignatura usando solo los documentos del curso: el enunciado, la rúbrica y las pautas. Es la app que enseño en la **sesión 1** funcionando, y la que desmonto en la **sesión 4** para contar cómo se construyó.

**App desplegada:** _(pendiente: pega aquí la URL cuando la despliegues)_

## Qué hace

Escribes una duda del reto, busca los fragmentos más parecidos entre los tres documentos y responde con ellos, diciendo de dónde sale cada cosa. Si algo no está en los documentos, lo dice en lugar de inventárselo.

## La pieza de IA

La API de Gemini para dos cosas distintas, embeddings con `gemini-embedding-001` para buscar y `gemini-3.8-flash` para redactar la respuesta. La búsqueda por similitud son treinta líneas de numpy, **sin Chroma**: Streamlit Community Cloud trae una versión de sqlite más antigua de la que pide chromadb, y con cuarenta fragmentos numpy va sobrado. Es el ejemplo perfecto de que la pieza más sencilla que resuelve el problema gana.

Si se acaba la cuota o falla la red, la app responde con un mensaje claro en lugar de romperse.

## Cómo la construí

Con un agente, a partir de dos ficheros: [`especificacion.md`](especificacion.md) y [`AGENTS.md`](AGENTS.md). Los prompts reales están en [`prompts.md`](prompts.md), que es lo que proyecto en la sesión 4.

## Ponerla en marcha

Los documentos del reto viven en `contenido/`.

En local:

```bash
pip install -r requirements.txt
mkdir -p .streamlit && echo 'GEMINI_API_KEY = "tu-clave"' > .streamlit/secrets.toml
streamlit run app.py
```

Desplegada por la ruta A, la de los alumnos: este repositorio público en GitHub, la app en share.streamlit.io y la clave en Settings → Secrets.

## Aviso

`contenido/` son copias de los documentos del reto, y la app responde con lo que tenga en esa carpeta.
