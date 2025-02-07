import random
import string

# import: Permite incluir módulos externos y acceder a sus funciones y variables.
# input(): Función que muestra un mensaje y espera la entrada del usuario. Devuelve una cadena.
# int(): Convierte una cadena o número a un entero.
# random.choice(seq): Devuelve un elemento aleatorio de la secuencia "seq".
# La expresión (random.choice(caracteres) for _ in range(longitud)) genera un iterador que produce un carácter aleatorio por cada iteración en range(longitud).
# ''.join(iterable): Une todos los elementos (que deben ser cadenas) de la variable iterable en una sola cadena. El separador es la cadena que precede a join (en este caso, una cadena vacía '').
# list.append(item): Añade item al final de la lista.
# random.shuffle(lista): Mezcla los elementos de la lista en orden aleatorio.
# La variable _ en bucles: Es una convención en Python para indicar que la variable de iteración no se usará.

def generar_contrasena_basica(longitud):
    """
    Genera una contraseña básica de la longitud especificada 
    utilizando letras, dígitos y símbolos.
    """
    caracteres = string.ascii_letters + string.digits + string.punctuation
    # Genera la contraseña usando una comprensión de generador
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def generar_contrasena_segura(longitud):
    """
    Genera una contraseña segura de la longitud especificada, 
    garantizando que incluya al menos una letra, un dígito y un símbolo.
    """
    if longitud < 3:
        # Se requiere al menos 3 caracteres para incluir una de cada categoría
        raise ValueError("La longitud debe ser al menos 3 para incluir letras, dígitos y símbolos.")
    
    # Definir cada grupo de caracteres
    letras = string.ascii_letters
    digitos = string.digits
    simbolos = string.punctuation

    # Incluir al menos un carácter de cada categoría
    contrasena = [
        random.choice(letras),
        random.choice(digitos),
        random.choice(simbolos)
    ]
    
    # Rellenar la contraseña con caracteres aleatorios del conjunto completo
    todos = letras + digitos + simbolos
    for _ in range(longitud - 3):
        contrasena.append(random.choice(todos))
    
    # Mezclar la lista para evitar un orden predecible
    random.shuffle(contrasena)
    return ''.join(contrasena)

def main():
    """
    Función principal que solicita la longitud de la contraseña,
    genera la contraseña utilizando una de las funciones definidas 
    y la muestra en pantalla.
    """
    try:
        longitud = int(input("Ingresa la longitud de la contraseña: "))
        # Puedes elegir entre generar una contraseña básica o segura:
        # contraseña = generar_contrasena_basica(longitud)
        contraseña = generar_contrasena_segura(longitud)
        print("Tu contraseña generada es:", contraseña)
    except ValueError as error:
        print("Error:", error)

if __name__ == "__main__":
    main()
