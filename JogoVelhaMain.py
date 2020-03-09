from gameSet import gameSet
from gradeJogo import criaGrade
from random import randint
from time import sleep #intervalo de decisao

def pensar():
# TIMER
   def frasePensar():
      print("Pc esta pensando...")

   secs = randint(1, 2)
   while (secs > 0):
      frasePensar()
      sleep(1)
      secs -= 1
################



# Chamando as funcoes para comecar o game
playerData = gameSet()

esp = 20 #espacamento usado para centralizar grade...
coordenadasGrade = { # posicoes do game: coordenadas na grade (eixo x, eixo y)
                     1: (esp + 5, 3),
                     2: (esp + 9, 3),
                     3: (esp + 15, 3),
                     4: (esp + 5, 6),
                     5: (esp + 9, 6),
                     6: (esp + 15, 6),
                     7: (esp + 5, 10),
                     8: (esp + 9, 10),
                     9: (esp + 15, 10)
                     }

def aindaJoga(): #Analisar se e possivel jogar ainda ou o game acabou
   return True

#Logica da jogada 1
def primeiraJogada(coordenadas):
   jogadas = ()
   """Tupla que n aceita repeticao,
   ajudando na logica de nao poder
   sobreescrever uma jogada ja feita."""
   if(len(jogadas) == 0):
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
   
   else:
      while(aindaJoga == True):
         return 0

# primeiraJogada(coordenadasGrade) #teste
################################

#Fazer a logica de chamada da func jogada analisando a grade.