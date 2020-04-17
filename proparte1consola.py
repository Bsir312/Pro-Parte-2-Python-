import os
nombres = []
for item in os.listdir("C:\\Users\\Miguel\\Pictures\\Imagenes\\imagen1.png"):
    if item[-4:] == ".png":
        nombres.append(item)

print("listado de todos los nombres",nombres)
print("Nombre Original",nombres[0:4])
os.rename("imagen1.png","ejemplo_1.png")
print ("renombrado exitosamente")
print(item)