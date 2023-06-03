from random import randint

vetor = []
vetor_impar = []
vetor_resto_divisao = []

for indice in range(100):
    numeros_aleatorios = randint(1, 1000)
    vetor.append(numeros_aleatorios)

for num in vetor:
    if num % 2 != 0:
        vetor_impar.append(num)
    elif num % 2 == 0:
        restao_divisao_por_5 = num % 5
        vetor_resto_divisao.append(restao_divisao_por_5)


print("Vetor de números ímpares:")
print(vetor_impar)

print("Vetor de resto da divisão por 5 dos números pares:")
print(vetor_resto_divisao)