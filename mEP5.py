##Maratona de boston
tempodocorredorminutos=int(input())
idade=int(input())
sexo=input()


tempodocorredorhoras=tempodocorredorminutos//60
restotempoemhoras=tempodocorredorminutos%60

if sexo=="M" or sexo=="m":
	print("Tempo do corredor: {:0>2}h {:0>2}min".format(tempodocorredorhoras,restotempoemhoras))
if sexo=="F" or sexo=="f":
	print("Tempo da corredora: {:0>2}h {:0>2}min".format(tempodocorredorhoras,restotempoemhoras))




if sexo=="M" or sexo=="m":
	if idade>=18 and idade<=34:
		temponecessario=180
		print("Tempo necessario: 03h 00min ")
	if idade>=35 and idade<=39:
		temponecessario=185
		print("Tempo necessario: 03h 05min ")
	if idade>=40 and idade<=44:
		temponecessario=190
		print("Tempo necessario: 03h 10min ")
	if idade>=45 and idade<=49:
		temponecessario=200
		print("Tempo necessario: 03h 20min ")
	if idade>=50 and idade<=54:
		temponecessario=205
		print("Tempo necessario: 03h 25min ")
	if idade>=55 and idade<=59:
		temponecessario=215
		print("Tempo necessario: 03h 35min ")
	if idade>=60 and idade<=64:
		temponecessario=230
		print("Tempo necessario: 03h 50min ")
	if idade>=65 and idade<=69:
		temponecessario=245
		print("Tempo necessario: 04h 05min ")
	if idade>=70 and idade<=74:
		temponecessario=260
		print("Tempo necessario: 04h 20min ")
	if idade>=75 and idade<=79:
		temponecessario=275
		print("Tempo necessario: 04h 35min ")
	if idade>=80:
		temponecessario=290
		print("Tempo necessario: 04h 50min ")

if sexo=="F" or sexo=="f":
	if idade>=18 and idade<=34:
		temponecessario=210
		print("Tempo necessario: 03h 30min ")
	if idade>=35 and idade<=39:
		temponecessario=215
		print("Tempo necessario: 03h 35min ")
	if idade>=40 and idade<=44:
		temponecessario=220
		print("Tempo necessario: 03h 40min ")
	if idade>=45 and idade<=49:
		temponecessario=230
		print("Tempo necessario: 03h 50min ")
	if idade>=50 and idade<=54:
		temponecessario=235
		print("Tempo necessario: 03h 55min ")
	if idade>=55 and idade<=59:
		temponecessario=245
		print("Tempo necessario: 04h 05min ")
	if idade>=60 and idade<=64:
		temponecessario=260
		print("Tempo necessario: 04h 20min ")
	if idade>=65 and idade<=69:
		temponecessario=275
		print("Tempo necessario: 04h 35min ")
	if idade>=70 and idade<=74:
		temponecessario=290
		print("Tempo necessario: 04h 50min ")
	if idade>=75 and idade<=79:
		temponecessario=305
		print("Tempo necessario: 05h 05min ")
	if idade>=80:
		temponecessario=320
		print("Tempo necessario: 05h 20min ")



if temponecessario>=tempodocorredorminutos:
	print("Conseguiu indice? SIM")
	tempoabaixodamedia= temponecessario - tempodocorredorminutos
	tempoabaixodamediahoras= tempoabaixodamedia//60
	tempoabaixodamediaminutos= tempoabaixodamedia%60

	if sexo=="M" or sexo=="m":
		print("O corredor correu {:0>2}h {:0>2}min abaixo do indice".format(tempoabaixodamediahoras,tempoabaixodamediaminutos))

	if sexo=="F" or sexo=="f":
		print("A corredora correu {:0>2}h {:0>2}min abaixo do indice".format(tempoabaixodamediahoras,tempoabaixodamediaminutos))

if temponecessario<tempodocorredorminutos:
	print("Conseguiu indice? NAO")
	tempoabaixodamedia= tempodocorredorminutos - temponecessario
	tempoabaixodamediahoras= tempoabaixodamedia//60
	tempoabaixodamediaminutos= tempoabaixodamedia%60

	if sexo=="M" or sexo=="m":
		print("O corredor correu {:0>2}h {:0>2}min acima do indice".format(tempoabaixodamediahoras,tempoabaixodamediaminutos))

	if sexo=="F" or sexo=="f":
		print("A corredora correu {:0>2}h {:0>2}min acima do indice".format(tempoabaixodamediahoras,tempoabaixodamediaminutos))








