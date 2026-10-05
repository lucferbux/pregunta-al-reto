# Reto: vuestra primera herramienta con IA publicada en internet

**Fundamentos de programación (Python para IA)** · Máster en Inteligencia Artificial · OBS Business School · Mini-reto de 4 semanas

## El contexto

Muchas organizaciones pequeñas, como asociaciones, ONG, PYMEs o equipos dentro de una empresa, tienen problemas que una herramienta sencilla con IA resolvería: responder siempre las mismas dudas, clasificar incidencias, resumir documentos o simplificar textos administrativos. No tienen perfil técnico ni presupuesto para contratar desarrollo, así que esos problemas se siguen resolviendo a mano.

Hoy, con asistentes y agentes de programación, construir y publicar una herramienta así está al alcance de quien sepa especificar bien lo que quiere y comprobar lo que produce la IA. La habilidad escasa ya no es escribir código: es convertir un problema real en una especificación clara, dirigir a la IA y comprobar que el resultado sirve.

## La pregunta esencial

> ¿Cómo puede una persona sin perfil técnico construir en cuatro semanas una herramienta con IA que resuelva un problema real de su sector o de su comunidad, y publicarla para que cualquiera pueda usarla?

## Vuestro papel

Trabajáis en un pequeño estudio de producto con IA. Al estudio llegan encargos de organizaciones de vuestro entorno, y este mes os toca elegir uno y entregarlo funcionando.

Elegís vosotros el problema, de vuestro sector o de una comunidad cercana. Algunos ejemplos para inspiraros:

- un asistente que responde las dudas de los vecinos de una asociación a partir de sus estatutos;
- un clasificador de incidencias de soporte para una PYME;
- una herramienta que pasa textos administrativos a lectura fácil;
- un generador de resúmenes de actas de reuniones.

## El reto

Diseñad, construid y desplegad una aplicación con IA generativa que resuelva el problema que habéis elegido, probadla y mejoradla con lo que salga de la prueba.

- **Específico:** una app con IA para un problema concreto y un usuario concreto.
- **Medible:** la app funciona en una URL pública, y documentáis una prueba y un cambio hecho a partir de ella.
- **Alcanzable:** se construye con Colab, las plantillas de la asignatura y un asistente de IA. No se evalúa la complejidad del código.
- **Relevante:** es la forma real de prototipar productos con IA hoy.
- **Temporal:** cuatro semanas, con un hito en la semana 2 que no tiene nota y sirve para recibir feedback a mitad de camino.

## Restricciones

- **Coste cero:** capa gratuita de la API de Gemini y despliegue gratuito.
- **Ninguna clave de API en el código:** siempre en los secretos de la plataforma.
- **Ningún dato personal real:** para probar, inventad ejemplos.
- **Pensada para no técnicos:** la tiene que poder usar alguien sin conocimientos técnicos.

## Cómo se trabaja: individual, con equipo opcional

**El reto es individual.** Cada persona elige su problema, construye y despliega su app y entrega su propio documento, y toda la nota depende solo de lo que entrega ella.

Si queréis, podéis organizaros en un **equipo** de entre dos y seis personas para coordinaros: compartir un mismo problema y repartiros funcionalidades distintas, resolveros dudas y probaros las apps entre vosotros. Es opcional y no cambia nada de la evaluación: no hay nota de equipo, no hay que registrar el equipo en ningún sitio y, si os incorporáis tarde o preferís ir por vuestra cuenta, trabajáis en solitario sin ningún problema.

Si trabajáis en equipo y queréis compartir repositorio, tenéis el paso a paso en [`guia_equipo_github.md`](guia_equipo_github.md), y una plantilla para organizaros en [`acuerdo_equipo.md`](acuerdo_equipo.md). Las dos cosas son opcionales.

## Calendario

| Semana | Fase | Sesión en directo | Qué hacéis | Entrega |
|---|---|---|---|---|
| 1 | Implicación | Sesión 1 · Lanzamiento · 07/10/2026 | Elegir el problema y el usuario, y desplegar un hola mundo | Pauta 1 (sin nota) y autoevaluación de la sesión 1, recomendada antes del 13/10/2026 |
| 2 | Investigación | Sesión 2 · Mentoría · 14/10/2026 | Escribir la especificación y desplegar la versión 0 de la app | **Hito de la semana 2** (sin nota, con feedback en la sesión 3), recomendado antes del 20/10/2026, y autoevaluación de la sesión 2 |
| 3 | Acción | Sesión 3 · Mentoría · 21/10/2026 | Integrar la IA (modelo de Hugging Face, API de un LLM o RAG) y hacer la prueba entre compañeros | Pauta 3 (sin nota) y autoevaluación de la sesión 3, recomendada antes del 27/10/2026 |
| 4 | Comunicación | Sesión 4 · Solución y debate · 28/10/2026 | Mejorar con lo aprendido, cerrar el README y escribir el pitch | **Entrega final de la actividad principal** |

Todas las sesiones son a las 19:00. Las fechas de la tabla son recomendaciones para ir al día y para que el feedback del hito os llegue a tiempo, pero entregar al final no penaliza: todas las actividades cierran el 02/11/2026. Es el primer módulo y hay quien se incorpora tarde, así que nadie pierde nota por ello, aunque quien sigue el ritmo semanal llega al final mucho más tranquilo.

Las pautas de cada semana, con sus preguntas guía, están en [`pautas_reto.md`](pautas_reto.md).

