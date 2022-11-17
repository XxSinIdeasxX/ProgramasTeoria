import matplotlib.pyplot as plt
import math

def binario(n, elem, conteo):
    if(n==0):
        while(elem>0):
            elem-=1
        return conteo
    conteo=binario(n//2,elem-1,conteo)
    if(n%2==1):
        conteo+=1
    return conteo

def sigma1(n,cont):
    if(n==0):
        return []
    cad=sigma1(n-1,cont)
    for i in cad:
        unos.append(i)
        listas.append(cont)
        if i==0:
            logU.append(0)
        else:
            logU.append(int(math.log(i,10)))
        cont+=1
    cad=[]
    ant=1
    aux=0
    for i in range(2**(n-1),2**n):
        if i==(2**n)-1:
            sig=0
        
        else:
            sig=binario(i+1,n,0)

        if (ant<aux and aux>sig)or(ant>aux and aux<sig):
            unos.append(aux)
            cad.append(aux)
            listas.append(cont)
            if aux==0:
                logU.append(0)
            else:
                logU.append(int(math.log(aux,10)))
        ant=aux
        aux=sig
        cont+=1 
    print(n)
    return cad

unos=[]
logU=[]
listas=[]
# Generar uinverso n
conteo=1
n=26
print('\nGenerando el universo de n =',str(n)+'...\n')

unos.append(0)
logU.append(0)
listas.append(0)

sigma1(n,conteo)
print(len(unos))

plt.title('Logaritmo de unos por cadena universo n = '+str(n)) 
plt.xlabel('Cadena')
plt.ylabel('Unos')
plt.scatter(listas, unos, label='Elementos')
plt.scatter(listas, logU, label='Log Elementos')
plt.legend(loc='upper left')
plt.show()
