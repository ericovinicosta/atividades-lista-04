#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

numeros = [0,0,0,0,0] #lista 


#carga da lista
for num in range(5): #loop para carregar 5 posições da lista
    numeros[num] = int(input("Digite o {} número: ".format(num + 1)))

#mostrar elementos da lista
for num in range(5):#loop para exibir as 5 posições da lista
    print(numeros[num], end=' ',)

print() #linha vazia para não emendar com o prompt