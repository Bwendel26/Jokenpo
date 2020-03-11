from random import randint
from time import sleep #intervalo de decisao

print("Bem vindo ao jogo da velha!")
modoDeJogo = input("1 jogador ou 2? ")
str(modoDeJogo)

def gameSet():
  """
  Funcao que decide quem inicia jogando.
  """

  if(modoDeJogo == "2"):
    jogador1 = input("Quem e o jogador 1: ")
    jogador2 = input("Quem e o jogador 2: ")
  else:
    jogador1 = input("Digite seu nome: ")

  print("Vamos ver quem vai comecar...")
  # TIMER
  def foo():
    print("processando...")

  secs = randint(2, 5)
  while (secs > 0):
    foo()
    sleep(1)
    secs -= 1
  ##########################

  # Logica de quem inicia jogando
  quemComeca = randint(1, 2) #1 ou 2.

  if (modoDeJogo == "1"): #1 pessoa jogando
    if (quemComeca == 1): 
      quemComeca = jogador1 # player inicia jogando
    elif (quemComeca == 2):
      quemComeca = "pc" # pc inicia jogando
  elif (modoDeJogo == "2"): #2 pessoas jogando
    if (quemComeca == 1):
      quemComeca = jogador1 # player1 inicia jogando
    elif (quemComeca == 2):
      quemComeca = jogador2 #player2 inicia jogando

  print("{} vai comecar o game!".format(quemComeca))

  # Selecao de retorno da funcao, baseado no modo de jogo.
  if (modoDeJogo == "1"):
    return [ jogador1, quemComeca ]
  elif (modoDeJogo == "2"):
    return [ jogador1, jogador2, quemComeca ]