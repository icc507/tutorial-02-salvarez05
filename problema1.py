#Problema 1  / 8 ptos x4 pruebas / 32 puntos
#Concatenación de listas o tuplas
#--------------------------------
#Confeccione un programa que lea 2 tuplas sean t1 y t2
#La salida debe ser una tupla en el orden t2 t1 t2
#---------------------------------
#Ejemplo de entrada:
#         20 90 hola
#		  mundo 44
#La salida debe ser
#         ('mundo', 44, 20, 90, 'hola', 'mundo', 44)
t = input()
t2= t.split()
tupla1=()
for elemento in t2:
    elemento = elemento.strip()
    if elemento.isdigit():
        tupla1 += (int(elemento),)
    else:
        tupla1 += (elemento,)
m = input()
m2 = m.split()
tupla2= ()
for elemento in m2:
    elemento = elemento.strip()
    if elemento.isdigit():
        tupla2 += (int(elemento),)
    else:
        tupla2 += (elemento,)
print(tupla2+tupla1+tupla2)
