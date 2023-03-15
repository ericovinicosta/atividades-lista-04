#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

numeros = [] #lista vazia
tamanho = 10 #tamanho da lista

#entradas na lista
for n in range(tamanho):
    numeros.append(float(input('Digite o {}° numero: '.format(n + 1))))

#exibição da lista
numeros.reverse()#invertendo a lista
for n in range(tamanho):#itera a lista na ordem inversa
    print(numeros[n], end=' ')

print()
