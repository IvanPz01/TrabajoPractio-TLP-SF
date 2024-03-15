import math 
list = []

numero = int(input("Digite um número: "))
for i in range(1, numero+1):
    list.append(i)

resultado = math.factorial(numero)
print(f"O fatorial de {numero} es {resultado}")