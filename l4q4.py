'''
    4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
'''
vogais = ['a','e','i','o','u']
lista_de_caracteres = []
for i in range(10):
    lista_de_caracteres.append(input())

for caracter in lista_de_caracteres:
    if caracter not in vogais:
        print(caracter, end=' ')

print()