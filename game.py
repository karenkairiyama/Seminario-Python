import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]


# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de intentos permitidos
#max_attempts = 10
#Cambie la variable max_attempts a max_failures para reflejar que está contando el número máximo de fallos permitidos en lugar de intentos.
# Numero de fallos permitidos
max_failures = 10

# Lista para almacenar las letras adivinadas
guessed_letters = []


print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")


word_displayed = "_" * len(secret_word)
# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")


# Agregué un contador cant_fallos para rastrear la cantidad de fallos del jugador
cant_fallos = 0
#for i in range(max_attempts):
#Modifiqué el bucle for para un bucle while True, lo que permite que el bucle se ejecute indefinidamente hasta que se cumpla una condición de salida.
while True:
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()

    #verificar que lo ingresado por el usuario sea una sola letra

    if len(letter) !=1 or not letter.isalpha():
        #si no es una letra valida
        print("Por favor, ingresa una sola letra valida.")
    else:
        #si la longitud es 1 y es una letra
        # Verificar si la letra ya ha sido adivinada
        if letter in guessed_letters:
            print("Ya has intentado con esa letra. Intenta con otra.")
            continue
        
        # Agregar la letra a la lista de letras adivinadas
        guessed_letters.append(letter)
        # Verificar si la letra está en la palabra secreta
        if letter in secret_word:
            print("¡Bien hecho! La letra está en la palabra.")
        else:
            print("Lo siento, la letra no está en la palabra.")
            # Si falló con la letra se incrementa la cantidad de fallos
            cant_fallos += 1
        # Mostrar la palabra parcialmente adivinada
        letters = []
        for letter in secret_word:
            if letter in guessed_letters:
                letters.append(letter)
            else:
                letters.append("_")
        word_displayed = "".join(letters)
        print(f"Palabra: {word_displayed}")

        # Verificar si se ha adivinado la palabra completa
        if word_displayed == secret_word:
            print(f"¡Felicidades! Has adivinado la palabra secreta:{secret_word}")
            break
        elif cant_fallos == max_failures:
            """Agregué una condición dentro del bucle while para verificar si el jugador ha alcanzado el número máximo de fallos permitidos (cant_fallos == max_failures). 
            Si se alcanza este límite, se imprime un mensaje y se revela la palabra secreta"""
            print(f"¡Oh no! Has agotado tus {max_failures} intentos.")
            print(f"La palabra secreta era: {secret_word}")
            break
"""else:
    print(f"¡Oh no! Has agotado tus {max_failures} intentos.")
    print(f"La palabra secreta era: {secret_word}")"""