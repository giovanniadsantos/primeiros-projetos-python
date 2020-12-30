# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word):
        self.erros = 0
        self.word = word
        self.hidden = ""
        self.lc = ""
        self.le = ""
        self.temp_hidden = []


    # Método para adivinhar a letra
    def guess(self, letter):

        for x in range(len(self.word)):
            if letter == self.word[x]:
                self.temp_hidden[x] = self.word[x]

        self.hidden = ""
        for i in self.temp_hidden:
            self.hidden += i

        if letter in self.word:
            self.lc += letter+" "
        else:
            self.le += letter+" "
            self.erros += 1


    # Método para verificar se o jogo terminou
    def hangman_over(self):
        if self.erros == 6:
            return True

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if self.hidden == self.word:
            return True

    # Método para não mostrar a letra no board
    def hide_word(self):
        for x in self.word:
            self.temp_hidden.append("_")
            self.hidden += "_"

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print(board[self.erros])
        print("palavra: " + str(self.hidden))
        print("\nLetras certas: " + self.lc)
        print("\nLetras erradas: " + self.le)



# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))-1].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())
    game.hide_word()

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter

    while game.erros < 6:
        # Verifica o status do jogo
        game.print_game_status()

        letra = input("\nDigite uma letra: ")
        game.guess(letra)

        # De acordo com o status, imprime mensagem na tela para o usuário
        if game.hangman_won():
            print('\nParabéns! Você venceu!!')
            print('A palavra era ' + game.word)
            break

        if game.hangman_over():
            print('\nGame over! Você perdeu.')
            print('A palavra era ' + game.word)
            print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()