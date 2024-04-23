# Tarea 3.1 Ejercicios AFN
## Realizar los ejercicios acordados en clase de la página 49, del libro Teoría de la computación de Carrión Viramontes
### a) El lenguaje donde toda cadena tiene exactamente dos 'b's:

La expresión regular `(a^*ba^*ba^*)` describe cadenas que tienen exactamente dos 'b's. Aquí está su desglose:

- `a^*`: Esto representa cero o más ocurrencias de 'a'.
- `b`: Esto representa una sola 'b'.
- `a^*`: Esto representa cero o más ocurrencias de 'a'.
- `b`: Esto representa otra única 'b'.
- `a^*`: Esto representa cero o más ocurrencias de 'a'.

Esto garantiza que haya exactamente dos 'b's en cualquier cadena que coincida con esta expresión regular, con cualquier cantidad de 'a's antes, entre y después de las 'b's.

### b) El lenguaje de las cadenas no vacías, donde toda 'a' está entre dos 'b's:

La expresión regular `(b^+a(b^+a)^*b^+)` describe cadenas no vacías donde cada 'a' está entre dos 'b's. Aquí está su desglose:

- `b^+`: Esto representa una o más ocurrencias de 'b'.
- `a`: Esto representa una sola 'a'.
- `(b^+a)^*`: Esto representa cero o más ocurrencias de una secuencia que comienza con una o más 'b's, seguida de una 'a'.
- `b^+`: Esto representa otra secuencia de una o más ocurrencias de 'b'.

Esto asegura que cada 'a' esté entre dos 'b's en cualquier cadena que coincida con esta expresión regular, y que la cadena no sea vacía.

### c) El lenguaje donde toda cadena contiene el sufijo 'aba':

La expresión regular `(a^*ba^*ba)` describe cadenas donde 'aba' aparece como sufijo. Aquí está su desglose:

- `a^*`: Esto representa cero o más ocurrencias de 'a'.
- `b`: Esto representa una sola 'b'.
- `a^*`: Esto representa cero o más ocurrencias de 'a'.
- `b`: Esto representa otra única 'b'.
- `a`: Esto representa una sola 'a'.

Esto asegura que 'aba' aparezca como sufijo en cualquier cadena que coincida con esta expresión regular.

### d) El lenguaje donde ninguna cadena contiene las subcadenas 'aa' ni 'bb':

La expresión regular `(a|b|^*)^*` describe cadenas sin las subcadenas 'aa' ni 'bb'. Aquí está su desglose:

- `(a|b|^*)`: Esto representa cualquier combinación de 'a's y 'b's, o una cadena vacía.
- `^*`: Esto representa cero o más ocurrencias de lo anterior.

Esto garantiza que ninguna cadena contenga las subcadenas 'aa' ni 'bb'.

### e) El lenguaje donde toda cadena contiene la subcadena 'baba':

La expresión regular `(a|b|^*)^*baba(a|b|^*)^*` describe cadenas que contienen la subcadena 'baba'. Aquí está su desglose:

- `(a|b|^*)^*`: Esto representa cero o más ocurrencias de cualquier combinación de 'a's y 'b's, o una cadena vacía.
- `baba`: Esto representa la subcadena 'baba'.
- `(a|b|^*)^*`: Esto representa cero o más ocurrencias de cualquier combinación de 'a's y 'b's, o una cadena vacía.

Esto asegura que cualquier cadena que coincida con esta expresión regular contenga la subcadena 'baba' en cualquier posición.

### f) El lenguaje donde toda cadena contiene por separado a las cadenas 'ab' y 'ba':

La expresión regular `((ab)|(ba))(a|b|^*)^*` describe cadenas que contienen tanto 'ab' como 'ba', seguido de cero o más ocurrencias de 'a's y 'b's. Aquí está su desglose:

- `((ab)|(ba))`: Esto representa la presencia de 'ab' o 'ba'.
- `(a|b|^*)^*`: Esto representa cero o más ocurrencias de cualquier combinación de 'a's y 'b's, o una cadena vacía.

Esto garantiza que cualquier cadena que coincida con esta expresión regular contenga tanto 'ab' como 'ba' en cualquier orden, seguido de cualquier combinación de 'a's y 'b's.

### g) Toda cadena es de longitud impar y contiene una cantidad par de 'a's:

La expresión regular `b^*(ab^*ab^*)^*` describe cadenas de longitud impar con una cantidad par de 'a's. Aquí está su desglose:

- `b^*`: Esto representa cero o más ocurrencias de 'b'.
- `(ab^*ab^*)^*`: Esto representa cero o más ocurrencias de una secuencia que comienza con 'a', seguida de cero o más ocurrencias de 'b', seguida nuevamente por 'a', y seguida de cero o más ocurrencias de 'b'.

Esto garantiza que cualquier cadena que coincida con esta expresión regular tenga una longitud impar y una cantidad par de 'a's.

##### Josue Ramirez Hernandez - 21200990
