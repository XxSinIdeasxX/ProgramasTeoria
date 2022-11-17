import random
import webbrowser
from tkinter import *

def menu():
    print('\n\t\t    Menu\n============================================')
    print('1. Verificar si el protocolo esta encendido')
    print('2. Generar el AFD')
    print('3. Salir\n')
    op=int(input('Seleccione una opcion: '))
    while(op<1 or op>3):
        print('\n\t> Error <\n')
        op=int(input('Seleccione una opcion valida: '))
    return op

def grafo():
    ventana = Tk()
    ventana.wm_attributes("-topmost", True)
    ventana.resizable(False, False)
    ancho = 400
    alto = 300
    canv = Canvas(ventana, width=ancho, height=alto)

    ventana.title('Grafo protocolo e imparidad')
    canv.pack()

    canv.create_line(30,alto/2-75, 175,alto/2-75, width=2)
    canv.create_line(100,alto/2-75, 100,alto/2+35, width=2)
    canv.create_rectangle(200,alto/2-85, 300, alto/2-65,width=2)
    canv.create_rectangle(200,alto/2+40, 300, alto/2+60,width=2)
    canv.create_rectangle(315,alto/2-80, 335, alto/2+40,width=2)
    canv.create_rectangle(210,alto/2-80, 190, alto/2+40,width=2)

    canv.create_polygon(75,alto/2-75, 66,alto/2-80, 66,alto/2-70)
    canv.create_polygon(175,alto/2-75, 166,alto/2-80, 166,alto/2-70)
    canv.create_polygon(222,alto/2-85, 231,alto/2-90, 231,alto/2-80)
    canv.create_polygon(299,alto/2-65, 290,alto/2-70, 290,alto/2-60)
    canv.create_polygon(226,alto/2+40, 235,alto/2+45, 235,alto/2+35)
    canv.create_polygon(299,alto/2+60, 290,alto/2+65, 290,alto/2+55)
    canv.create_polygon(100,alto/2+21, 105,alto/2+12, 95,alto/2+12)
    canv.create_polygon(190,alto/2+24, 195,alto/2+16, 185,alto/2+16)
    canv.create_polygon(315,alto/2+24, 320,alto/2+15, 310,alto/2+15)
    canv.create_polygon(210,alto/2-53, 215,alto/2-44, 205,alto/2-44)
    canv.create_polygon(335,alto/2-49, 330,alto/2-40, 340,alto/2-40)

    canv.create_oval(75,alto/2-50, 125,alto/2-100, width=2, fill='white') # Q0
    canv.create_oval(175,alto/2-50, 225,alto/2-100, width=2, fill='white')# Q2
    canv.create_oval(296,alto/2-46, 354,alto/2-104, width=2, fill='white')
    canv.create_oval(300,alto/2-50, 350,alto/2-100, width=2, fill='white')# Q3
    canv.create_oval(296,alto/2+21, 354,alto/2+79, width=2, fill='white')
    canv.create_oval(300,alto/2+25, 350,alto/2+75, width=2, fill='white') # Q5
    canv.create_oval(171,alto/2+21, 229,alto/2+79, width=2, fill='white')
    canv.create_oval(175,alto/2+25, 225,alto/2+75, width=2, fill='white') # Q4
    canv.create_oval(71,alto/2+21, 129,alto/2+79, width=2, fill='white')
    canv.create_oval(75,alto/2+25, 125,alto/2+75, width=2, fill='white')  # Q1

    Label(ventana,text='Start', font = ('Arial', 11)).place(x=30, y=alto/2-90, anchor='center')
    Label(ventana,text='ON', font = ('Arial', 11)).place(x=150, y=alto/2-90, anchor='center')
    Label(ventana,text='1', font = ('Arial', 11)).place(x=263, y=alto/2-90, anchor='s')
    Label(ventana,text='1', font = ('Arial', 11)).place(x=263, y=alto/2-58, anchor='n')
    Label(ventana,text='1', font = ('Arial', 11)).place(x=263, y=alto-115, anchor='s')
    Label(ventana,text='1', font = ('Arial', 11)).place(x=263, y=alto-83, anchor='n')

    Label(ventana,text='OFF', font = ('Arial', 11)).place(x=95, y=alto/2-10, anchor='e')
    Label(ventana,text='0', font = ('Arial', 11)).place(x=215, y=alto/2-10, anchor='w')
    Label(ventana,text='0', font = ('Arial', 11)).place(x=185, y=alto/2-10, anchor='e')
    Label(ventana,text='0', font = ('Arial', 11)).place(x=340, y=alto/2-10, anchor='w')
    Label(ventana,text='0', font = ('Arial', 11)).place(x=310, y=alto/2-10, anchor='e')

    Label(ventana, text='Q0', font = ('Arial', 11), background='white').place(x=100, y=alto/2-75, anchor='center')
    Label(ventana, text='Q1', font = ('Arial', 11), background='white').place(x=100, y=alto/2+50, anchor='center')
    Label(ventana, text='Q2', font = ('Arial', 11), background='white').place(x=200, y=alto/2-75, anchor='center')
    Label(ventana, text='Q3', font = ('Arial', 11), background='white').place(x=325, y=alto/2-75, anchor='center')
    Label(ventana, text='Q4', font = ('Arial', 11), background='white').place(x=200, y=alto/2+50, anchor='center')
    Label(ventana, text='Q5', font = ('Arial', 11), background='white').place(x=325, y=alto/2+50, anchor='center')

    ventana.mainloop()

