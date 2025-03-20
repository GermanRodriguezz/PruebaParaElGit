import random
import string
import sys
digitos = string.digits
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

questions_to_ask = random.choices(list(zip(questions, answers, correct_answers_index)), k=3) # ESTO GENERA UNA LISTA DE TUPLAS    

# DONDE LAS TUPLAS QUE ESTAN DENTRO DE LAS LISTAS CONTIENEN LAS OPCIONES DE LAS PREGUNTAS,LAS RESPUESTAS Y LOS INDICES
# LA TUPLA 1 CONTIENE A LA PREGUNTA, CON SU RESPUESTA Y EL INDICE DE LA RESPUESTA CORRECTA
# LA TUPLA 2 HACE LO MISMO

# El usuario deberá contestar 3 preguntas
for  preguntas,respuestas,index_correct in questions_to_ask :
    # Se selecciona una pregunta aleatoria
    #question_index = random.randint(0, len(questions_to_ask) - 1)
    # Se muestra la pregunta y las respuestas posibles
    print(preguntas)
    for i, respuesta in enumerate(respuestas):
        print(f"{i + 1}. {respuesta}")
    # El usuario tiene 2 intentos para responder  correctamente
    for intento in range(2):
        user_answer = (input("Respuesta: "))
        if user_answer in digitos :
            user_answer = int(user_answer)-1
            if (user_answer) == index_correct:
            # Se verifica si la respuesta es correcta
                print("¡Correcto!")
                break
            elif (user_answer) > 3:
                print('Respuesta invalida, no esta en el rango de respuestas!')
                sys.exit(1) 
        else :
            print('Se ingreso un string')
            sys.exit(1)
    else:
# Si el usuario no responde correctamente después de  2 intentos,
# se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(respuestas[index_correct])
# Se imprime un blanco al final de la pregunta
print()