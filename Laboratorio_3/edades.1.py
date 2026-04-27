# progama que pide total de la compra 

while True: 
    print ("Introduzca el total de su compra") 

    total_compra = float(input()) #acepta el total
    
    if total_compra >=20 and total_compra<=50:
        print ("Usted ganó un litro de soda")
   
    elif total_compra >50.01 and total_compra <=100:
        print ("Usted ganó dos litros de soda")
    else:
        print("Usted se ganó 4 litros de soda")

    break #si no se usa, provoca bug





