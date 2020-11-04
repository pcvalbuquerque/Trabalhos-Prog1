x=float(input())
op=input()
y=float(input())

if op== "+":
	print("{} + {} = {}".format(x, y ,x+y))
elif op == "-":
	print("{} - {} = {}".format(x, y ,x-y))
elif op== "*":
	print("{} * {} = {}".format(x, y ,x*y))
elif op== "**":
	print("{} ** {} = {}".format(x, y ,x**y))
elif op== "%":
	print("{} % {} = {}".format(x, y ,x%y))
elif op== "//":
	print("{} // {} = {}".format(x, y ,x//y))
else:
	print("Operacao nao reconhecida!")