# Desafio: Jogo de Batalha Naval (simples)

import random

# Cria tabuleiro 5x5
tabuleiro = [["." for _ in range(5)] for _ in range(5)]

# Sorteia posição do navio
linha_navio = random.randint(0, 4)
coluna_navio = random.randint(0, 4)

def mostrar_tabuleiro():
    for l in tabuleiro:
        print(" ".join(l))
    print()

print("=== BATALHA NAVAL ===")
print("Tente acertar a posição do navio! (tabuleiro 5x5)")
mostrar_tabuleiro()

while True:
    jogada = input("Digite linha e coluna (ex: 2 3) ou 'sair': ")
    if jogada.lower() == "sair":
        print("Jogo encerrado. O navio estava em:", linha_navio, coluna_navio)
        break

    try:
        linha, coluna = map(int, jogada.split())
        if 0 <= linha < 5 and 0 <= coluna < 5:
            if linha == linha_navio and coluna == coluna_navio:
                print("🎉 BOOM! Você acertou o navio!")
                tabuleiro[linha][coluna] = "N"
                mostrar_tabuleiro()
                break
            else:
                print("Água! Você errou.")
                tabuleiro[linha][coluna] = "X"
                mostrar_tabuleiro()
        else:
            print("Posição inválida! Use números de 0 a 4.")
    except:
        print("Entrada inválida! Digite linha e coluna, exemplo: 2 3.")
