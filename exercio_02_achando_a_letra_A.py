frase = str(input('Digite uma palavra/frase: ')).strip()
cont = 0

for letra in frase:
    if letra == 'a':
        cont+=1

print('Na frase:'
    f'\n{frase} temos {cont} letras "a". ')