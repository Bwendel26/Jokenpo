from gameSet import modoDeJogo
from gameSet import gameSet

player = gameSet()

def switchPlayer():
   """
   Funcao que verifica o player e faz a troca para outro.
   """

   #escrever o condicional do modo de jogo.
   if (modoDeJogo == "1" or modoDeJogo == 1):
      quemJoga = player[1]

      if (player[0] == quemJoga):
         quemJoga = "pc"
      else: 
         quemJoga = player[0]

      return quemJoga #quemComeca
   else:
      quemJoga = player[2]

      if (player[0] == quemJoga):
         quemJoga = player[1]
      else: 
         quemJoga = player[0]
      
      return quemJoga #quemComeca