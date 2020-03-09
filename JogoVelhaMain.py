from gameSet import gameSet
from gradeJogo import criaGrade
from random import randint
from time import sleep #intervalo de decisao

# Chamando as funcoes para comecar o game
playerData = gameSet()

coordenadasGrade = { # posicoes do game: coordenadas na grade
                     1: (5, 3),
                     2: (9, 3),
                     3: (15, 3),
                     4: (5, 6),
                     5: (9, 6),
                     6: (15, 6),
                     7: (5, 10),
                     8: (9, 10),
                     9: (15, 10)
                     }

#Logica da jogada
def jogada(coordenadas):
   jogadas = ()
   """Tupla que n aceita repeticao,
   ajudando na logica de nao poder
   sobreescrever uma jogada ja feita."""
   
   # Nivel de analise de modo de jogo1
   if (len(playerData) == 2):
      iniciante = playerData[1]
      criaGrade()
      #Nivel de analise de jogada
      if (playerData[1] == "pc"):
         #Pensar na jogada
         # TIMER
         def foo():
            print("Pc esta pensando...")

         secs = randint(1, 2)
         while (secs > 0):
            foo()
            sleep(1)
            secs -= 1
         ################
         jogada1 = randint(1, 9)
      else:
         jogada1 = input("{} qual a sua jogada (1 a 9)?: ".format(iniciante))

   # Nivel de analise de modo de jogo2
   elif (len(playerData) == 3):
      iniciante = playerData[2]
      criaGrade()
      jogada1 = input("{} qual a sua jogada (1 a 9)?: ".format(iniciante))
   
   return print(jogada1) #teste

jogada(coordenadasGrade)
################################

#Fazer a logica de chamada da func jogada analisando a grade.