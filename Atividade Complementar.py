#atividade de nomes

nomes = []

while len(nomes) < 10:
    nome = str(input("escreva um nome): "))
    nomes.append(nome)
procurar= str(input("qual nome procurar? "))
for nome in nomes:
    if procurar in nomes:
        encontrou = "ACHEI"
    else:
     encontrou="NÃO ACHEI"
print(encontrou)