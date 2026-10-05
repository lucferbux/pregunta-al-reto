# Rúbrica del reto

**Fundamentos de programación (Python para IA)** · Máster en Inteligencia Artificial · OBS Business School

Esta rúbrica es el contrato de calidad del reto: la tenéis desde el primer día para saber exactamente qué se espera en cada entrega.

## Cómo se calcula la nota

| Actividad | Qué es | Tipo | Peso en la nota final |
|---|---|---|---|
| Actividad sesión 1 | Autoevaluación: test de 8 preguntas en Blackboard | Individual | 10% |
| Actividad sesión 2 | Autoevaluación: test de 8 preguntas en Blackboard | Individual | 10% |
| Actividad sesión 3 | Autoevaluación: test de 8 preguntas en Blackboard | Individual | 10% |
| Actividad sesión 4 · **actividad principal** | El reto: app desplegada, proceso con IA, prueba y pitch escrito | Individual | 60% |
| Debates | Participación en el debate semanal del foro | Individual | 10% |

## Plazos

Las sesiones en directo son el 07/10, el 14/10, el 21/10 y el 28/10/2026 a las 19:00. Os recomiendo hacer cada autoevaluación la semana de su sesión, antes de la siguiente (la de la sesión 1 antes del 13/10/2026, la de la sesión 2 antes del 20/10/2026 y la de la sesión 3 antes del 27/10/2026), y subir el hito de la semana 2 como tarde el 20/10/2026, antes de la sesión 3, porque así os llega el feedback a tiempo. Aun así, entregar al final no penaliza, porque todas las actividades cierran el 02/11/2026. Es el primer módulo y hay quien se incorpora tarde, así que nadie pierde nota por eso, aunque quien sigue el ritmo semanal llega al final con mucho menos agobio.

## El hito de la semana 2

El **hito de la semana 2** es la foto de vuestro reto a mitad de camino, y cabe en una ficha de cinco líneas que publicáis en el debate Hito de la semana 2: el problema, el usuario, qué hará la app, la pieza de IA y el enlace a la versión 0 desplegada. No tiene nota propia: la reviso y os devuelvo feedback en la sesión 3, y lo que contiene se evalúa después dentro de la actividad principal con los criterios de la rúbrica de abajo. Es vuestra oportunidad de saber cómo vais antes de que cuente.

Lo que miro en la ficha es muy concreto:

| Línea de la ficha | Está bien si |
|---|---|
| Problema | Es una frase y habla de un problema concreto, no de una tecnología |
| Usuario | Dice quién lo tiene, con el detalle suficiente para imaginárselo |
| Qué hará la app | Hay entre una y tres funcionalidades, y cada una se entiende sin explicación |
| Pieza de IA | Nombra una opción (API de Gemini, modelo de Hugging Face o RAG) y da un motivo |
| Enlace a la versión 0 | El enlace abre una app, aunque todavía no tenga IA |

## Rúbrica de la actividad principal

Cada criterio se valora en uno de estos niveles, que son los mismos de las competencias del módulo:

| No presentado | Básico | Intermedio | Avanzado | Experto |
|---|---|---|---|---|
| 0 | 4 | 6 | 8 | 10 |

La nota de la actividad principal (sobre 10) es la media ponderada de sus criterios. Todos son individuales: aunque os hayáis organizado en equipo, cada persona recibe la nota de lo que entrega ella. Entre paréntesis va el apartado del documento de entrega en el que se mira cada criterio. El apartado 8, las capturas, acompaña a varios: son la prueba visible de que la app funciona, de cómo habéis trabajado con la IA y de la prueba.

| Criterio | Peso | Básico | Intermedio | Avanzado | Experto |
|---|---|---|---|---|---|
| Problema y usuario (CE63015) (apartado 2) | 10% | Problema genérico, sin usuario concreto | Problema concreto y usuario identificado | Además explica cómo se resuelve hoy sin la app | Además acota qué parte resuelve la IA y qué queda fuera |
| Especificación y prompting (CE63011) (apartado 3) | 10% | Descripción vaga de la app | Especificación con funcionalidades, entradas y salidas | Especificación que otro asistente podría construir sin preguntar | Con casos límite, criterios de aceptación y prompts reutilizables |
| App desplegada y funcional (CE63015) (apartados 1 y 8) | 25% | Arranca pero falla en el uso normal | Funciona en el caso principal | Estable, con ejemplos y mensajes de error claros | Un usuario no técnico la usa sin ayuda |
| Integración de la IA (CE63011) (apartados 4 y 8) | 20% | La IA no aporta nada al problema | La IA resuelve una parte del problema | La elección de modelo, API o RAG está justificada | Además maneja cuotas y errores con mensajes claros |
| Proceso con IA y harness (CE63014) (apartados 5 y 8) | 15% | No hay registro del proceso | Registro de prompts | Registro de prompts y fichero de contexto (AGENTS.md o equivalente) | Además explica qué se delegó al agente y qué se revisó a mano, con ejemplos |
| Prueba y mejora (CE63015) (apartados 6 y 8) | 10% | Dice que la ha probado, sin detalle | Una prueba documentada, propia o de un compañero: qué se probó y qué pasó | Además un cambio concreto hecho a partir de la prueba | Además ha probado la app de un compañero y le ha dejado feedback útil en el debate |
| README y pitch escrito (apartado 7) | 10% | README incompleto y sin pitch | README completo con la plantilla | Además un pitch de cinco frases que explica el problema, la solución y lo aprendido | Además el pitch convence, con un dato o un ejemplo concreto que respalda el impacto |

**Reglas de la actividad principal:**

- Si la URL de vuestra app no funciona el día de la corrección, vuestra nota de la actividad principal tiene un máximo de 3 sobre 10. Comprobad el enlace en una ventana de incógnito antes de entregar.
- Si la clave de la API aparece en el código o en el repositorio, el criterio Integración de la IA queda en Básico.

## Nano-reto de recuperación

Para quien no supere el reto. Es individual, dura una semana y la nota máxima es 7. Detalle en [`nano_reto.md`](nano_reto.md).

| Criterio | Puntos |
|---|---|
| La app funciona y está desplegada (ruta A o B) | 4 |
| La IA está bien integrada y la clave está protegida | 1,5 |
| README con los prompts usados y una prueba documentada | 1,5 |

## Sobre el uso de IA

Usar IA no solo está permitido: es el objetivo del módulo. Lo que se evalúa es que sepáis especificar, dirigir, comprobar y explicar lo que habéis construido. Si en una entrega hay algo que no sabéis explicar, os pediré que lo profundicéis en la siguiente.
