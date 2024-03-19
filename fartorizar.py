import math 
list = []
numero = int(input("Digite um número: "))
def factorial(numero):
        for i in range(1, numero+1):
            list.append(i)
            resultado = math.factorial(numero)
        return resultado

resultado_final = factorial(numero)

print(f"El fatorial de {numero} es {resultado_final}")