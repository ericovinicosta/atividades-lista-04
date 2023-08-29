'''
5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
Imprima os três vetores.
'''
vetor = []
pares = []
impares = []

for n in range(20):
    vetor[n].append(int(input(f'Entre com o valor {str(n+1)}: ')))

for n in range(len(vetor)):
    if(vetor[n] % 2):
        pares.append(vetor[n])
    else:
        impares.append(vetor[n])