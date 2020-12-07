def eleicao():	
	ncandidato=int(input())
	candidatos=[""]*(ncandidato+1)
	candidatos=quantidadecandidato(ncandidato,candidatos)
	neleitores=int(input())
	nvotos=[0]*(neleitores)
	validos=[0]*(ncandidato+1)
	nvotos=votos(ncandidato,neleitores,nvotos)
	validos, brancos, nulos = computavoto(neleitores,nvotos,candidatos,validos)
	printacandidato(candidatos,validos)
	print("Brancos: {}".format(brancos))
	print("Nulos: {}".format(nulos))
	ganhador=vencedor(validos)
	print("Vencedor(a): {}".format(candidatos[ganhador]))

def quantidadecandidato(ncandidato,candidatos,y=1):
	if ncandidato>0:
		nomedocandidato=input()
		candidatos[y]=nomedocandidato
		return quantidadecandidato(ncandidato-1,candidatos,y+1)
	else:
		return candidatos
		

def votos(ncandidato,neleitores,nvotos,x=0):
	if neleitores>0:
		voto=int(input())
		nvotos[x]=voto
		return votos(ncandidato,neleitores-1,nvotos,x+1)
	else:
		return nvotos

def computavoto(neleitores,nvotos,candidatos,validos,brancos=0,nulos=0,w=0):
	if len(nvotos)>w:
		if nvotos[w]==0:
			return computavoto(neleitores,nvotos,candidatos,validos,brancos+1,nulos,w+1)
		elif nvotos[w]>len(candidatos)-1:
			return computavoto(neleitores,nvotos,candidatos,validos,brancos,nulos+1,w+1)
		else:
			validos[nvotos[w]]+=1
			return computavoto(neleitores,nvotos,candidatos,validos,brancos,nulos,w+1)
	else:
		return validos, brancos, nulos

def vencedor(validos,nmax=0,i=0,ganhador=0):
	
	if i>=len(validos):
		return ganhador
	elif validos[i]>nmax:
		ganhador=i
		nmax=validos[i]
		return vencedor(validos,nmax,i+1,ganhador)
	else:
		return vencedor(validos,nmax,i+1,ganhador)
def printacandidato(candidatos,validos,gg=1):
	
	if gg>len(candidatos)-1:
		return True
	else:	
		print("{}: {}".format(candidatos[gg], validos[gg]))
		return printacandidato(candidatos,validos,gg+1)




eleicao()
	

	


























