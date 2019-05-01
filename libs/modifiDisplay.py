#FUNCTION TEXT
def AddCharA(char,lista,z):
	x=0
	for y in lista[0]:
		if y=="|":
			break
		else:
			x+=1
	x+=1
	if x==len(lista[0]):
		lista[0]=lista[0][:len(lista[0])-1]+char+"|"
	elif x==1:
		lista[0]=char+lista[0][:]
	else:
		lista[0]=lista[0][:x-1]+char+lista[0][x-1:]
	
	print(char)
	print(lista)
	z[0].configure(text=lista[0])

def DelChar(lista,z):
	if len(lista[0])!=1:
		x=0
		for y in lista[0]:
			if y=="|":
				break
			else:
				x+=1
		x+=1
		print(x)
		if x!=1:
			if x==len(lista[0]):
				lista[0]=lista[0][:x-2]+"|"
			else:
				lista[0]=lista[0][:x-2]+"|"+lista[0][x:]
	print(lista)
	z[0].configure(text=lista[0])

def MoveD(lista,z):
	if len(lista[0])!=1:
		x=0
		for y in lista[0]:
			if y=="|":
				break
			else:
				x+=1
		print(x)
		x+=1
		if x!=len(lista[0]):
			if x==1:
				lista[0]=lista[0][x]+"|"+lista[0][x+1:]
			else:
				lista[0]=lista[0][:x-1]+lista[0][x]+"|"+lista[0][x+1:]
	print(lista)
	z[0].configure(text=lista[0])

def MoveI(lista,z):
	print("------\n",lista)
	if len(lista[0])!=1:
		x=0
		for y in lista[0]:
			if y=="|":
				break
			else:
				x+=1
		x+=1
		print(x)
		if x!=1:
			if x==len(lista[0]):
				lista[0]=lista[0][:x-2]+"|"+lista[0][x-2]
			else:
				lista[0]=lista[0][:x-2]+"|"+lista[0][x-2]+lista[0][x:]
	print(lista)
	z[0].configure(text=lista[0])
