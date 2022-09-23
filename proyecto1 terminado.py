print("juego de trivia")
print(" digite solo respuestas concisas y en minuscula ")
print(" mediante este codigo se pude crear difentes cuestionarios o trivias solamente cambiando las preguntas y las respuestas")
print(" este codigo tiene como fin ayudar a los docentes a hacer mas facil su tarea de verificar las respuestas de los estudiantes")

#instrucciones de como crear el codigo

#1. crear las preguntas y digitar lo que se quiera preguntar 

pregunta1 = "en que año surgio la programacion? = "
pregunta2 = "cual fue el primer lenguaje de programacion? = "
pregunta3 = " quien invento el primer lenguaje de programacion? = "
pregunta4 = " en que tipo de datos se clasiican los datos? = "
preegunta5 = " que es c++? = "
pregunta6 = " quien es el  el informático más famoso en la actualidad? = "
pregunta7 = " quien creo microsoft? = "
pregunta8 = " cual es el lenguaje de programacion mas usado en el mundo? = "
pregunta9 =" en que año se creo el primer computador? "
pregunta10 = " indique lo que le falta para ser correcto....... print(helloworld )"

# 2. respuestas: hacemos lo mismo que con las preguntas pero colocamos las respuestas de las preguntas

respuesta1 = "1957"
respuesta2 = "fortran"
respuesta3 = "ada lovelace"
respuesta4 = "primitivos y derivados"
respuesta5 = "un lenguaje de programacion"
respuesta6 = "steve jobs"
respuesta7 = "bill gates"
respuesta8 = "python"
respuesta9 = "1943"
respuesta10 = "las comillas"

#3) para crear las entradas es necesario colocar un input ya que el codigo no seguira hasta que la persona pulse enter, luego usamos f que nos va a ayudar a poner el texto en la entrada
#entradas

entrada1 = input(f"pregunta 1 :{pregunta1}")
entrada2 = input(f"pregunta 2 :{pregunta2}")
entrada3 = input(f"pregunta 3 :{pregunta3}")
entrada4 = input(f"pregunta 4 :{pregunta4}")
entrada5 = input(f"pregunta 5 :{preegunta5}")
entrada6 = input(f"pregunta 6 :{pregunta6}")
entrada7 = input(f"pregunta 7 :{pregunta7}")
entrada8 = input(f"pregunta 8 :{pregunta8}")
entrada9 = input(f"pregunta 9 :{pregunta9}")
entrada10 = input(f"pregunta 10 :{pregunta10}")
#49 es necesario crear las variables de las entradas para poder crear el condicional if y ponenos todo como False 
#aciertos

acierto1 = False
acierto2 = False
acierto3 = False
acierto4 = False
acierto5 = False
acierto6 = False
acierto7 = False
acierto8 = False
acierto9 = False
acierto10 = False

#5) colocamos la condicion if para crear el condicional de que si la entrada 1 es igual a la respuesta es un valor verdadero
# tambien es necesario colocar un else que nos ayudara a que si el usuario coloca algo diferente a la rspuesta sea un valor incorrecto o falso
#condicion 1

if (entrada1 == respuesta1):
    acierto1 = True

else: acierto1 = False 

#condicion 2 

if (entrada2 == respuesta2):
    acierto2 = True

else: acierto2 = False 

#condicion 3

if (entrada3 == respuesta3):
    acierto3 = True

else: acierto3 = False 

#condicion 4 

if (entrada4 == respuesta4):
    acierto4 = True

else: acierto4 = False 

#condicion 5 

if (entrada5 == respuesta5):
    acierto5 = True

else: acierto5 = False 

#condicion 6 

if (entrada6 == respuesta6):
    acierto6 = True

else: acierto6 = False 

#condicion 7
if (entrada7 == respuesta7):
    acierto7 = True

else: acierto7 = False 

#condicion 8
if (entrada8 == respuesta8):
    acierto8 = True

else: acierto8 = False 

#condicion 9
if (entrada9 == respuesta9):
    acierto9 = True

else: acierto9 = False 

#condicion 10
if (entrada10 == respuesta10):
    acierto10 = True

else: acierto10 = False 

# es el carácter de salto de línea y se usa para indicar el fin de una línea de texto y el inicio de una línea nueva. 
print("/n")

#acierto y condiciones segunda parte 

# las variables de falso y verdadero no estan programdas porque no le hemos indicado que hacer con el TRUE y FALSE
#if 1 

# Aqui ya definimos que cuando sea TRUE escribir es correcta y si es FALSe escribir es incorrecta
if( acierto1 == True ):
    print("pregunta 1 es correcta")

else: print("pregunta 1 es incorrecta ")

#if 2 
if( acierto2 == True ):
    print("pregunta 2 es correcta")

else: print("pregunta 2 es incorrecta ")


#if 3
if( acierto3 == True ):
    print("pregunta 3 es correcta")

else: print("pregunta 3 es incorrecta ")


#if 4
if( acierto4 == True ):
    print("pregunta 4 es correcta")

else: print("pregunta 4 es incorrecta ")


#if 5
if( acierto5 == True ):
    print("pregunta 5 es correcta")

else: print("pregunta 5 es incorrecta ")


#if 6
if( acierto6 == True ):
    print("pregunta 6 es correcta")

else: print("pregunta 6 es incorrecta ")


#if 7
if( acierto7 == True ):
    print("pregunta 7 es correcta")

else: print("pregunta 7 es incorrecta ")


#if 8
if( acierto8 == True ):
    print("pregunta 8 es correcta")

else: print("pregunta 8 es incorrecta ")


#if 9
if( acierto9 == True ):
    print("pregunta 9 es correcta")

else: print("pregunta 9 es incorrecta ")


#if 10
if( acierto10 == True ):
    print("pregunta 10 es correcta")

else: print("pregunta 10 es incorrecta ")

