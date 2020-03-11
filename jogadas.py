from gameSet import gameSet
from gradeJogo import criaGrade
from aindaJoga import aindaJoga
from random import randint
from time import sleep #intervalo de decisao


def pensar():
# TIMER
   def frasePensar():
      print("Pc esta pensando...")

   secs = randint(2, 3)
   while (secs > 0):
      frasePensar()
      sleep(1)
      secs -= 1
################


playerData = gameSet()

#Logica da jogada 1
def jogada(coordenadas):
   jogadas = [""]
   qtdJogadas = 0
   """Tupla que n aceita repeticao,
   ajudando na logica de nao poder
   sobreescrever uma jogada ja feita."""
   if(len(jogadas) == 1):
      # Nivel de analise de modo de jogo1
      if (len(playerData) == 2):
         iniciante = playerData[1]
         criaGrade()
         #Nivel de analise de jogada
         if (playerData[1] == "pc"):
            #Pensar na jogada
            pensar()
            jogada1 = randint(1, 9)
         else:
            jogada1 = input("{} qual a sua jogada (1 a 9)?: ".format(iniciante))

      # Nivel de analise de modo de jogo2
      elif (len(playerData) == 3):
         iniciante = playerData[2]
         criaGrade()
         jogada1 = input("{} qual a sua jogada (1 a 9)?: ".format(iniciante))
      
      jogadas[0] = jogada1
      qtdJogadas += 1
   
   elif(len(jogadas > 1)):
      if (aindaJoga()): #MEXER AQUI ##############
         return""