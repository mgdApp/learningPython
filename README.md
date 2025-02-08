# passwords.py
Crea contraseñas aleatorias en Python (no es la opción más segura).

# Syntax

1. Importar módulos:
    - `import random`: Importa el módulo random, que contiene funciones para generar números y seleccionar elementos de forma aleatoria.
    - `import string`: Importa el módulo string, que provee constantes y utilidades relacionadas con cadenas de caracteres.

2. Definir cada grupo de caracteres:
    - `letras = string.ascii_letters`: Cadena/string que contiene todas las letras mayúsculas y minúsculas que se guarda en la variable `letras`.
    - `digitos = string.digits`: Cadena/string que contiene los dígitos del 0 al 9 que se guarda en la variable `digitos`.
    - `simbolos = string.punctuation`: Cadena/string que contiene símbolos de puntuación que se guarda en la variable `simbolos`.

3. Solicitar la longitud de la contraseña:
    - `longitud = int(input("Ingresa la longitud de la contraseña: ")):` Guarda la longitud de la contraseña elegida por el usuario.
  
      - `input("...")`: Muestra un mensaje al usuario y espera que ingreses un valor (será de tipo cadena/string).
      - `int(...)`: Convierte el string obtenido en un número entero.

4. Seleccionar al menos un carácter de cada grupo:
    - `contrasena = [ random.choice(letras), random.choice(digitos), random.choice(simbolos) ]`: Crea una lista llamada `contrasena` que contiene un cáracter escogido de manera aleatoria de `letras`, `digitos` y `simbolos`.
  
5. Caracteres aleatorios adicionales:
    - `todos = letras + digitos + simbolos`: Concatena los strings `letras`, `digitos` y `simbolos` en la variable `todos`.
    - `for _ in range(longitud - 3): contrasena.append(random.choice(todos))`: El ciclo `for` se ejecuta `longitud - 3` veces (ya que ya se han añadido 3 caracteres iniciales) y en cada iteración se selecciona y agrega de manera aleatoria un carácter de la variable `todos` a la lista `contrasena`.
      - La variable `_` se usa convencionalmente cuando el valor de iteración no es necesario.
  
6. Mezclar los caracteres para evitar un orden predecible:
    - `random.shuffle(contrasena)`: Reorganiza aleatoriamente todos los elementos de la lista `contrasena`.
    
7. Convertir la lista en una cadena:
    - `contrasena = ''.join(contrasena)`: Se usa el método `join` para concatenar todos los caracteres de la lista en una solo string, asignándolo nuevamente a `contrasena`.
      
8. Mostrar la contraseña generada:
    - `print("Tu contraseña generada es:", contrasena)`: Se imprime la contraseña final en la consola.
