Nota_1 = float(input("Digite a nota 1: "))
Nota_2 = float(input("Digite a nota 2: "))
Nota_3 = float(input("Digite a nota 3: "))
Nota_4 = float(input("Digite a nota 4: "))

media = (Nota_1 + Nota_2 + Nota_3 + Nota_4) / 4

if media >= 6:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

print(f"Média final: {media}")
print(f"Situação do Aluno: {situacao}")