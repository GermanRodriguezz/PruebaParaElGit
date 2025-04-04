import random
import string
import sys
letras = string.ascii_letters
digitos = string.digits
puntaje = 0
# Preguntas para el juego
questions = [
"¿Qué función se usa para obtener la longitud de una  cadena en Python?",
"¿Cuál de las siguientes opciones es un número entero en  Python?",
"¿Cómo se solicita entrada del usuario en Python?",
"¿Cuál de las siguientes expresiones es un comentario  válido en Python?",
"¿Cuál es el operador de comparación para verificar si  dos valores son iguales?",]
# Respuestas posibles para cada pregunta, en el mismo orden  que las preguntas
answers = [
("size()", "len()", "length()", "count()"),
("3.14", "'42'", "10", "True"),
("input()", "scan()", "read()", "ask()"),
(
"// Esto es un comentario",
"/* Esto es un comentario */",
"-- Esto es un comentario",
"# Esto es un comentario",
),
("=", "==", "!=", "==="),]
# Índice de la respuesta correcta para cada pregunta, el el  mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
# El usuario deberá contestar 3 preguntas
for _ in range(3):
    # Se selecciona una pregunta aleatoria
    question_index = random.randint(0, len(questions) - 1)
    # Se muestra la pregunta y las respuestas posibles
    print(questions[question_index])
    for i, answer in enumerate(answers[question_index]):
        print(f"{i + 1}. {answer}")
    # El usuario tiene 2 intentos para responder  correctamente
    for intento in range(2):
        user_answer = (input("Respuesta: "))
        if user_answer in digitos :
            user_answer = int(user_answer)-1
            if (user_answer) == correct_answers_index[question_index]:
            # Se verifica si la respuesta es correcta
                print("¡Correcto!")
                puntaje += 1
                print('se sumo un punto!')
                break
            elif user_answer != correct_answers_index[question_index] or user_answer > 3 :
                print('Respuesta no correcta!')
                puntaje = puntaje - 0.5
                print('se desconto 0.5 puntos')
        else :
            print('Se ingreso un string')
            puntaje = puntaje - 0.5
            print('se desconto 0.5 puntos')
    else:
# Si el usuario no responde correctamente después de  2 intentos,
# se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(answers[question_index][correct_answers_index[question_index]])
# Se imprime un blanco al final de la pregunta
print(f'{puntaje} es el puntaje final del jugador/a')
print()