#Problema 2  / 9 ptos x4 pruebas / 36 puntos
#Concatenación de listas o tuplas
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios elementos y los entregue de manera inversa
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 90 hola jiji 77
#La salida debe ser
#         (77, 'jiji', 'hola', 90, 20)
t = input()
tupla =tuple(t.split())
tupla_invertida = tuple(reversed(tupla))
tupla_invertida2 =()
for elemento in tupla_invertida:
    elemento = elemento.strip()
    if elemento.isdigit():
        tupla_invertida2 += (int(elemento),)
    else:
        tupla_invertida2 += (elemento,)
print(tupla_invertida2)
