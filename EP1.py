def maquina(a,b,c,d,e):
	"""função principal da maquina, ela recebe o produto que o cliente quer, e chama as outras funções,
	também é nessa função que contem a logo da maquina, além de calcular o troco, e chamar a função
	troco para mostrar"""
	print("<>"*31)
	print("{} Máquina de Salgados {}".format("-"*20, "-"*20))
	print("<>"*31)
	print("")
	listaprodutos(a,b,c,d,e)
	produto=int(input("Escolha um produto: "))
	if estoque(a, b, c, d, e, produto) == False:
		print("\nProduto indisponível")
		comprardenovo(a, b, c, d, e, produto)
	escolha, valor = qualproduto(produto)
	dinheiro=recebadinheiro(valor)
	if dinheiro==valor:
		print("\nValor pago: R${}".format(dinheiro))
		print("\nNão há troco")
	if dinheiro>valor:
		print("\nValor pago: R${0:.2f}".format(dinheiro))
		print("\nTroco: R${0:.2f}".format(dinheiro-valor))
		print("O seu troco está disponivel abaixo :")
	troco(dinheiro-valor)
	comprardenovo(a, b, c, d ,e , produto)

def listaprodutos(a, b, c, d, e):
	"""Função que mostra a listagem de produtos, e nessa função que mostra ao cliente se o produto que ele quer 
	esta disponivel ou indisponivel, além de mostrar valores e qual produto o cliente quer escolher."""  
	print("~"*45)
	if estoque(a, b, c, d, e, 1):
		print("-----1 - Pão de Queijo ------------- R$2,50")
	else:
		print("-----1 - Pão de Queijo ------- Indisponível")         #
	if estoque(a, b, c, d, e, 2):
		print("-----2 - Coxinha ------------------- R$3,00")
	else:
		print("-----2 - Coxinha ------------- Indisponível")
	if estoque(a, b, c, d, e, 3):
		print("-----3 - Pastel -------------------- R$4,00")
	else:
		print("-----3 - Pastel -------------- Indisponível")
	if estoque(a, b, c, d, e, 4):
		print("-----4 - Esfirra ------------------- R$4,50")
	else:
		print("-----4 - Esfirra ------------- Indisponível")
	if estoque(a, b, c, d, e, 5):
		print("-----5 - Espetinho de frango ------- R$5,00")
	else:
		print("-----5 - Espetinho de frango - Indisponível")
	print("~"*45)

def qualproduto(produto):
	"""Função que mostra qual produto o cliente escolheu e qual o valor desse produto, o valor 
	do produto vai direto para o calculo do troco, sendo diminuido pelo valor que o cliente inseriu."""   
	if produto==1:
		print("\nVocê escolheu Pão de Queijo")
		print("Preço: R$ 2,50\n")
		return "Pão de Queijo", 2.50
	elif produto==2:
		print("\nVocê escolheu Coxinha")
		print("Preço: R$ 3,00\n")
		return "Coxinha", 3.00
	elif produto==3:
		print("\nVocê escolheu Pastel")
		print("Preço: R$ 4,00\n")
		return "Pastel", 4.00
	elif produto==4:
		print("Você escolheu Esfirra\n")
		print("Preço: R$ 4,50\n")
		return "Esfirra", 4.50
	elif produto==5:
		print("\nVocê escolheu Espetinho de frango")
		print("Preço: R$ 5,00\n")
		return "Espetinho de frango", 5.00

def estoque(a, b, c, d, e, produto):
	"""Função que determina se o produto ta no estoque ou não, se o produto selecionar for maior que zero, 
	quer dizer que ainda tem no minimo 1 no estoque, e por isso aparecerá como True, caso não tenha o produto 
	no estoque, irá apresentar False para o programa, assim fazendo com que na lista de produtos, esse produto 
	apareca como indisponivel."""   
	if produto == 1:
		if a > 0:
			return True
		else:
			return False
	elif produto == 2:
		if b > 0:
			return True
		else:
			return False
	elif produto == 3:
		if c > 0:
			return True
		else:
			return False
	elif produto == 4:
		if d > 0:
			return True
		else:
			return False
	elif produto == 5:
		if e > 0:
			return True
		else:
			return False

def recebadinheiro(total, x=0):
	"""Função que recebe o dinheiro do cliente, e verifica se o valor inserido é suficiente para comprar o produto,
	se nao for é pedido novamente para o cliente inserir um valor, assim sucessivamente até que o valor do produto
	seja alcançado."""
	if total>x:
		dinheiro1=float(input("Insira o dinheiro no local indicado:"))
		return recebadinheiro(total, x+dinheiro1)
	else:
		return x

def troco(trocoreal):
	"""A função troco é responsavel por calcular e apresentar o troco para o cliente, mostrando sempre a maior nota ou
	moeda possivel para diminuir a quantidade de nota/moedas no troco, a função round dentro do troco, nao deixa que
	por conta dos calculos acabe faltando alguns centavos, assim garantido o valor exato que o cliente precisa receber"""  
	trocoreal=round(trocoreal,2)
	if trocoreal >=100:
		print('R$ 100,00')
		return troco(trocoreal-100)

	elif trocoreal >=50:
		print('R$ 50,00')
		return troco(trocoreal-50)

	elif trocoreal >=20:
		print('R$ 20,00')
		return troco(trocoreal-20)

	elif trocoreal >= 10:
		print('R$ 10,00')
		return troco(trocoreal-10)

	elif trocoreal >= 5:
		print('R$ 5,00')
		return troco(trocoreal-5)

	elif trocoreal >= 2:
		print('R$ 2,00')
		return troco(trocoreal-2)

	elif trocoreal >= 1:
		print('R$ 1,00')
		return troco(trocoreal-1)

	elif trocoreal >= 0.50:
		print('R$ 0,50')
		return troco(trocoreal-0.50)

	elif trocoreal >= 0.25:
		print('R$ 0,25')
		return troco(trocoreal-0.25)

	elif trocoreal >= 0.10:
		print('R$ 0,10')
		return troco(trocoreal-0.10)

	elif trocoreal >= 0.05:
		print('R$ 0,05')
		return troco(trocoreal-0.05)

	elif trocoreal >= 0.01:
		print('R$ 0,01')
		return troco(trocoreal-0.01)


def comprardenovo(a, b, c, d, e, produto):
	"""A função comprardenovo é responsavel por tornar possivel outra compra após a finalização de uma, quando o cliente 
	deseja fazer uma compra novamente, é tirado 1 do produto que escolheu do estoque, e é chamado a função principal novamente, 
	caso o cliente nao queira mais nada , o programa é encerrado."""
	outracompra=input('\nDeseja fazer outra compra? (S/N):')
	if outracompra == 's' or outracompra == 'S':
		if produto == 1:
			return maquina(a-1, b, c, d, e)
		elif produto == 2:
			return maquina(a, b-1, c, d, e)
		elif produto == 3:
			return maquina(a, b, c-1, d, e)
		elif produto == 4:
			return maquina(a, b, c, d-1, e)
		elif produto == 5:
			return maquina(a, b, c, d, e-1)
	if outracompra == 'n' or outracompra == 'N':
		print("<>"*31)
		print("{} Máquina de Salgados {}".format("-"*20, "-"*20))
		print("<>"*31)
		print("")
		print("\nObrigado pela compra!")
		print("\nVolte sempre!")


maquina(5, 5, 5, 5, 5)

