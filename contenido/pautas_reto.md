# Pautas del reto

**Fundamentos de programación (Python para IA)** · Máster en Inteligencia Artificial · OBS Business School

Las pautas no tienen nota. Son el entrenamiento semanal para llegar al hito de la semana 2 y a la entrega final con una propuesta sólida. Cada una trae **preguntas guía**: no hay que entregarlas, pero si podéis responderlas vais por buen camino.

Todas las pautas se pueden hacer desde Google Colab y el navegador. Si preferís trabajar en local con un agente (Copilot, Cursor, Gemini CLI, Claude Code o Codex), adelante: los pasos son los mismos.

El reto es individual. Si os habéis organizado en equipo, que es opcional, hacéis juntos lo que queráis compartir, pero cada persona despliega su app y entrega lo suyo.

## Pauta 1 · Semana 1 · Implicación

**Objetivo:** tener un problema real, un usuario concreto en la cabeza y una app hola mundo en internet.

1. **Elegid el problema.** Una lista de 3 candidatos y os quedáis con uno. Mejor pequeño y real que grande y vago.
2. **Describid al usuario.** Quién tiene ese problema, cómo lo resuelve hoy y qué le molesta. Vale que seáis vosotros mismos o alguien de vuestro entorno: no hace falta entrevistar a nadie.
3. **Cread las cuentas:** GitHub y Streamlit Community Cloud (ruta A). Si vuestra cuenta de Hugging Face tiene más de 30 días y el email verificado, también podéis usar la ruta B.
4. **Desplegad el hola mundo** siguiendo la sesión 1. Guardad la URL.
5. **Si vais a trabajar en equipo** (opcional), decidid ahora cómo os organizáis con el [acuerdo de equipo](acuerdo_equipo.md) y, si queréis compartir repositorio, seguid la [guía de GitHub en equipo](guia_equipo_github.md).

**Preguntas guía:**

- ¿Quién tiene exactamente el problema y cómo lo resuelve hoy sin vuestra app? (CE63015)
- ¿Qué tendría que pasar para que esa persona usara la app una segunda vez? (CE63015)
- ¿Qué parte del problema resuelve de verdad la IA y qué parte se resolvería con una hoja de cálculo? (CE63011)

## Pauta 2 · Semana 2 · Investigación → hito de la semana 2

**Objetivo:** una especificación que cualquier asistente de IA podría construir sin preguntaros, y la versión 0 de vuestra app en internet.

1. **Escribid la especificación** con la [plantilla](plantillas/especificacion.md).
2. **Escribid el `AGENTS.md`** de vuestra app con la [plantilla](plantillas/AGENTS.md). Veinte minutos ahora os ahorran horas después.
3. **Pasad la especificación a vuestro asistente o agente** y pedidle la versión 0. Revisad lo que genera antes de aceptarlo.
4. **Desplegad la versión 0.** Puede no tener IA todavía: basta con la interfaz y un flujo que funcione.
5. **Publicad la ficha del hito** en el debate Hito de la semana 2, recomendado antes del 20/10/2026 para que os llegue el feedback en la sesión 3. Son cinco líneas ([plantilla](plantillas/ficha_hito.md)) y no tiene nota propia.

**Preguntas guía:**

- Si dais vuestra especificación a dos asistentes distintos, ¿construyen lo mismo? Si no, ¿qué le falta? (CE63011)
- ¿Qué necesita saber el agente de vuestro proyecto para no tener que repetírselo en cada conversación? (CE63014)
- ¿Qué tareas dejaríais hacer al agente sin revisar y cuáles no? ¿Por qué? (CE63014)
- ¿Un modelo de Hugging Face, la API de un LLM o un RAG? ¿Qué gana y qué pierde vuestra app con cada opción? (CE63011)

## Pauta 3 · Semana 3 · Acción

**Objetivo:** la pieza de IA funcionando dentro de la app, con la clave protegida, y la prueba entre compañeros hecha.

1. **Integrad la IA** que decidisteis en la especificación: la API de Gemini (plantillas de [Streamlit](plantillas/streamlit/app.py) y [Gradio](plantillas/huggingface/app.py)), un modelo de Hugging Face o un RAG con vuestros documentos (sesión 3 y parte C del ejercicio 3).
2. **Guardad la clave como secreto** en vuestra plataforma. Comprobad que no aparece en ningún archivo del repositorio.
3. **Probad la app de un compañero.** Entrad en el debate Hito de la semana 2, elegid una app que todavía tenga pocas respuestas, usadla cinco minutos como si fuerais su usuario y respondedle en su hilo: qué habéis probado, qué ha funcionado, dónde os habéis atascado y una sugerencia.
4. **Apuntad lo que os digan de la vuestra.** Si nadie la ha probado todavía, probadla vosotros como usuario con los casos de los criterios de aceptación de vuestra especificación, que vale igual.
5. **Proteged lo que puede fallar:** que la app responda con un mensaje claro si se acaba la cuota o no hay conexión.

**Preguntas guía:**

- ¿Cómo sabéis que el código que ha generado la IA hace lo que dice? ¿Qué probaríais antes de enseñarlo? (CE63011)
- ¿Qué le pasa a vuestra app si mañana se acaba la cuota gratuita o retiran el modelo que usa? (CE63015)
- ¿Dónde está vuestra clave de API y quién podría verla? (CE63015)
- ¿Qué pasó en la prueba que no esperabais y qué habéis cambiado por ello? (CE63015)

## Pauta 4 · Semana 4 · Comunicación → entrega final

**Objetivo:** la versión final, bien documentada, y un pitch escrito que convenza en cinco frases.

1. **Aplicad lo aprendido** en la prueba: al menos un cambio concreto en la app.
2. **Cerrad el README** de vuestra app con la [plantilla](plantillas/README_app.md).
3. **Escribid el pitch:** cinco frases, siguiendo el guion del [enunciado](enunciado.md#pitch-escrito).
4. **Rellenad el documento de entrega** con la [plantilla](plantillas/entrega_final.md), comprobad los enlaces en una ventana de incógnito y entregad. Todas las actividades cierran el 02/11/2026.

**Pregunta guía:**

- Si vuestra app fuera un producto, ¿qué frase la vendería en diez segundos y qué dato la respaldaría? (CE63015)
