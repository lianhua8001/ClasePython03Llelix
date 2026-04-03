
# CODE:9
# IMPORTANTE: NO borrar los comentarios

'''
Alumno:
- Crear una una variable llamada nombre_completo_1
  para almacenar el nombre completo de su padre
  que debe ingresar por consola con la función input.
  Imprimir en consola el contenido de esta variable

- Crear una una variable llamada nombre_completo_2
  para almacenar el nombre completo de su madre que 
  debe ingresar por consola con la función input.
  Imprimir en consola el contenido de esta variable

- Crear una una variable llamada nombre
  para almacenar el nombre del hijo/a que usted
  debe ingresar por consola con la función input.
  Imprimir en consola el contenido de esta variable

- Cuando utilice la función split para dividir
  el nombre_completo_1, almacene los resultados
  en las variables llamadas nombre_1 y apellido_1
  Imprimir en consola el contenido de estas variables

  
  CONTINUE LA SOLUCIÓN DEL PROGRAMA AQUÍ:
- Cuando utilice la función split para dividir
  el nombre_completo_2, almacene los resultados
  en las variables llamadas nombre_2 y apellido_2
  Imprimir en consola el contenido de estas variables

- Crear una una variable llamada hijo
  para almacenar el nombre del hijo/a contenido en
  la variable nombre sumando/concatenando
  los apellidos almaecnados en apellido_1 y apellido_2
  Imprimir en consola el contenido de esta variable

  AL FINAL DEBE APARECER EL NOMBRE DEL HIJO CON EL APELLIDO 
  DEL PADRE Y DE LA MADRE.

'''


nombre_completo_1=str(input("Introduzca el nombre y apellido de su padre:"))
print (nombre_completo_1)

nombre_completo_2=str(input("Introduzca el nombre y apellido de su madre:"))
print (nombre_completo_2)

nombre=str(input("Introduce tu nombre:"))
print(nombre)

padre=nombre_completo_1.split() 
nombre_1=padre[0]
apellido_1=padre[1]
print(nombre_1, apellido_1)

# Empezar aquí la resolución del ejercicio

madre=nombre_completo_2.split() 
nombre_2=madre[0]
apellido_2=madre[1]
print(nombre_2, apellido_2)

 
nombre_sumado =  apellido_1+ " "+ apellido_2
hijo = nombre+ " "+ nombre_sumado
print ("El nombre del hijo es:", hijo)
