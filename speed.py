import random
import time
from datetime import datetime

words = """Eu encho meus olhos com querosene 
Deixe tudo queimar,
deixe tudo queimar 
Toda a Rússia me olha 
Deixe tudo queimar, 
deixe tudo queimar
Eu encho meus olhos com querosene 
Deixe tudo queimar, 
deixe tudo queimar
Toda a Rússia olha para mim 
Deixe tudo queimar, 
deixe tudo queimar
Agora estou pronto para tudo no mundo
Já cumpri minha pena na internet
Saio para acariciar um gato
E o carro de um policial passa por cima dele
Ando pela cidade com um moletom preto
Geralmente aqui faz frio, gente zangada
Tem nada à minha frente
Mas estou esperando por você, você vai me encontrar
Em correntes de ouro eu me afogo em um pântano
Meu sangue é mais puro que drogas puras
Juntos com outros eles vão torcer você na praça
E eu vou torcer no meu novo espaço de vida
Eu encho meus olhos com querosene
Deixe tudo queimar, deixe tudo queimar
Toda a Rússia me olha
Deixe tudo queimar, deixe tudo queimar
Eu encho meus olhos com querosene
Deixe tudo queimar, deixe tudo queimar
Toda a Rússia olha para mim
Deixe tudo queimar, deixe tudo queimar
Agora estou pronto para tudo no mundo
Já cumpri minha pena na internet
Saio para acariciar um gato
E o carro de um policial passa por cima dele
Ando pela cidade com um moletom preto
Geralmente aqui faz frio, gente zangada
Tem nada à minha frente
Mas estou esperando por você, você vai me encontrar
Chega
de morte Chega de
morte Chega de morte Chega de
morte
Em correntes de ouro eu me afogo no pântano
Meu sangue é mais puro que drogas puras
Junto com outros eles vão torcer você na praça E
eu vou torcer você em meu novo espaço de vida
Em correntes de ouro eu me afogo no pântano
Meu sangue é mais puro que drogas puras
Juntamente com os outros, eles vão torcer você no
novo espaço quadrado
Chega
de morte Chega de
morte Chega de morte Chega de
morte"""


listWords = words.split()
print('\nTeste de velocidade de digitação, digite as palavras que aparecerem em verde!\n')
time.sleep(5)

aleatoryWords = []

inicio = datetime.now()


for c in range(0, 20):
    wordAleatory = listWords[random.randint(0, len(listWords))]
    aleatoryWords.append(wordAleatory)
    print(
        f"\033[32m{wordAleatory}\033[0;0m", end=' ')

userWords = input(
    """\n\nDigite:""").split()


fim = datetime.now()

correctWords = []
incorrectWords = []

for c in range(0, len(aleatoryWords)):
    if aleatoryWords[c] == userWords[c]:
        correctWords.append(userWords[c])
    else:
        incorrectWords.append(userWords[c])

if len(incorrectWords) != 0:
    print(f"\nVocê errou as palvras:", end=' ')
    for c in incorrectWords:
        print(f"'{c}'", end='  ')
else:
    print("\nVocê acertou todas as palavras")


iniciosec = int(inicio.second + (inicio.minute*60))
fimsec = int(fim.second + (fim.minute*60))


if fimsec - iniciosec < 60:
    print(
        f"\n\nSeu tempo foi de {fimsec-iniciosec} segundos,"
        f" obtendo um wpm de: {(len(correctWords)//((fimsec-iniciosec) / 60)):.0f}\n")

else:
    print(
        f"\n\nSeu tempo foi de {((fimsec - iniciosec) // 60)} minuto e {((fimsec - iniciosec) % 60)} seconds,"
        f" obtendo um wpm de: {(len(correctWords)//((fimsec-iniciosec) / 60)):.0f}\n")
