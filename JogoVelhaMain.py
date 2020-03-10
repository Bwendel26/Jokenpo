from jogadas import jogada, pensar


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


jogada(coordenadasGrade) #teste
################################

#Fazer a logica de chamada da func jogada analisando a grade.