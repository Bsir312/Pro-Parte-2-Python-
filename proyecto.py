
import json
import os
os.system("clear")   #El proyecto Se trabajo en linux.....
print("gracias por preferirnos")

base_de_datos = []

for i in range(3):
  diccionario = {}

  tipo = int(input("""
  1. motocicletas
  2. automovil
  3. camioneta
  INGRESE TIPO DE VEICULO: """))
  os.system("clear")

  while tipo>4:
    tipo = int(input("""
  1. motocicleta
  2. automovil
  3. camioneta
  INGRESE TIPO DE VEICULO: """))
    os.system("clear")

  precio = ""
  if tipo==1:
    precio=25
  elif tipo==2:
    precio=  30
  elif tipo==3:
    precio=50 
  else:
    print("error, el numero no existe")    

  if tipo==1:
    tipo="motocicleta"
  elif tipo==2:
    tipo="automovil"  
  elif tipo==3:
    tipo="camioneta"
  else:
    print("error")       

  cliente = int(input("""INGRESE TIPO DE CLIENTE, 
  1.ESTANDAR  
  2.MIEMBRO: """))
  os.system("clear")

  while cliente>2:
    cliente = int(input("""INGRESE TIPO DE CLIENTE, 
  1.ESTANDAR  
  2.MIEMBRO: """))
    os.system("clear")
    

  dia_semana = int(input("""INGRESE EL DIA:
  1.lunes a viernes
  2.sabado o domingo """))  
  os.system("clear")

  while dia_semana>2:
    dia_semana = int(input("""INGRESE EL DIA:
  1.lunes a viernes
  2.sabado o domingo """)) 

    os.system("clear")
  miembro=""
  if cliente == 2 and dia_semana ==1:
    miembro=(precio)*(0.20)  
  elif cliente==1 and dia_semana==1:
    miembro=(precio)*(0.10)
  elif cliente==1 and dia_semana==2:
    miembro=0
  elif cliente==2 and dia_semana==2:
    miembro=(precio)*(0.10)
  else:
    miembro=precio

  if cliente == 1:
    cliente = "ESTANDAR"
  else:
    cliente = "MIEMBRO" 
  descuento = miembro
  total =(precio)-(miembro)

  if dia_semana==1:
    dia_semana= "true"
  else:
    dia_semana="false"  

  diccionario["tipo"]=tipo
  diccionario["precio"]=precio
  diccionario["cliente"]=cliente
  diccionario["fin de semana"]=dia_semana
  diccionario["descuento"]=descuento
  diccionario["total"]=total
  base_de_datos.append(diccionario)

print("descuento: ",diccionario ["descuento"])
print("total: ", diccionario["total"])


print(base_de_datos)

for element in base_de_datos:
  print(element)

with open("base_de_datos", "w") as archivo:
  json.dump(base_de_datos, archivo)
  print("archivo exportado")