#Script para la creacion de posibles usuarios

nombres= ["Paulo Gondra","Alfredo vasquez"]
posiblesnombres=[]
for nombre in nombres:
    splitnombre=nombre.split()
    #primera letra nombre + apellido 
    opcion1=splitnombre[0]+splitnombre[1]
    posiblesnombres.append(opcion1.lower())
    #primera letra . apellido
    opcion2=splitnombre[0][0]+"."+splitnombre[1]
    posiblesnombres.append(opcion2.lower())
    #nombreapellido sin espacios
    opcion3=splitnombre[0]+splitnombre[1]
    posiblesnombres.append(opcion3.lower())
    #nombre+primeraletraapellido
    opcion4=splitnombre[0]+splitnombre[1][0]
    posiblesnombres.append(opcion4.lower())
    #nombre.primeraletraapellido
    opcion5=splitnombre[0]+"."+splitnombre[1][0]
    posiblesnombres.append(opcion5.lower())

list_en_texto=""
for i in posiblesnombres:
    list_en_texto+=i + "\n"

print(list_en_texto)
