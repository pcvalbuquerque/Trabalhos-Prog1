import random
from os import system, name 

def jogodavelha():
	""" Função principal(main) que recebe as outras funções e recebe a lista que contem as jogadas, 
	a função main tambem define qual o timeee chamando a função random e usando um contador que defi
	ne qual time será. 
	"""
	limpaTela()
	print(" "*20+"~"*10+ "Bem Vindo ao jogo da velha"+ "~"*10)
	print(" "*20+"Voce irá enfrentar o JARVIS, boa sorte!\n\n\n")
	print(getMatricula())
	print(getNome())
	regra=input("\n\n Deseja ver o livro de regras? \n")
	print("")
	regras(regra)
	print("")
	jogadas=[" "," "," "," "," "," "," "," "," "," "]
	tabuleiro(jogadas)
	print(" "*17+"Agora precisamos definir quem voce será\n")
	qualtime=input(" "*17+"Escolha entre X ou O:")
	if qualtime=="X":
		robo="O"
		print(" "*17+"Voce escolheu o X!\n")
		print(" "*17+"O robo será o O!\n")
	elif qualtime=="O":
		robo="X"
		print("\nVoce escolheu o O!\n")
		print("O robo será o X!\n")
	elif qualtime!="X" and qualtime!="O":
		print(" "*17+"Não é um time válido")
		print(" "*17+"Portanto voce será o 'X' ")
		qualtime="X"
		robo="O"
	primeiroajogar()
	if primeiroajogar()==1:
		print(" "*17+"Voce fara a primeira jogada!")
		print(" "*17+"\nVamos começar!\n")
		y=1
	else:
		print(" "*17+"O Robo SNK fara a primeira jogada!")
		print(" "*17+"\nVamos começar!\n")
		y=2
	print(quemjoga(y,receberjogadasjogador,jogadaComputador,tabuleiro,jogadas,qualtime,robo))
	jogardenovo()
def primeiroajogar():
	""" Função que usa o random para determinar aleatoriamente quem será de cada time
	"""
	return random.randrange(1,3)
def quemjoga(y,receberjogadasjogador,jogadaComputador,tabuleiro,jogadas,qualtime,robo):
	"""A função quem joga é a responsavel por definir quem joga, verifica quem ganhou e se deu velha tambem, ele recebe
	as funções que contem a jogada do jogador e a estrategia robo, ele verifica se valor digitado pelo jogador é valido 
	se nao for ele chama a função de novo.
	
	"""
	if y%2==1:
		receberjogadasjogador(y,jogadas,qualtime)
		tabuleiro(jogadas)
		if jogadas[1]==jogadas[2] and jogadas[1]==jogadas[3] and jogadas[1]!=" ":
			return("O jogo acabou! o '{}' Venceu!".format(jogadas[1]))
		elif jogadas[4]==jogadas[5] and jogadas[4]==jogadas[6] and jogadas[4]!=" ":		
			return("O jogo acabou! o '{}' Venceu!".format(jogadas[4]))
		elif jogadas[7]==jogadas[8] and jogadas[7]==jogadas[9] and jogadas[7]!=" ":
			return("O jogo acabou! o '{}' Venceu!".format(jogadas[7]))
		elif jogadas[1]==jogadas[4] and jogadas[1]==jogadas[7] and jogadas[1]!=" ":		
			return("O jogo acabou! o '{}' Venceu!".format(jogadas[1]))
		elif jogadas[2]==jogadas[5] and jogadas[2]==jogadas[8] and jogadas[2]!=" ":		
			return("O jogo acabou! o '{}' Venceu!".format(jogadas[2]))
		elif jogadas[3]==jogadas[6] and jogadas[3]==jogadas[9] and jogadas[3]!=" ":		
			return("O jogo acabou! o '{}' Venceu!".format(jogadas[3]))
		elif jogadas[1]==jogadas[5] and jogadas[1]==jogadas[9] and jogadas[1]!=" ":		
			return("O jogo acabou! o '{}' Venceu!".format(jogadas[1]))
		elif jogadas[3]==jogadas[5] and jogadas[3]==jogadas[7] and jogadas[3]!=" ":				
			return("O jogo acabou! o '{}' Venceu!".format(jogadas[3]))
		else:
			if " " in jogadas[1:9]:
				return quemjoga(y+1,receberjogadasjogador,jogadaComputador,tabuleiro,jogadas,qualtime,robo)
			else:
				return (" "*30+"VELHAAAA!!")
	if y%2==0:
		print(" "*20+"O Falcon 9 jogou!\n")
		jogadaComputador(y,jogadas,robo,qualtime)
		tabuleiro(jogadas)
		print(" "*20+"Sua vez!\n")
		if jogadas[1]==jogadas[2] and jogadas[1]==jogadas[3] and jogadas[1]!=" ":
			return("O jogo acabou! o '{}' Venceu!".format(jogadas[1]))
		elif jogadas[4]==jogadas[5] and jogadas[4]==jogadas[6] and jogadas[4]!=" ":			
			return("O jogo acabou! o '{}' Venceu!".format(jogadas[4]))
		elif jogadas[7]==jogadas[8] and jogadas[7]==jogadas[9] and jogadas[7]!=" ":			
			return("O jogo acabou! o '{}' Venceu!".format(jogadas[7]))
		elif jogadas[1]==jogadas[4] and jogadas[1]==jogadas[7] and jogadas[1]!=" ":			
			return("O jogo acabou! o '{}' Venceu!".format(jogadas[1]))
		elif jogadas[2]==jogadas[5] and jogadas[2]==jogadas[8] and jogadas[2]!=" ":			
			return("O jogo acabou! o '{}' Venceu!".format(jogadas[2]))
		elif jogadas[3]==jogadas[6] and jogadas[3]==jogadas[9] and jogadas[3]!=" ":			
			return("O jogo acabou! o '{}' Venceu!".format(jogadas[3]))
		elif jogadas[1]==jogadas[5] and jogadas[1]==jogadas[9] and jogadas[1]!=" ":			
			return("O jogo acabou! o '{}' Venceu!".format(jogadas[1]))
		elif jogadas[3]==jogadas[5] and jogadas[3]==jogadas[7] and jogadas[3]!=" ":			
			return("O jogo acabou! o '{}' Venceu!".format(jogadas[3]))
		else:
			if " " in jogadas[1:9]:
				return quemjoga(y+1,receberjogadasjogador,jogadaComputador,tabuleiro,jogadas,qualtime,robo)
			else:

				return (" "*30+"VELHAAAA!!")
