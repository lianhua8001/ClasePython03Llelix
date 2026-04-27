##Guardar mi nombre en una variable y mostrarlo en mayuscula
nombre = "Danna"
print (nombre.upper())

##Lista de numeros, que muestre mayor, menor y la suma
numero = [5,8,2,4,3]
print("el numero menor es:",min(numero))
print("el numero mayor es:",max(numero))
print("la suma es de:",sum(numero))


##bucle de impresion del 1 al 10
for i in range(1,11):
    print (i)

##nombre bonito, programa que imprima su nombre
nombre =str(input("Introduzca su nombre por consola:"))

print(nombre.upper())
print(nombre.lower())
print(nombre.capitalize())
cantidad_nombre = len (nombre)
print ("Su nombre tiene:",cantidad_nombre," letras")

##programa que determine si aprobó o no
nota1 =float(input("Introduzca la primera nota:"))
nota2 =float(input("Introduzca la segunda nota:"))
nota3 =float(input("Introduzca la tercera nota:"))

notas = [nota1,nota2,nota3]


promedio =round (sum(notas)/ len(notas),2 )

print("Promedio",promedio)
print("Mayor", max(notas))
print("Menor", min(notas))


if promedio>=3.0: 
    print("Apobó")
else:
    print("Reprobó")


## compra con descuento
total_de_compra= float(input("Ingrese el total de su compra:"))

if total_de_compra >=0 and total_de_compra<=20:
    print("usted no aplica a ningún descuento T-T")
elif total_de_compra >=20.01 and total_de_compra<=50:
    rebaja =total_de_compra*0.05
    descuento =total_de_compra - rebaja
    print("Su descuento es del 5%")
elif total_de_compra >=50.01 and total_de_compra<= 100:
    rebaja =total_de_compra*0.10
    descuento =total_de_compra - rebaja
    print("Su descuento es del 10%")
else:
    total_de_compra <= 100.1
    rebaja= total_de_compra*0.15
    descuento= total_de_compra-rebaja
    print("Felicidades su descuento es del 15%")

print(total_de_compra)
print(descuento)

##nombre y apellido
name =str(input("Introduzca su nombre:"))
lastName =str(input("Introduzca su apellido:")) 

full_name= name +" " + lastName

print(full_name.upper())
print(full_name.lower())
print(full_name.title())





