"""
    23. A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
       alexandre       456123789
       anderson        1245698456
       antonio         123456456
       carlos          91257581
       cesar           987458
       rosemary        789456125
       Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
       ACME Inc.               Uso do espaço em disco pelos usuários
       ------------------------------------------------------------------------
       Nr.  Usuário        Espaço utilizado     % do uso
       
       1    alexandre       434,99 MB             16,85%
       2    anderson       1187,99 MB             46,02%
       3    antonio         117,73 MB              4,56%
       4    carlos           87,03 MB              3,37%
       5    cesar             0,94 MB              0,04%
       6    rosemary        752,88 MB             29,16%
       
       Espaço total ocupado: 2581,57 MB
       Espaço médio ocupado: 430,26 MB
       O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.
"""
import math

def converte_byte_em_megabyte(bytes):
    return f'{bytes / math.pow(1024,2):.2f}'
    
def calcula_percentual_uso(ocupado, total):
    return f'{100 * ocupado / total:.2f}'


with open('usuarios.txt',mode='r',encoding='utf-8') as usuario:
    dados_de_usuario = usuario.readlines()
    
l_nomes = []
l_espaco_ocupado = []

for linha in dados_de_usuario:
    l_nomes.append(linha[:16].split())
    l_espaco_ocupado.append(int(linha[16:]))

total = 0
for tam in l_espaco_ocupado:
    total += int(tam)
    
print(total, calcula_percentual_uso(456123789, total))
#saida: gerar relatorio.txt
relatorio_header = f"""
ACME Inc.               Uso do espaço em disco pelos usuários
-------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso
"""     
relatorio_footer = f"""
Espaço total ocupado: {converte_byte_em_megabyte(total)} MB
Espaço médio ocupado: {float(converte_byte_em_megabyte(total))/len(l_nomes):.2f} MB
"""
print(relatorio_header)

for i in range(len(l_nomes)):
    nome = str(l_nomes[i])
    espaco = l_espaco_ocupado[i]
    print(f'{i+1:3} {nome:15} {converte_byte_em_megabyte(espaco):7} MB {calcula_percentual_uso(espaco, total):5}%')

print(relatorio_footer)