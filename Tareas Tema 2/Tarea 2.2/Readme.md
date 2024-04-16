# Telegram Bot Josh
------
## Funcionamiento

1. **Inicio del bot:**
   - Este punto describe cómo el bot responde cuando lo inicias. Puedes explicar que el bot saluda cortésmente al usuario cuando se inicia con palabras como "hola", "hi", "hello" o "hey".
   - Expresión Regular: ` saludo_expresion_regular = re.compile(r"hello|hi|hey|hola", re.IGNORECASE) `
   - Captura de pantalla:
     -------
     ![evidencia](https://github.com/Josuerh20/Lenguajes-Automatas-J/blob/master/Tareas%20Tema%202/Tarea%202.2/IMG%20BOT/Img%20bot/BOT1.jpeg)

2. **Respuesta a "¿Cómo estás?":**
   - Aquí puedes explicar cómo el bot responde cuando el usuario pregunta cómo está. Puedes indicar que el bot responde con una pregunta similar o con un mensaje amigable.
   - - Expresión Regular: ` bien_expresion_regular = re.compile(r"bien|good", re.IGNORECASE)` ó `mal_expresion_regular = re.compile(r"mal|bad", re.IGNORECASE) `
   - Captura de pantalla:
      -------
     ![evidencia](https://github.com/Josuerh20/Lenguajes-Automatas-J/blob/master/Tareas%20Tema%202/Tarea%202.2/IMG%20BOT/Img%20bot/BOT2.jpeg)
3. **Solicitud de la hora:**
   - Este punto describe cómo el bot responde cuando el usuario solicita la hora actual. Puedes explicar que el bot devuelve la hora actual en formato de 24 horas.
   - - Expresión Regular: ` hora_expresion_regular = re.compile(r"hora|time", re.IGNORECASE) `
   - Captura de pantalla:
     -------
     ![evidencia](https://github.com/Josuerh20/Lenguajes-Automatas-J/blob/master/Tareas%20Tema%202/Tarea%202.2/IMG%20BOT/Img%20bot/BOT3.jpeg)

4. **Pedido de chiste:**
   - Aquí puedes explicar cómo el bot responde cuando el usuario solicita un chiste. Indica que el bot selecciona aleatoriamente un chiste de una lista y lo comparte con el usuario.
   - - Expresión Regular: ` chiste_expresion_regular = re.compile(r"chiste|broma|joke", re.IGNORECASE) `
   - Captura de pantalla:
     -------
     ![evidencia](https://github.com/Josuerh20/Lenguajes-Automatas-J/blob/master/Tareas%20Tema%202/Tarea%202.2/IMG%20BOT/Img%20bot/BOT4.jpeg)

5. **Solicitud de conversión de unidades:**
   - Este punto describe cómo el bot maneja las solicitudes de conversión de unidades de pulgadas a centímetros. Explica que el usuario puede enviar un mensaje que incluya la cantidad seguida de "pulgadas", y el bot responderá con el equivalente en centímetros.
   - - Expresión Regular: ` conversion_expresion_regular = re.compile(r"(\d+(?:\.\d+)?)\s*pulgadas", re.IGNORECASE `
   - Captura de pantalla:
    -------
     ![evidencia](https://github.com/Josuerh20/Lenguajes-Automatas-J/blob/master/Tareas%20Tema%202/Tarea%202.2/IMG%20BOT/Img%20bot/BOT5.jpeg)

#### Josue Ramirez hernandez - 21200990
