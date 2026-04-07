#Programa que calcule la temperatura y ayude a determinar la minima y la media 

temperatura_1 = float(input("Ingrese la temperatura: "))
temperatura_2 = float(input("Ingrese la temperatura: "))
temperatura_3 = float(input("Ingrese la temperatura:"))

#condicional para la conocer la temperatura media

if (temperatura_1 > temperatura_2) and (temperatura_1 > temperatura_3):
    temperatura_max = temperatura_1
elif(temperatura_2 > temperatura_1) and (temperatura_2 > temperatura_3):
    temperatura_max = temperatura_2
else:
    temperatura_max = temperatura_3
print ("La temperatura Maxima es: ", temperatura_max)


#condicional para conocer la temperatura minima 

if (temperatura_1 < temperatura_2) and (temperatura_1 < temperatura_3):
    temperatura_min = temperatura_1
elif(temperatura_2 < temperatura_1) and (temperatura_2 < temperatura_3):
    temperatura_min = temperatura_2
else:
    temperatura_min = temperatura_3
print ("La temperatura Minima es:" ,temperatura_min)

#operacion para conocer la media de las temperaturas 
temperatura_media  = (temperatura_1 + temperatura_2 + temperatura_3) - temperatura_max - temperatura_min
   
print(f"La temperatura media es: {temperatura_media}")
