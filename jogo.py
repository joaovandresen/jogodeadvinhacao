import random
print("🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆")
print("🏆 Boas vindas ao:    🏆 ")
print("🏆 jogo de advinhação do ")
print("🏆 João Vandresen     🏆")
print("🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆")

numeroSecreto= random.randrange(0,100)
totalTentativas = 0
pontos = 100

print("                                      ")
print("Qual nível de dificuldade você deseja utilizar? ")
print("(1) - Fácil (2) - Médio (3) - Difícil")

nivel = int(input("Escolha um nível: "))

if(nivel == 1):
    print("Que nível fácil, franguinho")
    totalTentativas = 20
if(nivel == 2):
    print("Você tem medos de desafio, galizé")
    totalTentativas = 10
if(nivel == 3):
    print("Você já é um galizé, boa sorte")
    totalTentativas = 5
else:
    print("Esse nível não existe")