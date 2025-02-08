import random
import string

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
