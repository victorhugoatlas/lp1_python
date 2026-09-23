notas = [7.5, 8.0, 6.5, 9.0, 7.0]

def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

arredondar_media = lambda media: round(media, 2)

media = calcular_media(notas)
media_arredondada = arredondar_media(media)

situacao = "Aprovado" if media_arredondada >= 7 else "Reprovado"

print("Notas:", notas)
print("Média Arredondada:", media_arredondada)
print("Situação:", situacao)