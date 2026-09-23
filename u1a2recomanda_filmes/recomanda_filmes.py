idade = int(input("Digite sua idade: "))

if idade < 12:
    print("Recomendamos o Filme Infantil")
elif 12 <= idade < 18:
    print("Recomendamos o Filme Adolescente")
else:
    print("Recomendamos o filme adulto")

quantidade_ingressos = 10

if quantidade_ingressos > 0:
    print("Ingressos disponíveis. Divirta-se no cinema!")
else:
    print("Desculpe, todos os ingressos estão esgotados para hoje.")