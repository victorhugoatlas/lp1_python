convidados = ("Hemilly", "Thaynnara", "Yukari", "Victoria", "Evelyn")

confirmados = ["Hemilly", "Yukari"]

nao_confirmados = [convidado for convidado in convidados if convidado not in confirmados]

print("Convidados que ainda não confirmaram:")
for pessoa in nao_confirmados:
    print(pessoa)

print("\nEnviando lembretes para convidados que ainda não confirmaram.")