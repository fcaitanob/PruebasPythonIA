"""
Ejercicio 17 (*)
Básicos de listas
Crear una lista llamada lista1 con los elementos 1, 2, 3, 4 y 5
Cambiar el valor 1 por el 8
Agregar al final los números 4, 5 y 8
Cambiar los valores desde el lugar 3 hasta el lugar 6 por el número 2
Cambiar los valores de los lugares 2, 3 y 4, empezando por el final por 5, 6 y 7
Crear una lista igual a la anterior pero en reversa que se llamara lista2
Obtener una lista que concatene la lista inicial con la segunda (llamada lista3)

"""

#Crear una lista llamada lista1 con los elementos 1, 2, 3, 4 y 5
lista1 = [1,2,3,4,5,1,25, 1]
print("La lista1 original es: " + str(lista1))


#Cambiar el valor 1 por el 8
lista1[0] = 8
print("Lista1 luego de susitiir el 1 x el 8: " + str(lista1))

#Cambiar el valor 1 por el 8 v2
i = lista1.index(1, 0, lista1.__sizeof__())
print("Indice de lista1 donde está el primer 1: " + str(i))
i=0
for x in lista1:
    if x == 1:
        lista1[i] = 8
    i=i+1
print("Lista1 luego de sustituir los unos por ochos: " + str(lista1))

#Agregar al final los números 4, 5 y 8
lista1.append(4)
lista1.append(5)
lista1.append(8)
print("Lista1 luego de agregados: " + str(lista1))

#Cambiar los valores desde el lugar 3 hasta el lugar 6 por el número 2
i=0
for i in range(3, 6+1):
    lista1[i] = 99
print("Lista1 luego de sustituciones: " + str(lista1))
    

#Cambiar los valores de los lugares 2, 3 y 4, empezando por el final por 5, 6 y 7
i=len(lista1)
j=lista1.__len__()
print(i)
print(j)
while j>=0:
    if j==4:
        lista1[j]=7
    if j==3:
        lista1[j]=6
    if j==2:
        lista1[j]=5
    j=j-1
print("Lista con cambios en reversa 5, 6 y 7: " + lista1.__str__())


#Crear una lista igual a la anterior pero en reversa que se llamara lista2
j=len(lista1)-1
lista2=[]
while j>=0:
    lista2.append(lista1[j])
    j= j-1
print("Lista revertida: " + str(lista2))




#Obtener una lista que concatene la lista inicial con la segunda (llamada lista3)
lista3=[]
for x in lista1:
    lista3.append(x)
for x in lista2:
    lista3.append(x)
print("Lista 3 concatenando lista1 y lista 2: " + str(lista3))    



    
        
