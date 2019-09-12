import math

def minterminos():#Esta funcion inicializa una lista en la que se guardon los minterminos agregados
	mint=int(input("Cuantos minterminos tiene tu funcion:"))
	print("\n")
	mins=[]
	for i in range(mint):
		dat=int(input(f"agrega el elemento #:{i} a la lista de minterminos"))
		mins.append(dat)
	return mins#Regresa la lista de minterminos 

def num_Mayor(numerosX):#Encuentra el valor maximo de los minterminos 
	numMayor=max(numerosX)
	return numMayor#Regresa el valor maximo 


def num_Bits(numRef):#Identifica cuantos bits serán necesariosa usar 
	numBits=0
	if numRef>=0 and numRef<2:
		numBits=1
	if numRef>=2 and numRef<4:
		numBits=2
	if numRef>=4 and numRef<8:
		numBits=3
	if numRef>=8 and numRef<16:
		numBits=4
	if numRef>=16 and numRef<32:
		numBits=5
	if numRef>=32 and numRef<64:
		numBits=6
	if numRef>=64 and numRef<128:
		numBits=7
	if numRef>=128 and numRef<256:
		numBits=8
	if numRef>=256 and numRef<512:
		numBits=9
	if numRef>=512 and numRef<1024:
		numBits=10
	if numRef>=1024 and numRef<2048:
		numBits=11
	if numRef>=2048 and numRef<4096:
		numBits=12
	return numBits#Regresa el numero de bits a usar 


def Mzeros(data):#Crea una matriz en la que se guardan los minterminos en valor binario 
	tam=len(data)#Tamaño de la lista con los minterminos
	mayormin=num_Mayor(data)#sr obtiene el mayor numero de los minterminos
	bits=num_Bits(mayormin)#Se obtiene el numero de vits necesarios para pasar los minterminos a binarios 
	ceros=[]#Crea una matriz vacia 
	data2=data#Creamos una copia de los minterminos 
	for i in range(tam):#Se crea un ciclo que va a iterar de acuerdo al numero de minterminos que tengamos
		temp=[]#Se crea una lista vacia en la que se guardaran los digitos de nuestro numero binario
		ref=pow(2,bits-1)#ref es el mayor numero decimal que se necesita para pasar a binario, 2,8,16,32,64, etc...
		bits2=bits#Se respalda el numero de bits para que lo podamos ir modificando 
		temp.append(data[i])#El primer termino del arreglo binario, será el numero en decimal ara no perder la referencia de que numero es
		for j in range(bits):#Iteramos en el numero de bits maximo que se obtivo en la L 49
			nuevo=int(data2[i]/ref)#divide el numero en la potencia maxima de dos que se necesita para ver si tenemos un 0 o un 1 
			if nuevo==1:#Si tenemos un 1 se le resta esa potencia de dos al valor(mintermino)
					data2[i]=data2[i]-pow(2,bits2-1)
			bits2=bits2-1#Se va restando un bit hasta llegar a 0 y no iterar mas 
			temp.append(nuevo)#Se agrega un digito binario al arreglo temp (cuando termine este ciclo, el resultado de ese arreglo es el numero binario )
			ref=ref/2
			
		ceros.append(temp)#Se agrega el numero bianrio a un arreglo para generar una matriz
	return ceros# Regresa la matriz con los numeros binarios 

def numUnos(binarios):#Cuenta el numero de unos que tiene cada numero binario y agrega ese numero en el ultimo digito de cada numero binario
	tam=len(binarios)
	long=len(binarios[1])
	for i in range(tam):
		cont=0
		for j in range(1,long):
			if binarios[i][j]==1:
				cont=cont+1
		binarios[i].append(cont)

def ordenarUnos(matrizBinaria):#Esta funcion ordena los numeros binarios dependiendo de cuantos unos tenga
	tam=len(matrizBinaria)
	lon=len(matrizBinaria[1])
	cont=0
	temp=[]
	for i in range(0,lon):
		for j in range(0,tam):
			if matrizBinaria[j][len(matrizBinaria[1])-1]==i:
				temp=matrizBinaria[cont]
				matrizBinaria[cont]=matrizBinaria[j]
				matrizBinaria[j]=temp
				cont=cont+1


def verificar_potencia(num1,num2):
	difer=abs(num1-num2)
	if (difer==1 or difer==2 or difer==4 or difer==8 or difer==16 or difer==32 or difer==64 or difer==128 or difer==256 or difer==512 or difer==1024 or difer==2048 or difer==4096) :
		return difer
	else:
		return 0 


def suma_de_binarios(binario1,binario2):
	cant=len(binario1)-2
	termsum=[]
	nothing=[]
	cont=0
	for i in range(1,len(binario1)-1):
		if binario1[i]==binario2[i]:
			termsum.append(binario1[i])
		else:
			termsum.append("_")
			cont=cont+1
	if cont!=1:
		return 0
	else:
		return termsum

def formar_matriz_it(primerMatriz):
	cubo=[]
	primos=[]
	flag1=0
	flag2=0
	terms=len(primerMatriz)
	lon=len(primerMatriz[1])
	temp1=[]
	temp2=[]
	matrizindice=[]
	matrizindice.append([])
	ciclos=primerMatriz[terms-1][lon-1]
	for i in range(0,ciclos):
			temp1=[]
			temp2=[]
			for j in range (0,terms):
				temp1=[]
				temp2=[]
				if primerMatriz[j][lon-1]==i:
					for k in range(0,terms):
						temp1=[]
						temp2=[]
						if primerMatriz[k][lon-1]==i+1:
							if verificar_potencia(primerMatriz[j][0],primerMatriz[k][0])!=0:
								temp1=[]
								temp2=[]
								temp1.append(primerMatriz[j][0])
								temp1.append(primerMatriz[k][0])
								binar=suma_de_binarios(primerMatriz[j],primerMatriz[k])
								if binar!=0:
									temp2.append(verificar_potencia(primerMatriz[j][0],primerMatriz[k][0]))
									temp2.extend(binar)
									temp2.append(i)
									print(temp2)
									matrizindice[0].append(temp1)
									matrizindice.append(temp2)
	return matrizindice






#def ecuacion_final():


def main():
	print("Metodo Q-M-C\n")
	datos=minterminos()
	datosBinarios=Mzeros(datos)
	numUnos(datosBinarios)
	ordenarUnos(datosBinarios)
	data63=formar_matriz_it(datosBinarios)
	#implicantes(datosBinarios)


main()


