# CODE:7
# IMPORTANTE: NO borrar los comentarios

'''
Alumno:
- Crear una una variable llamada nombre_completo
  para almacenar el nombre completo que usted
  debe ingresar por consola con la función input.
  Recuerde en este caso utilizar el input junto a str.

- Crear una una variable llamada identificacion
  para almacenar el documento de identificación que usted
  debe ingresar por consola con la función input.
  Recuerde en este caso utilizar el input junto a str.

- Crear una una variable llamada edad
  para almacenar la edad que usted
  debe ingresar por consola con la función input.
  Recuerde en este caso utilizar el input junto a int.

- Crear una una variable llamada altura
  para almacenar la altura que usted
  debe ingresar por consola con la función input.
  Recuerde en este caso utilizar el input junto a float.

'''

print('Sistema de ingreso de datos')
# Empezar aquí la resolución del ejercicio
nombre = str(input("Ingrese su nombre:"))
apellido = str(input("Ingrese su apellido:"))

nombre_completo = nombre +" "+ apellido

identificacion = str(input("Ingrese su cédula:"))

edad = int(input("Ingrese su edad:"))

altura = float(input("Ingrese su altura:"))

print("Sus datos de identidad son:")
print ("Nombre:", nombre_completo)
print ("Cédula:",identificacion)
print ("Edad:", edad)
print ("Altura:", altura)
