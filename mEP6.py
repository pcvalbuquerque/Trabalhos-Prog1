def geometria():
	formato=input()
	
	if formato=="R" or formato=="P" or formato=="TE" or formato=="TRE" or formato=="TRD":
		if formato=="R" or formato=="P":	
			largura=int(input())
			altura=int(input())
			if largura>0 and altura>0:
				caracter=input()
				if formato=="R":
					retangulo(caracter, largura, altura)
				if formato=="P":
					paralelograma(caracter, largura, altura)
				
			else:
				print("Medida invalida.")
		else:
			altura=int(input())	
		
			if altura>0:	
				caracter=input()
				if formato=="TE":
					trianguloequi(caracter, altura)
				if formato=="TRE":
					trianguloretE(caracter, altura)
				if formato=="TRD":
					trianguloretD(caracter,altura)
				
			else:
				print("Medida invalida.")
		
	else:
		print("Objeto invalido.")


def retangulo(caracter, largura, altura, n=0):
	if n==0:
		print((caracter)*(largura))
		return retangulo(caracter, largura, altura, n+1)
	alturasemborda=altura-1
	if n<alturasemborda:
		print(caracter+(" "*(largura-2)+caracter))
		
		return retangulo(caracter, largura, altura, n+1)	
		

	if n==alturasemborda:
		print((caracter)*(largura))
	
def paralelograma(caracter, largura, altura, n=0,c=2):
	if n==0:
		print((caracter)*(largura))
		return paralelograma(caracter, largura, altura,n+1,c)
	alturasemborda=altura-1
	if n<alturasemborda:
		print((" "*n)+caracter+(" "*(largura-c)+caracter))
		return paralelograma(caracter, largura, altura, n+1,c)
	
	if n==alturasemborda:
		print((" "*n)+(caracter)*(largura))

def trianguloequi(caracter, altura, n=0,c=0):
	if n==0:
		print(" "*(altura-1)+caracter)
		return trianguloequi(caracter, altura, n+1,c)
	
	alturasemborda=altura-1
	if n<alturasemborda:
		print((" "*(altura-c-2))+(caracter)+(" "*(n+c))+(caracter))
		return trianguloequi(caracter, altura, n+1,c+1)
	if n==alturasemborda:
		print(caracter*((altura*2)-1))
	
def trianguloretE(caracter, altura, n=0):
	if n==0:
		print(caracter)
		return trianguloretE(caracter, altura, n+1)
	if n==1:
		print(caracter+caracter)
		return trianguloretE(caracter,altura,n+1)
	alturasemborda=altura-1
	if n<alturasemborda:
		print(caracter+(" "*(n-1)+caracter))
		return trianguloretE(caracter, altura, n+1)

	if n==alturasemborda:
		print(caracter*(n+1))

def trianguloretD(caracter, altura, n=0):
	if n==0:
		print((" "*(altura-n-1))+caracter)
		return trianguloretD(caracter, altura, n+1)
	if n==1:
		print((" "*(altura-n-1))+caracter+caracter)
		return trianguloretD(caracter,altura,n+1)
	alturasemborda=altura-1
	if n<alturasemborda:
		print((" "*(altura-n-1))+caracter+(" "*(n-1)+caracter))
		return trianguloretD(caracter, altura, n+1)

	if n==alturasemborda:
		print(caracter*(n+1))

geometria()