import numpy as np

participantes = [
    {
        "nome": "Victor",
        "localizacao": "Brasil",
        "afiliacao": "IF Goiano",
        "interesses": ["Programação", "Sertanejo"]
    },
    {
        "nome": "Tatiana",
        "localizacao": "Japao",
        "afiliacao": "IF Goiano",
        "interesses": ["Sushi", "Pop"]
    },
    {
        "nome": "Hemilly",
        "localizacao": "Brasil",
        "afiliacao": "Anhanguera",
        "interesses": ["Sertanejo", "BMW"]
    }
]

regioes = set(participante["localizacao"] for participante in participantes)

afiliacoes = {}
for participante in participantes:
    afiliacao = participante["afiliacao"]
    if afiliacao not in afiliacoes:
        afiliacoes[afiliacao] = []
    afiliacoes[afiliacao].append(participante["nome"])

areas_de_interesse = np.array([interesse for participante in participantes for interesse in participante["interesses"]])
interesses_unicos, contagem = np.unique(areas_de_interesse, return_counts=True)
areas_mais_popular = interesses_unicos[np.argmax(contagem)]

print("Regiões dos participantes:", regioes)
print("Afiliações dos participantes:")
for afiliacao, nomes in afiliacoes.items():
    print(f"{afiliacao}: {', '.join(nomes)}")
print("Area de interesse mais popular:", areas_mais_popular)