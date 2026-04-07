# Progama para calcular el promedio con numeros enteros y determine la nota

#Se solicita las notas al usuario mediante un mensaje en consola

print("Bienvenido, por favor ingrese sus notas:")
nota_1 = int(input("Ingrese la nota 1:"))
nota_2 = int(input("Ingrese la nota 2:"))
nota_3 = int(input("Ingrese la nota 3:"))

#se realiza la operacion para saber el promedio final
promedio = nota_1 + nota_2 + nota_3


#se realiza las condicionales requeridas

if promedio >= 90:
    print ("Su nota es, A")
elif promedio >= 80:
    print ("Su nota es, B")
elif promedio >= 70:
    print ("Su nota es, C")
elif promedio >=60:
    print ("Su nota es, D")
else:
    print ("Su nota es, F") 


    



