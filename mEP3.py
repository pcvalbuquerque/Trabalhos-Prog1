#joao e maria nao ficar de recuperação
#eduardo e monica receber autorização
#O salario de eduardo ou da monica ser pago ate 15 de dezembro
#Passagens e hotel < 10k



njao1=float(input())
njao2=float(input())
njao3=float(input())

nmaria1=float(input())
nmaria2=float(input())
nmaria3=float(input())

feriasdudu=input()
feriasmoni=input()

salariodudu=int(input())
salariomoni=int(input())


valorhotel=float(input())
valorpassagem=float(input())


notasfinaisjao=(njao1>=7) and (njao2>=7) and (njao3>=7)
print("Joao aprovado em todas as disciplinas?",notasfinaisjao)

notasfinaismaria=(nmaria1>=7) and (nmaria2>=7) and (nmaria3>=7)
print("Maria aprovada em todas as disciplinas?",notasfinaismaria)

feriasdem= (feriasdudu=="Sim") and (feriasmoni=="Sim")
print("Eduardo e Monica de ferias de dezembro?",feriasdem)

salariosaiu= (salariodudu<=15) or (salariomoni<=15)
print("Pagamento de Eduardo ou Monica liberado a tempo?",salariosaiu)

passahotel= (valorhotel+valorpassagem)<=10000
print("Valor total menor ou igual a R$10.000,00?",passahotel)



vaiviajar= (notasfinaisjao == True) and (notasfinaismaria == True) and (feriasdem == True) and (salariosaiu == True) and (passahotel == True)
print("Irao viajar?",vaiviajar)