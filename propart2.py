
import os
import json
base_de_datos=[]

while True:
    tipo={}

    
    vehiculo=input("Seleccione el tipo de vehiculo: \n"
    "1.Motocicleta\n" "2.Automovil\n" "3.Camioneta\n" "4.Leer Archivo .JSON\n" "5.Salir\n4" )
    if vehiculo=='1':
        vehiculo='Motocicleta'
        precio=15.00
        os.system("cls")
        print("=================================")
        print("El tipo de vehiculo es:",vehiculo, ", Deberá pagar un monto de: ", precio)
        Cliente=input("seleccione el cliente que eres: \n" "1.Estandar\n" "2.Miembro\n")
        if Cliente=='1':
            Cliente='Estandar'
            print("Cliente: Estandar\n")
            Fin_de_Semana=input("Que día nos visita?: \n" "1.Lunes a Viernes\n" "2.Fines De Semana\n")
            while Fin_de_Semana!=3:
                if Fin_de_Semana=='1':
                   Fin_de_Semana=False
                   print('-------------------')
                   print("Fin se semana: ",Fin_de_Semana)
                   Descuento=(precio)*(0.10)
                   Total=precio-Descuento
                   #TotalM=Total1
                   print("El descuento es de: ", Descuento)
                   print ("El total a pagar es de: ", Total)
                   print('-------------------')
                   break
                elif Fin_de_Semana=='2':
                    Fin_de_Semana=True
                    print('-------------------')
                    print("Fin se semana: ",Fin_de_Semana)
                    print("El total a pagar es de: ", precio)
                    print('-------------------')
                    break
        elif Cliente=="2":
            Cliente='Miembro'
            print("Cliente: Miembro")
            Fin_de_Semana=input("Que día nos visita?: \n" "1.Lunes a Viernes\n" "2.Fines De Semana\n")
            while Fin_de_Semana!=3:
                if Fin_de_Semana=="1":
                    Fin_de_Semana=False
                    print('-------------------')
                    print("Fin se semana: ",Fin_de_Semana)
                    print("---------------------")
                    print("El total a pagar es de: ", precio)
                    print('-------------------')
                    break
                elif Fin_de_Semana=="2":
                    Fin_de_Semana=True
                    print("----------------------")
                    print("Fin se semana: " ,Fin_de_Semana)
                    Descuento=(precio)*(0.10)
                    Total=precio-Descuento
                    print("El descuento es de: ", Descuento)
                    print ("El total a pagar es de: ", Total)
                    print("----------------------")
                    break 
        else:
            print("Opcion invalida, favor seleccionar una opcion valida")
             
    elif vehiculo=="2":
        vehiculo="Automovil"
        precio=30.00
        os.system("cls")
        print("=================================")
        print("El tipo de vehiculo es:",vehiculo, ", Deberá pagar un monto de: ", precio)
        Cliente=input("seleccione el cliente que eres: \n" "1.Estandar\n" "2.Miembro\n")
        if Cliente=='1':
            Cliente='Estandar'
            print("Cliente: Estandar\n")
            Fin_de_Semana=input("Que día nos visita?: \n" "1.Lunes a Viernes\n" "2.Fines De Semana\n")
            while Fin_de_Semana!=3:
                if Fin_de_Semana=='1':
                   Fin_de_Semana=False
                   print('-------------------')
                   print("Fin se semana: ",Fin_de_Semana)
                   Descuento=(precio)*(0.10)
                   Total=precio-Descuento
                   print("El descuento es de: ", Descuento)
                   print ("El total a pagar es de: ", Total)
                   print('-------------------')
                   break
                elif Fin_de_Semana=='2':
                    Fin_de_Semana=True
                    print('-------------------')
                    print("Fin se semana: ",Fin_de_Semana)
                    print("El total a pagar es de: ", precio)
                    print('-------------------')
                    break
        elif Cliente=="2":
            Cliente='Miembro'
            print("Cliente: Miembro")
            Fin_de_Semana=input("Que día nos visita?: \n" "1.Lunes a Viernes\n" "2.Fines De Semana\n")
            while Fin_de_Semana!=3:
                if Fin_de_Semana=="1":
                    Fin_de_Semana=False
                    print('-------------------')
                    print("Fin se semana: ",Fin_de_Semana)
                    print("---------------------")
                    print("El total a pagar es de: ", precio)
                    print('-------------------')
                    break
                elif Fin_de_Semana=="2":
                    Fin_de_Semana=True
                    print("----------------------")
                    print("Fin se semana: " ,Fin_de_Semana)
                    Descuento=(precio)*(0.10)
                    Total=precio-Descuento
                    print("El descuento es de: ", Descuento)
                    print ("El total a pagar es de: ", Total)
                    print("----------------------")
                    break 
        else:
            print("Opcion invalida, favor seleccionar una opcion valida")

    elif vehiculo=="3":
        vehiculo='Camioneta'
        precio=50.00
        os.system("cls")
        print("=================================")
        print("El tipo de vehiculo es:",vehiculo, ", Deberá pagar un monto de: ", precio)
        Cliente=input("seleccione el cliente que eres: \n" "1.Estandar\n" "2.Miembro\n")
        if Cliente=='1':
            Cliente="Estandar"
            Cliente="Estandar"
            print("Cliente: Estandar\n")
            Fin_de_Semana=input("Que día nos visita?: \n" "1.Lunes a Viernes\n" "2.Fines De Semana\n")
            while Fin_de_Semana!=3:
                if Fin_de_Semana=='1':
                   Fin_de_Semana=False
                   print('-------------------')
                   print("Fin se semana: ",Fin_de_Semana)
                   Descuento=(precio)*(0.10)
                   TotalC=precio-Descuento
                   #TotalM=Total1
                   print("El descuento es de: ", Descuento)
                   print ("El total a pagar es de: ", Total)
                   print('-------------------')
                   break
                elif Fin_de_Semana=='2':
                    Fin_de_Semana=True
                    print('-------------------')
                    print("Fin se semana: ",Fin_de_Semana)
                    print("El total a pagar es de: ", precio)
                    print('-------------------')
                    break
        elif Cliente=="2":
            Cliente="Miembro"
            Cliente='Miembro'
            print("Cliente: Miembro")
            Fin_de_Semana=input("Que día nos visita?: \n" "1.Lunes a Viernes\n" "2.Fines De Semana\n")
            while Fin_de_Semana!=3:
                if Fin_de_Semana=="1":
                    Fin_de_Semana=False
                    print('-------------------')
                    print("Fin se semana: ",Fin_de_Semana)
                    print("---------------------")
                    print("El total a pagar es de: ", precio)
                    print('-------------------')
                    break
                elif Fin_de_Semana=="2":
                    Fin_de_Semana=True
                    print("----------------------")
                    print("Fin se semana: " ,Fin_de_Semana)
                    Descuento=(precio)*(0.10)
                    Total=precio-Descuento
                    print("El descuento es de: ", Descuento)
                    print ("El total a pagar es de: ", Total)
                    print("----------------------")
                    break 
        
    elif vehiculo=="4":

        with open('base_de_datos.json', 'r') as archivo:

            base_de_datos = json.load(archivo) 
            print("Archivo obtenido con exito") 
        print(base_de_datos)
        break
    elif vehiculo=='5':
        print("***Feliz Dia***")
        break
    else:
        print("Opcion invalida")
        os.system('cls')

    tipo["vehiculo"]=vehiculo
    tipo["precio"]=precio
    tipo["Cliente"]=Cliente
    tipo["Fin de Semana"]=Fin_de_Semana
    tipo["Descuento"]=Descuento
    tipo["Total"]=Total

    base_de_datos.append(tipo)
print(base_de_datos)


for element in base_de_datos:
  print(element)

with open('base_de_datos.json', 'w') as archivo: # la w significa que vamos a escribir hacía el archivo ('base_de_datos.json')
    json.dump(base_de_datos, archivo) #dump=(tirar, base de datos dentro de archivo)
    print("Archivo exportado") 

  