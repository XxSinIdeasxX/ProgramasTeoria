import matplotlib.pyplot as plt
import random
import math

def menu():
    print('\n\t\t    Menu\n============================================')
    print('1. Generar primos hasta n')
    print('2. Generar primos hasta n aleatorio')
    print('3. Generar gráficas para el conjunto anterior')
    print('4. Salir\n')
    op=int(input('Seleccione una opcion: '))
    while(op>4 or op<1):
        op=int(input('\t> Error <\n\nSeleccione una opcion valida: '))
    return op

def binario(n, unos, bits):
    if(n==0):
        return [unos, bits]
    aux=binario(n//2, unos, bits)
    unos=aux[0]
    bits=aux[1]
    if(n%2==1):
        unos+=1
    Pbin.write(str(n%2))
    return [unos, bits+1]

def esPrimo(n):
    if n==2:
        return True
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True        

def primos(n):
    while n<2:
        n=int(input('< n debe ser mayor o igual a 2 >\n\nIngrese un n valido: '))

    print('\nGenerando el conjunto de numeros primos hasta n =',str(n)+'...\n')
    numeros.clear()
    unos.clear()
    elementos.clear()
    Pbin.write('>>> Representacion binaria de primos hasta n = '+str(n)+'\n\nU = {10')
    Pdec.write('>>> Numeros primos hasta n = '+str(n)+'\n\nU = {2')
    numeros.append(2)
    unos.append(1)
    elementos.append(2)
    for i in range(3,n+1):
        if esPrimo(i):
            Pbin.write(', ')
            Pdec.write(', '+str(i))
            aux=binario(i, 0, 0)
            elementos.append(aux[1])
            unos.append(aux[0])
            numeros.append(i)
    Pbin.write('}\n\n')
    Pdec.write('}\n\n')
    print('Se generaron correctamente los primos hasta n =',n)

Pbin=open('PrimosBin.txt','w')
Pdec=open('PrimosDec.txt','w')

numeros=[]       # Número de cadena
elementos=[]    # Número de elementos por cadena
unos=[]         # Número de unos por cadena
while True:
    op=menu()
    if op==1:       # Primos hasta n
        n=int(input('\nIngrese el valor de n: '))
        primos(n)

    elif op==2:     # Primos con n aleatorio
        n=random.randint(1,20000000)
        primos(n)

    elif op==3:     # Generar gráficas
        if len(numeros)==0:
            print('\nNo se ha generado ningun conjunto de primos, por favor seleccione otra opcion')
        else:
            print('\nSe generaron las graficas para los primos hasta n =',str(n),'\nCierre las ventanas para continuar')
            
            logE=[]

            for i in elementos:
                if i==0:
                    logE.append(0)
                else:
                    logE.append(math.log(i, 10))

            plt.title('Elementos por numero primo')    
            plt.xlabel('Numero')
            plt.ylabel('Elementos')
            plt.plot(numeros, elementos, label='Elementos')
            plt.plot(numeros, logE, label='Log Elementos')
            plt.legend(loc='right')
            plt.show()

            logU=[]
            
            for i in unos:
                if i==0:
                    logU.append(0)
                else:
                    logU.append(math.log(i, 10))            

            plt.title('Unos por numero primo')    
            plt.xlabel('Numero')
            plt.ylabel('Unos')
            plt.plot(numeros, unos, label='Unos')
            plt.plot(numeros, logU, label='Log Unos')
            
            plt.legend(loc='upper left')
            plt.show()

    elif op==4:     # Salir
        print('\nHasta luego :D\n')
        break

Pbin.close()
Pdec.close()