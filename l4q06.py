'''
6. Faça um Programa que peça as quatro notas de 10 alunos, 
calcule e armazene num vetor a média de cada aluno, 
imprima o número de alunos com média maior ou igual a 7.0.
'''

medias = []
quantidade_alunos = 10
quantidade_notas = 4
for aluno in range(quantidade_alunos):
    media = 0
    for nota in range(quantidade_notas):
        media += float(input(f'Informe a {nota+1} nota do {aluno+1} aluno: '))
    medias.append(media / quantidade_notas)

for aluno in range(quantidade_alunos):
    if media[aluno] >= 7.0:
        print(f'{str(media[aluno])}')