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


def verificar_pesos(pesos1,pesos2):
	tam1=len(pesos1)
	tam2=len(pesos2)
	cont=0
	if tam1==tam2:
		for i in range(tam1):
			for j in range(tam2):
				if pesos1[i]==pesos2[j]:
					cont=cont+1
		if cont==tam1:
			return 1
		else: return 0
	else: return 0 

	
def eliminar_repetidos(lis):
	temporal=[]
	for i in range(0,len(lis)):
		cont=0
		for j in range(0,len(temporal)):
			if temporal[j]==lis[i]:
				cont=cont+1
		if cont==0:
			temporal.append(lis[i])
	return temporal

"""def eliminar_repetidos2(lis2):
	temporal=[]
	for i in range(0,len(lis2[0])):
		cont=0
		for j in range(0,len(temporal)):
			if temporal[j]==lis2[0][i]:
				cont=cont+1
		if cont==0:
			temporal.append(lis[i])
	print(temporal)
	print("esto es de eliminar repetidos")
	return temporal"""



def nuevos_terminos(a,b):
	termin=[]
	termin2=[]
	termin3=[]
	termin=a
	termin2=b
	termin3=termin+termin2
	termin3.sort()
	termin3=eliminar_repetidos(termin3)
	return termin3


def agregar_pesos(terminos):
	lista_vac=[]
	for i in range(0,len(terminos)):
		for j in range(len(terminos)):
			if verificar_potencia(terminos[i],terminos[j])!=0:
				lista_vac.append(verificar_potencia(terminos[i],terminos[j]))
	lista_vac.sort()
	lista_vac=eliminar_repetidos(lista_vac)
	return lista_vac

def no_terms_repetidos(matriz_a_llenar,terminos_a_buscar):
	for i in range(len(matriz_a_llenar)):
		if matriz_a_llenar[i]==terminos_a_buscar:
			return 0
		
	
def restar_listas(lista_max,lista_min):
	tempo90=[]
	#print("entemp90")
	#print(lista_min)
	cont=len(lista_max)
	a=0
	for j in range(0,cont):
		a=0
		for i in range(0,len(lista_min)):
			if lista_min[i]==lista_max[j]:
				a=a+1
		if a==0:
			tempo90.append(lista_max[j])
	return tempo90



def implicantes_primos(matriz_con_form,ciclos,implicantes):
	matriz_vac=[]
	count=0
	ciclics=ciclos
	tempo80=[]
	matriz_vac.append([])
	terms=len(matriz_con_form)-1
	lon=len(matriz_con_form[1])-1
	tempo30=[]
	for j in range (1,terms):
		for k in range(1,terms):
			if matriz_con_form[k][lon]==matriz_con_form[j][lon]+1:
				if verificar_pesos(matriz_con_form[j][0],matriz_con_form[k][0])!=0:
					temp1=[]
					temp2=[]
					temp3=[]
					temp4=[]
					#temp1.append(primerMatriz[j][0])
					#temp1.append(primerMatriz[k][0])
					binar=suma_de_binarios(matriz_con_form[j],matriz_con_form[k])
					if binar!=0:

						temp5=[]

						"""print(matriz_con_form[0][j-1])
						print(matriz_con_form[0][k-1])
						print(matriz_con_form[0])"""
						var1=matriz_con_form[0][j-1]
						var2=matriz_con_form[0][k-1]

						temp5=nuevos_terminos(var1,var2)
						#print()
						var100=no_terms_repetidos(matriz_vac[0],temp5)
						
						if var100!=0:
							
							var3=matriz_con_form[0][j-1]
							var4=matriz_con_form[0][k-1]
							
							temp4=agregar_pesos(temp5)
							temp2.append(temp4)
							temp2.extend(binar)
							temp2.append(matriz_con_form[j][lon])
							matriz_vac[0].append(temp5)
							matriz_vac.append(temp2)
							count=count+1
	tempo30=restar_listas(matriz_con_form[0],tempo80)
	#print("TEMPO30")
	#print(tempo30)

	implicantes.extend(tempo30)
	#print("implicantes\n")
	#print(implicantes)
	print("\n")
	for i in matriz_vac:
		print(i)
	print("\n\n\n")
	ciclos=ciclos-1
	#print("ESTO REALIZO CICLOOO")
	if ciclos==1:
		bart=implicantes
		#return bart
	else:
		implicantes_primos(matriz_vac,ciclos,implicantes)
	return implicantes















def formar_matriz_it(primerMatriz):
	cubo=[]
	primos=[]
	flag1=0
	flag2=0
	terms=len(primerMatriz)
	lon=len(primerMatriz[1])
	temp1=[]
	temp2=[]
	temp3=[]
	matrizindice=[]
	matrizindice.append([])
	ciclos=primerMatriz[terms-1][lon-1]
	implicantes=[]
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
								temp3=[]
								temp4=[]
								temp1.append(primerMatriz[j][0])
								temp1.append(primerMatriz[k][0])
								binar=suma_de_binarios(primerMatriz[j],primerMatriz[k])
								if binar!=0:
									temp4=(verificar_potencia(primerMatriz[j][0],primerMatriz[k][0]))
									temp3.append(temp4)
									temp2.append(temp3)
									temp2.extend(binar)
									temp2.append(i)
									#print(temp1 )
									#print(temp2)
									matrizindice[0].append(temp1)
									matrizindice.append(temp2)
	print("\n")
	for i in matrizindice:
		print(i)
	print("\n\n\n")						
	primos=implicantes_primos(matrizindice,ciclos-1,implicantes)
	#print("ESTOS SON LOS IMPLICANTES PRIMOS\n")
	#print(primos)






#def ecuacion_final():


def main():
	print("Metodo Q-M-C\n")
	datos=minterminos()
	datosBinarios=Mzeros(datos)
	numUnos(datosBinarios)
	ordenarUnos(datosBinarios)
	formar_matriz_it(datosBinarios)
	#implicantes(datosBinarios)


main()


