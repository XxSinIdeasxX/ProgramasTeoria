import matplotlib.pyplot as plt
import random
import math

def menu():
    print('\n\t\t    Menu\n============================================')
    print('1. Generar uinverso n')
    print('2. Generar univerrso con n aleatorio')
    print('3. Generar gráficas para el universo anterior')
    print('4. Salir\n')
    op=int(input('Seleccione una opcion: '))
    while(op>4 or op<1):
        print('\n\t> Error <\n')
        op=int(input('Seleccione una opcion valida: '))
    return op

def binario(n, elem, conteo):
    if(n==0):
        while(elem>0):
            doc.write('0')
            elem-=1
        return conteo
    conteo=binario(n//2,elem-1,conteo)
    if(n%2==1):
        conteo+=1
    doc.write(str(n%2))
    return conteo

def sigma(n):
    if(n==0):
        return
    sigma(n-1)
    for i in range (2**n):
        doc.write(', ')
        elementos.append(n)
        unos.append(binario(i,n,0))
        cad.append(cad[-1]+1)

doc=open('Universo.txt','w')

elementos=[]    # Número de elementos por cadena
unos=[]         # Número de unos por cadena
cad=[]          # Número de cadenas distintas

while True:
    op=menu()
    if op==1:       # Generar uinverso n
        unos.clear()
        elementos.clear()
        cad.clear()
        n=int(input('\nIngrese el valor de n: '))
        print('\nGenerando el universo de n =',str(n)+'...\n')
        doc.write('>>> Universo de n = '+str(n)+'\n\nU = {e')
        cad.append(0)
        unos.append(0)
        elementos.append(0)
        sigma(n)
        doc.write('}\n\n')
        print('Se genero correctamente el universo de n =',n)

    elif op==2:     # Generar univerrso con n aleatorio
        cad.clear()
        unos.clear()
        elementos.clear()
        n=random.randint(1,1000)
        print('\nGenerando el universo de n =',str(n)+'...\n')
        doc.write('>>> Universo de n = '+str(n)+'\n\nU = {e')
        cad.append(0)
        unos.append(0)
        elementos.append(0)
        sigma(n)
        doc.write('}\n\n')
        print('Se genero correctamente el universo de n =',n)

    elif op==3:     # Generar gráficas para en universo anterior
        if len(cad)==0:
            print('\nNo se ha generado ningun universo, por favor seleccione otra opcion')
        else:
            print('\nSe generaron las graficas para el universo n =',str(n)+', cierre las ventanas para continuar')
            
            logE=[]

            for i in elementos:
                if i==0:
                    logE.append(0)
                else:
                    logE.append(math.log(i, 10))

            plt.title('Elementos por cadena universo n = '+str(n))    
            plt.xlabel('Cadena')
            plt.ylabel('Elementos')
            plt.plot(cad, elementos, label='Elementos')
            plt.plot(cad, logE, label='Log Elementos')
            plt.legend(loc='right')
            plt.show()

            logU=[]
            
            for i in unos:
                if i==0:
                    logU.append(0)
                else:
                    logU.append(math.log(i, 10))            

            plt.title('Unos por cadena universo n = '+str(n))    
            plt.xlabel('Cadena')
            plt.ylabel('Unos')
            plt.plot(cad, unos, label='Unos')
            plt.plot(cad, logU, label='Log Unos')
            
            plt.legend(loc='upper left')
            plt.show()

    elif op==4:     # Salir
        print('\nHasta luego :D\n')
        break
doc.close()