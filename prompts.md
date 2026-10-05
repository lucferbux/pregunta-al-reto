# Los prompts reales con los que se construyó

Esto es lo que proyecto en la sesión 4, porque es la parte que no se ve en el resultado. Cuatro prompts y dos correcciones.

## 1. El plan, sin código

> Lee `especificacion.md` y `AGENTS.md`. Propón un plan para construir la versión 0 de esta app. No escribas código todavía: dime qué ficheros vas a crear, qué función hace qué y qué dudas tienes sobre la especificación.

Lo que devolvió tenía una duda buena: si el indexado se hacía en cada recarga, cada visita pagaba los embeddings de todos los documentos. Ahí se decidió el `@st.cache_resource`.

## 2. La corrección del plan

> El plan está bien con dos cambios. El indexado va en caché y solo se hace una vez por sesión de la app. Y quiero ver de qué documento y de qué sección sale cada respuesta, así que el troceado tiene que guardar el titular de la sección. Adelante.

## 3. La construcción

> Escribe `app.py` y `requirements.txt` siguiendo el plan. Respeta lo que dice `AGENTS.md` sobre los secretos y sobre no meter Chroma.

## 4. El caso límite que faltaba

> Prueba el caso 2 de `AGENTS.md`, la pregunta cuya respuesta no está en los documentos. La app se inventa una fecha de entrega. Arréglalo tocando solo las instrucciones del sistema, no la búsqueda.

Esta es la lección de la sesión 3 en directo: el RAG recupera siempre algo, aunque no tenga que ver, y lo que evita que el modelo se invente cosas es una instrucción explícita de decir que no lo sabe.

## 5. Antes del despliegue

> Repasa `app.py` buscando cualquier sitio donde la clave pueda acabar en pantalla, en un log o en el repositorio. Dime qué has revisado y qué has encontrado.

## Qué delegué y qué revisé a mano

- **Delegué:** el troceado por secciones, la interfaz de Streamlit y el formato del bloque de fuentes.
- **Revisé a mano, línea a línea:** dónde se lee la clave, el `try/except` de las llamadas a la API y las instrucciones del sistema, que es lo que decide si la app miente o no.
- **Rechacé:** una primera versión que guardaba las preguntas en un fichero para "mejorar el asistente". Ni datos de alumnos, ni cosas que no están en la especificación.
