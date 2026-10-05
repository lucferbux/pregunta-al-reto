# Especificación · Pregunta al reto

Esta es la especificación real con la que un agente construyó la app, escrita con la misma plantilla que se pide al alumnado.

## 1. Problema y usuario

- **Quién tiene el problema:** los 60 alumnos del módulo, durante las cuatro semanas del reto.
- **Cómo lo resuelve hoy:** preguntando en el foro y esperando respuesta, o releyendo tres documentos para encontrar una fecha o un requisito.
- **Qué le molesta:** las mismas cinco dudas se repiten cada edición, casi siempre de noche y casi siempre el día antes de entregar.
- **Qué parte resuelve la IA:** encontrar el fragmento que responde a la duda y redactarlo en dos frases, diciendo de dónde sale. Lo que no está escrito en los documentos se queda fuera y sigue yendo al foro.

## 2. Qué hace el producto

1. Responde una duda sobre el reto con los documentos del curso.
2. Enseña de qué documento y de qué sección sale la respuesta.
3. Dice que no lo sabe cuando la respuesta no está en los documentos.

## 3. Entradas y salidas

| El usuario da | La app devuelve | Ejemplo |
|---|---|---|
| Una duda escrita con sus palabras | Respuesta de dos a cuatro frases más las fuentes | "¿Qué entrego en el hito de la semana 2?" → las cinco líneas de la ficha y de dónde sale |

## 4. La pieza de IA

RAG sobre los tres documentos del reto: embeddings con `gemini-embedding-001`, similitud coseno con numpy y redacción con `gemini-3.8-flash`. Sin Chroma, porque Streamlit Cloud trae un sqlite más viejo del que necesita y aquí no hace falta.

## 5. Flujo del usuario

1. Entra y ve tres preguntas de ejemplo en la barra lateral.
2. Pregunta lo suyo.
3. Recibe la respuesta y puede desplegar de dónde sale.

## 6. Restricciones

Coste cero con la capa gratuita, la clave en los secretos de Streamlit Cloud, ningún dato personal, y lenguaje sencillo, que la van a usar a las dos de la mañana.

## 7. Criterios de aceptación

| Entrada | Resultado esperado |
|---|---|
| "¿Tengo que buscar usuarios para probar mi app?" | Dice que no, que la prueba es entre compañeros o propia, y cita el enunciado |
| "¿Puedo desplegar en Hugging Face con una cuenta nueva?" | Explica el límite de los 30 días y manda a la ruta A |
| "¿Qué nota saco si entrego tarde?" | Dice que no lo encuentra en los documentos y manda al foro |
| Se acaba la cuota de la API | Mensaje claro, la app no se rompe |

## 8. Fuera de alcance

Corregir entregas, dar notas, hablar con Blackboard y guardar las conversaciones.

## 9. Despliegue

Ruta A, Streamlit Community Cloud, desde un repositorio público de GitHub. La construyo yo, y la enseño en las sesiones 1 y 4.
