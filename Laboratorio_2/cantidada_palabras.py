# realize un programa que compare entre dos palabras la cantidad de letras
#que posee y determine cual es mayor 

palabra_1 = str(input("Ingrese la primera palabra: "))
palabra_2 = str(input("Ingrese la segunda palabra: "))

len_palabra1 = len(palabra_1)
len_palabra2 = len (palabra_2)

if (len_palabra1 > len_palabra2): 
    print ("posee mayor cantidad:", palabra_1) 

elif (len_palabra1  < len_palabra2): 
    print("posee mayor cantidad:", palabra_2) 


if len(palabra_1)>= 3 and len(palabra_2)>= 3:
    letra_1 = palabra_1 [2]
    letra_2 = palabra_2 [2]

    if letra_1 > letra_2:
        print ("La letra mayor es:", letra_1)
    elif letra_2> letra_1:
        print("La letra mayor es:",letra_2)
    else:
        print ("tienen menos de tres letras")

