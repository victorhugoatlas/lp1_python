filmes = ['Motoqueiro Fantasma', 'Aquaman', 'Espartacus', 'Bob Esponja', 'TED']

print("--- Sistema de Avaliação de Filmes ---")

for filme in filmes:
    while True:
        classificacao = input(f"Como você avalia '{filme}' de 1 a 5? (0 para parar): ")
        if classificacao == '0':
            print(f"Avaliação do 'filme' interrompida.")
            break

        classificacao = int(classificacao)
        if classificacao < 1 or classificacao > 5:
            print("Por favor, digite uma nota valida de 1 a 5.")
        else:
            print(f"Vicê avaliou '{filme}' com {classificacao} estrelas. \n")
            break