## Dónde desplegar: dos rutas

Cada persona elige una ruta. Las dos valen igual.

| | Ruta A · Streamlit Community Cloud | Ruta B · Hugging Face Spaces |
|---|---|---|
| Para quién | Para todos | Solo si vuestra cuenta de Hugging Face tiene el email verificado y **más de 30 días** |
| Interfaz | Streamlit | Gradio |
| Cómo se despliega | Subís `app.py` y `requirements.txt` a un repositorio público de GitHub y lo conectáis en share.streamlit.io | Creáis un Space en la web (SDK Gradio, hardware ZeroGPU) y subís los archivos desde la web o desde Colab |
| Dónde va la clave | Settings → Secrets | Settings → Variables and secrets |
| URL | `https://<nombre>.streamlit.app` | `https://<usuario>-<space>.hf.space` |
| Plantilla | [`plantillas/streamlit/`](plantillas/streamlit/) | [`plantillas/huggingface/`](plantillas/huggingface/) |

Los enlaces temporales de Gradio en Colab (`share=True`) caducan en una semana: sirven para enseñar un prototipo, pero no cuentan como despliegue.

## Qué entregáis

Todo es texto, enlaces y capturas de pantalla. No hay que grabar ningún vídeo.

### Hito de la semana 2

No tiene nota propia: lo reviso, os devuelvo feedback en la sesión 3 y su contenido se evalúa después dentro de la actividad principal. Es una **ficha de cinco líneas** que publicáis como respuesta en el debate **Hito de la semana 2**, en Blackboard (plantilla en [`plantillas/ficha_hito.md`](plantillas/ficha_hito.md)):

1. **Problema:** una frase.
2. **Usuario:** quién lo tiene, en una frase.
3. **Qué hará la app:** hasta tres funcionalidades.
4. **Pieza de IA:** la API de Gemini, un modelo de Hugging Face o un RAG, y por qué, en una frase.
5. **Enlace a la versión 0** de vuestra app desplegada. Puede no tener IA todavía.

### Prueba entre compañeros

No hace falta buscar usuarios fuera del máster: los usuarios sois vosotros. En la semana 3, entrad en el debate del hito, elegid la app de un compañero, usadla cinco minutos como si fuerais su usuario y respondedle en su hilo con qué habéis probado, qué ha funcionado, dónde os habéis atascado y una sugerencia. Con lo que os digan a vosotros, haced al menos un cambio en vuestra app.

Si nadie ha probado la vuestra a tiempo, probadla vosotros poniéndoos en el papel del usuario, con los casos de los criterios de aceptación de vuestra especificación. Vale exactamente igual.

### Entrega final · actividad principal

Un único documento (`.docx` o `.pdf`) que sigue la plantilla [`plantillas/entrega_final.md`](plantillas/entrega_final.md), con estos apartados en este orden:

1. **Enlaces:** la app desplegada y el repositorio.
2. **Problema y usuario.**
3. **Especificación.**
4. **La pieza de IA:** qué usa, por qué y qué pasa si falla.
5. **Proceso con IA:** el fichero de contexto del agente (AGENTS.md, CLAUDE.md o GEMINI.md), los prompts clave, y qué delegasteis y qué revisasteis a mano.
6. **Prueba y mejora:** quién probó la app, qué pasó y qué cambiasteis.
7. **Pitch escrito:** cinco frases.
8. **Capturas:** cuatro capturas de pantalla, cada una con una línea que diga qué se ve: la app funcionando, la app ante un caso límite o un error, un momento de vuestro trabajo con la IA y la prueba. Enseñan cómo habéis trabajado mejor que cualquier explicación.

Cada apartado corresponde a un criterio de la rúbrica, así que si están todos, y en ese orden, sabéis que no os dejáis nada.

### Pitch escrito

Cinco frases, una por idea, que van en el apartado 7 del documento y en el README de vuestra app:

1. El problema y quién lo tiene.
2. Qué hace vuestra app.
3. Qué aporta la IA, que no se conseguiría sin ella.
4. Qué aprendisteis de la prueba y qué cambiasteis.
5. Qué haríais después, con un dato o un ejemplo concreto que lo respalde.

En la sesión 4 haremos un comité de inversores en directo con quien quiera enseñar su app. Es voluntario y no tiene nota.

## Recursos

- **Notebooks de las sesiones** y **`Ejercicio4.ipynb`** (la guía del reto en Colab).
- **Plantillas:** [`plantillas/`](plantillas/) (app para cada ruta, README, AGENTS.md, especificación, ficha del hito y entrega final).
- **Clave de Gemini gratuita:** aistudio.google.com/apikey.
- **Herramientas de IA para programar:** Gemini en Colab, GitHub Copilot, Cursor, Gemini CLI, Claude Code y Codex. Todo se puede hacer desde Colab.
- **Recursos opcionales:** `recursos_opcionales.md`.

## Evaluación

La rúbrica completa está en [`rubrica.md`](rubrica.md). En resumen: la autoevaluación de cada una de las sesiones 1, 2 y 3 vale un 10%, la actividad principal, que es el reto, un 60%, y los debates otro 10%. Todo es individual. El hito de la semana 2 no tiene nota propia. Si no superáis el reto, hay un [nano-reto de recuperación](nano_reto.md) con nota máxima de 7.

Usar IA no solo está permitido: es el objetivo del módulo. Se evalúa que sepáis especificar, dirigir, comprobar y explicar lo que habéis construido.
