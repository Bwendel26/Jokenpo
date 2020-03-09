# funcoes auxiliares:
# def menosUm(subtraido):
#    subtraido -= 1
#    return subtraido

# variaveis auxiliares:
espacamento = 20 * " "

# Criado grade do game:
def criaColuns():
   """Cria grade do tabuleiro de jogo da velha."""

   #Preencher Colunas
   numColunsVaz = 5
   numColuns = 2
   coluns = ""

   while(numColuns > 0): #preenchendo colunas de linha
      while(numColunsVaz > 0): #preenchendo espacos vazios das colunas de cada linha
         coluns += " "
         numColunsVaz -= 1

      coluns += "|"
      numColunsVaz = 5
      numColuns -= 1

   coluns += "     "
   print(espacamento ,coluns ,espacamento)

########################
def criaGrade():
   """
   Funcao que monta a grade do jogo.
   """
   numLinsVaz = 3
   numLins = 3
   linha = "-" * 17 #Linha padrao

   while(numLins > 0):
      
      while(numLinsVaz > 0):
         criaColuns()
         numLinsVaz -= 1
      if(numLins > 1):
         print(espacamento, linha, espacamento)       
      numLinsVaz = 3
      numLins -= 1