def binario(n,elem,l):
    if(n==0):
        while(elem>0):
            l=l+'0'
            elem-=1
        return l
    l=binario(n//2,elem-1,l)
    l=l+str(n%2)
    return l

def impar(l, i):
    q=2
    historial.write('Cadena '+str(i)+': q0-q2')
    for i in l:
        if i=='0':
            if q==2: q=4
            elif q==3: q=5
            elif q==4: q=2
            elif q==5: q=3
        else:
            if q==2: q=3
            elif q==3: q=2
            elif q==4: q=5
            elif q==5: q=4
        historial.write('-q'+str(q))
    historial.write('\n\n')
    if q==2: return False
    else: return True

def cadenas(n):
    l=""
    l=binario(random.randint(0,(2**64)-1),64,l)

    cad.write('Ejecución '+n+'\n\n'+str(l))
    aceptadas.write('Ejecución '+n+'\n\n')
    rechazadas.write('Ejecución '+n+'\n\n')
    historial.write('Ejecución '+n+'\n\n')
    
    if impar(l,1): aceptadas.write(str(l)+'  ')
    else: rechazadas.write(str(l)+'  ')

    for i in range(2, 1000001):
        l=""
        l=binario(random.randint(0,(2**64)-1),64,l)
        cad.write(', '+str(l))

        if(impar(l, i)): aceptadas.write(str(l)+'  ')
        else: rechazadas.write(str(l)+'  ')
        
    cad.write('\n\n')
    aceptadas.write('\n\n')
    rechazadas.write('\n\n')
    historial.write('\n\n')


cad = open('Cadenas.txt', 'w')
aceptadas = open('Impares.txt', 'w')
rechazadas = open('Pares.txt', 'w')
historial = open('Historial.txt', 'w')
n=1     # Contador de ejecuciones totales del automata

while True:
    op=menu()
    if op==1:       # Protocolo
        if(random.randint(0,1)==1):     # Protocolo on off?
            i=0
            x=1
            print('\nEl protocolo esta encendido, el automata se esta ejecutando')
            while(x==1):
                cadenas(str(n))
                n+=1    # Contador de ejecuciones totales del automata
                i+=1    # Contador de ejecuciones parciales del automata
                x=random.randint(0,1)   # Protocolo on off?i,'\n'
            print('\nEjecuciones del automata:',i,'\n')
        else:
            print('\nEl protocolo esta apagado\n')

    elif op==2:     # Grafo
        grafo()

    elif op==3:     # Salir
        print('\nHasta luego :D\n')
        cad.close()
        aceptadas.close()
        rechazadas.close()
        break

## NOTA: Es necesario finalizar la ejecución del programa para poder visualizar los .txt