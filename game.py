import random

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo", "inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)

# Número máximo de intentos permitidos
max_failures = 10

# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

# Función para mostrar la palabra parcialmente adivinada según el nivel de dificultad
def mostrar_palabra(nivel):
    if nivel == "1":
        return "".join([letter if letter in "aeiou" else "_" for letter in secret_word])
    elif nivel == "2":
        return secret_word[0] + "_" * (len(secret_word) - 2) + secret_word[-1]
    elif nivel == "3":
        return "_" * len(secret_word)

# Preguntar al usuario el nivel de dificultad
dificultad = input("Selecciona el nivel de dificultad (1: Fácil, 2: Medio, 3: Difícil): ")

# Mostrar la palabra parcialmente adivinada según el nivel de dificultad seleccionado
word_displayed = mostrar_palabra(dificultad)
print(f"Palabra: {word_displayed}")

# Agregué un contador cant_fallos para rastrear la cantidad de fallos del jugador
cant_fallos = 0

# Bucle principal del juego
while True:
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()

    # Verificar que lo ingresado por el usuario sea una sola letra
    if len(letter) != 1 or not letter.isalpha():
        # Si no es una letra válida
        print("Por favor, ingresa una sola letra válida.")
        continue
    
    # Si la letra ingresada es válida
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
    for displayed_letter, secret_letter in zip(word_displayed, secret_word):
        if secret_letter in guessed_letters:
            letters.append(secret_letter)
        else:
            letters.append(displayed_letter)
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
    elif cant_fallos == max_failures:
        # Si el jugador ha agotado todos los intentos sin adivinar la palabra
        print(f"¡Oh no! Has agotado tus {max_failures} intentos.")
        print(f"La palabra secreta era: {secret_word}")
        break