def receberjogadasjogador(y,jogadas,qualtime):
	"""Recebe a jogada que o jogador deseja fazer, se o local estiver vazio ele computa a jogada, se não estiver ele chama 
	a função novamente.
	"""
	suajogada=int(input("\nQual posição deseja marcar (1-9): "))
	if suajogada>0 and suajogada<10:
		if jogadas[suajogada]== " ":
			jogadas[suajogada]=qualtime
		else:
			print("\nEssa posicao ja esta ocupada, tente outra!")
			return receberjogadasjogador(y,jogadas,qualtime)
	else:
		print("Por favor digite apenas valores de 1 a 9")
		return receberjogadasjogador(y,jogadas,qualtime)	
def jogadaComputador(y,jogadas,robo,qualtime):
	"""Aqui fica a estrategia do robo, foram feitas inumeras combinações possiveis para o caso de robo estar proximo de ganhar
	ou proximo de perder, quando ele estiver nessa situação ele age para ganhar, ou para não perder, caso niguem esteja proximo
	de ganhar ou perder, a estrategia que eu utilizei, foi seguir pelos cantos, da casa 9->1->3->7, nessa ordem de prioridade,
	o robo verifica se ha a possibilidade de ganhar ou perder, se nao houver ele segue pelos cantos verificando se a casa estiver
	disponivel ele joga, se não ele vai para a proxima até achar uma casa para jogar.  

	"""
	if jogadas[1]==robo and jogadas[3]==robo and jogadas[2]==" ":
		jogadas[2]=robo
	elif jogadas[1]==robo and jogadas[7]==robo  and jogadas[4]==" ":
		jogadas[4]=robo
	elif jogadas[1]==robo and jogadas[9]==robo  and jogadas[5]==" ":
		jogadas[5]=robo
	elif jogadas[3]==robo and jogadas[7]==robo  and jogadas[5]==" ":
		jogadas[5]=robo	
	elif jogadas[3]==robo and jogadas[9]==robo  and jogadas[6]==" ":
		jogadas[6]=robo
	elif jogadas[7]==robo and jogadas[9]==robo  and jogadas[8]==" ":
		jogadas[8]=robo
	elif jogadas[1]==qualtime and jogadas[2]==qualtime  and jogadas[3]==" ":
		jogadas[3]=robo	
	elif jogadas[1]==qualtime and jogadas[4]==qualtime  and jogadas[7]==" ":
		jogadas[7]=robo	
	elif jogadas[1]==qualtime and jogadas[5]==qualtime  and jogadas[9]==" ":
		jogadas[9]=robo	
	elif jogadas[2]==qualtime and jogadas[3]==qualtime  and jogadas[1]==" ":
		jogadas[1]=robo	
	elif jogadas[2]==qualtime and jogadas[5]==qualtime  and jogadas[8]==" ":
		jogadas[8]=robo	
	elif jogadas[3]==qualtime and jogadas[5]==qualtime  and jogadas[7]==" ":
		jogadas[7]=robo	
	elif jogadas[3]==qualtime and jogadas[6]==qualtime  and jogadas[9]==" ":
		jogadas[9]=robo
	elif jogadas[4]==qualtime and jogadas[5]==qualtime  and jogadas[6]==" ":
		jogadas[6]=robo	
	elif jogadas[4]==qualtime and jogadas[7]==qualtime  and jogadas[1]==" ":
		jogadas[1]=robo
	elif jogadas[5]==qualtime and jogadas[6]==qualtime  and jogadas[4]==" ":
		jogadas[4]=robo	
	elif jogadas[5]==qualtime and jogadas[7]==qualtime  and jogadas[3]==" ":
		jogadas[3]=robo	
	elif jogadas[5]==qualtime and jogadas[8]==qualtime  and jogadas[2]==" ":
		jogadas[2]=robo	
	elif jogadas[5]==qualtime and jogadas[9]==qualtime  and jogadas[1]==" ":
		jogadas[1]=robo	
	elif jogadas[6]==qualtime and jogadas[9]==qualtime  and jogadas[3]==" ":
		jogadas[3]=robo	
	elif jogadas[7]==qualtime and jogadas[8]==qualtime  and jogadas[9]==" ":
		jogadas[9]=robo	
	elif jogadas[8]==qualtime and jogadas[9]==qualtime  and jogadas[7]==" ":
		jogadas[7]=robo	
	elif jogadas[1]==qualtime and jogadas[3]==qualtime  and jogadas[2]==" ":
		jogadas[2]=robo	
	elif jogadas[1]==qualtime and jogadas[7]==qualtime  and jogadas[4]==" ":
		jogadas[4]=robo
	elif jogadas[1]==qualtime and jogadas[9]==qualtime  and jogadas[5]==" ":
		jogadas[5]=robo
	elif jogadas[2]==qualtime and jogadas[8]==qualtime  and jogadas[5]==" ":
		jogadas[5]=robo
	elif jogadas[3]==qualtime and jogadas[9]==qualtime  and jogadas[6]==" ":
		jogadas[6]=robo
	elif jogadas[3]==qualtime and jogadas[7]==qualtime  and jogadas[5]==" ":
		jogadas[5]=robo
	elif jogadas[4]==qualtime and jogadas[6]==qualtime  and jogadas[5]==" ":
		jogadas[5]=robo	
	elif jogadas[7]==qualtime and jogadas[9]==qualtime  and jogadas[8]==" ":
		jogadas[8]=robo
	elif jogadas[9]== " ":
		jogadas[9]=robo
	elif jogadas[1]==" ":
		jogadas[1]=robo
	elif jogadas[3]== " ":
		jogadas[3]=robo
	elif jogadas[7]== " ":
		jogadas[7]=robo
