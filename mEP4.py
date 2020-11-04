peso=float(input())
print("Peso: {}".format(peso))
idade=int(input())
print("Idade: {}".format(idade))
if idade>=16 and idade<=69:
	if idade <18:
		autorizacao=input()
		print("Documento de autorizacao: {}".format(autorizacao))
boasaude=input()
print("Boa saude: {}".format(boasaude))
usadrogas=input()
print("Uso drogas injetaveis: {}".format(usadrogas))
primeiradoacao=input()
print("Primeira doacao: {}".format(primeiradoacao))
if primeiradoacao=="N":
	mesesdesdeultima=int(input())
	print("Meses desde ultima doacao: {}".format(mesesdesdeultima))
	doacoesnosultimos12=int(input())
	print("Doacoes nos ultimos 12 meses: {}".format(doacoesnosultimos12))
sexo=input()
print("Sexo biologico: {}".format(sexo))
if sexo=="F":
	gravidez=input()
	print("Gravidez: {}".format(gravidez))
	amamentando=input()
	print("Amamentando: {}".format(amamentando))
	if amamentando=="S":
		mesesbebe=int(input())
		print("Meses bebe: {}".format(mesesbebe))

soma=0

if peso<50:
	soma= soma + 1
	print("Impedimento: abaixo do peso minimo.")
else:
	soma= soma + 0

#idade
if idade<16:
	soma= soma + 1
	print("Impedimento: menor de 16 anos.")
else:
	soma= soma + 0

if idade>69:
	soma= soma + 1
	print("Impedimento: maior de 69 anos.")
else:
	soma= soma + 0

if idade>=16 and idade<18 and autorizacao == "N":
	soma= soma + 1
	print("Impedimento: menor de 18 anos, sem consentimento dos responsaveis.")
else:
	soma= soma + 0

if idade>60 and idade<=69 and primeiradoacao == "S":
	soma= soma + 1
	print("Impedimento: maior de 60 anos, primeira doacao.")
else:
	soma= soma + 0

#boa saude
if boasaude== "N":
	soma= soma + 1
	print("Impedimento: nao esta em boa saude.")
else:
	soma= soma + 0

#drogado
if usadrogas == "S":
	soma= soma + 1
	print("Impedimento: uso de drogas injetaveis.")
else:
	soma= soma + 0

#meses desde a ultima doacao

if sexo=="M" and primeiradoacao == "N":
	if mesesdesdeultima<2:
		soma= soma + 1
		print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
	else:
		soma= soma + 0
	if doacoesnosultimos12>=4:
		soma= soma + 1
		print("Impedimento: numero maximo de doacoes anuais foi atingido.")
	else:
		soma= soma + 0
if sexo =="F" and primeiradoacao == "N":
	if mesesdesdeultima<3:
		soma= soma + 1
		print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
	else:
		soma= soma + 0
	if doacoesnosultimos12>=3:
		soma= soma + 1
		print("Impedimento: numero maximo de doacoes anuais foi atingido.")
	else:
		soma= soma + 0
if sexo == "F":	
	if gravidez == "S":
		soma= soma + 1
		print("Impedimento: gravidez.")
	else:
		soma= soma + 0
	if amamentando == "S" and mesesbebe<12:
		soma= soma + 1
		print("Impedimento: amamentacao.")
	else:
		soma= soma+ 0
			
if soma == 0:
	print("Procure um hemocentro.")




