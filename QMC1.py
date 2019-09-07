import math

def minterminos():
	mint=int(input("Cuantos minterminos tiene tu funcion:"))
	print("\n")
	mins=[]
	for i in range(mint):
		dat=int(input(f"agrega el elemento #:{i} a la lista de minterminos"))
		mins.append(dat)
	return mins

def num_Mayor(numerosX):
	#tam=len(numerosX)
	"""numMayor=0
	for i in range(tam):
		if numerosX[i]>numMayor:
			numMayor=numerosX(i)

	print(numMayor)"""
	numMayor=max(numerosX)
	return numMayor


def num_Bits(numRef):
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
	return numBits


def Mzeros(data):
	tam=len(data)
	mayormin=num_Mayor(data)
	bits=num_Bits(mayormin)
	ceros=[]
	data2=data
	for i in range(tam):
		temp=[]
		ref=pow(2,bits-1)
		bits2=bits
		temp.append(data[i])
		for j in range(bits):
			nuevo=int(data2[i]/ref)
			if nuevo==1:
					data2[i]=data2[i]-pow(2,bits2-1)
			bits2=bits2-1
			temp.append(nuevo)
			ref=ref/2
			
		ceros.append(temp)
	return ceros

def numCeros(binarios):
	



def main():
	print("Metodo Q-M-C\n")
	datos=minterminos()
	datosBinarios=Mzeros(datos)
	print(datosBinarios)



main()


