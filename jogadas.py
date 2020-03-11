from gameSet import gameSet
from gradeJogo import criaGrade
from aindaJoga import aindaJoga
import switchPlayer
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

###########ERROOOOOOOOO

playerData = gameSet()

#Logica da jogada 1
def jogada(coordenadas):
   jogadas = [""]  
   """talvez implementer uma verificacao com loop for para retirar as jogadas já feitas."""

   qtdJogadas = 0 #counter

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
      qtdJogadas += 1 #VERIFICAR AQUI
   
   elif(len(jogadas > 1)):
      if (aindaJoga()):
         jogadorAtual = switchPlayer()
         if (jogadorAtual == "pc"):
            pensar()
            jogadaAtual = randint (1, 9)
         else: 
            jogadaAtual = input("{} qual a sua jogada (1 a 9)?: ".format(jogadorAtual))
      else:
         jogadorAtual = "RESOLVER ISSO AQUI"
         print("O jogo acabou! \nParabens {} voce ganhou!!!".format(jogadorAtual))


jogada()