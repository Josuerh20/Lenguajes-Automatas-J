# Tarea 2.3

Esta tarea consiste en proporcionar expresiones regulares para validar contraseñas seguras y nombres de usuario según ciertos criterios específicos.

## Expresión Regular para Contraseñas Fuertes

La expresión regular para validar contraseñas fuertes asegura que una contraseña cumpla con los siguientes criterios:

- Al menos 1 minúscula
- Al menos 1 mayúscula
- Al menos 1 número
- Al menos 1 carácter especial
- Longitud mínima de 8 caracteres

Expresión regular:
` ^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$ `

## Expresión Regular para Nombres de Usuario

La expresión regular para validar nombres de usuario asegura que un nombre de usuario cumpla con los siguientes criterios:

- Longitud entre 3 y 16 caracteres
- Solo letras, números, guiones bajos y medios son permitidos

Expresión regular:
` ^[A-Za-z0-9_-]{3,16}$ `

--------
##### Josue Ramirez Hernandez 21200990