def tabuleiro(jogadas):
	"""A função tabuleiro recebe o tabuleiro que será realizado o jogo, ele puxa um item da lista e mostrar na casa onde ele deve aparecer,
	por exemplo [x,1],a função adiciona na casa 1
	"""
	print(" "*20+"Esse é o tabuleiro que voces irao jogar\n")
	print(" " *35+"  {} | {} | {} ".format(jogadas[7],jogadas[8],jogadas[9]))
	print(" " *35+"-------------")
	print(" " *35+"  {} | {} | {} ".format(jogadas[4],jogadas[5],jogadas[6]))
	print(" " *35+"-------------")
	print(" " *35+"  {} | {} | {} \n".format(jogadas[1],jogadas[2],jogadas[3]))	
def regras(regra):
	"""Função não necessaria para o programa funcionar, mas ela ajudará a quem nao conhece o jogo, também mostrar qual o numero de cada casa
	como se fosse uma legenda para o tabuleiro
	"""
	if regra=="s" or regra=="sim" or regra=="S" or regra=="SIM" or regra=="Sim":
		print("\nO tabuleiro é uma matriz de tres linhas por tres colunas")
		print("Voce pode escolher entre X ou O")
		print("É proibido escolher uma casa do tabuleiro que ja foi escolhida")
		print("Para ganhar voce precisar colocar 3-X ou 3-O em linha reta ou diagonal")
		print("Caso nenhum dos dois jogadores consigam ganhar, a velha será declarado e o jogo ficará empatado.\n")
		
		print(" "*20+"O Tabuleiro está numerado dessa maneira:\n")
		print(" " *35+"  7 | 8 | 9 ")
		print(" " *35+"-------------")
		print(" " *35+"  4 | 5 | 6 ")
		print(" " *35+"-------------")
		print(" " *35+"  1 | 2 | 3 \n\n\n")
		print("-"*70)
	else:
		print(" ")
def limpaTela(): 
	"""Função que limpa tela para o programa ficar esteticamente agradavel
	"""
	if name == 'nt': 
		system('cls') 
	else: 
		system('clear') 
def getMatricula():
    """
    Essa função mostra a matricula do aluno
    """
    return "2018204963" 
def getNome():
    """
    Essa função mostra o nome completo do aluno
    """
    return "Paulo César Viana de Albuquerque" 
def jogardenovo():
	again=input("Quer jogar de novo? S/N")
	if again =="S":
		return jogodavelha()
	else:
		return None
if __name__ == "__main__":
	jogodavelha()