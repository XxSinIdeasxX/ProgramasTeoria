import random
from tkinter import *
import time

class Nodo:
    def __init__(self):
        self.sig = None
        self.dato = 'X'

class Pila:
    def __init__(self):
        self.size = 0
        self.superior = None

    def push(self):
        # Si no hay datos, agregamos el valor en el elemento superior
        if self.superior == None:
            self.superior = Nodo()
            self.size += 1
            return

        nuevo_nodo = Nodo()
        nuevo_nodo.sig = self.superior
        self.superior = nuevo_nodo
        self.size += 1

    def pop(self):
        # Si no hay datos en la pila
        if self.superior == None:
            return -1

        self.superior = self.superior.sig
        self.size -= 1
        
    
    def estado(self):
        aux = 'Z'
        for i in range(self.size):
            aux = 'X'+aux
        return aux
    
    def getSize(self):
        return self.size

def menu():
    print('\n\t\t    Menu\n============================================')
    print('1. Ingresar una cadena')
    print('2. Generar una cadena aleatoria')
    print('3. Salir\n')
    op=int(input('Seleccione una opcion: '))
    while(op<1 or op>3):
        print('\n\t> Error <\n')
        op=int(input('Seleccione una opcion valida: '))
    return op

def automata(cad):
    animacion=False

    if len(cad) <= 10:
        animacion=True
        bloques=[]
        ventana = Tk()
        ventana.wm_attributes("-topmost", True)
        ancho = 500
        alto = 300
        canv = Canvas(ventana, width=ancho, height=alto)

        ventana.title('Automata de pila')
        canv.pack()

        Label(ventana,text='push', font = 12).place(x=125, y=alto/2-85, anchor='s')
        Label(ventana,text='0', font = 12).place(x=125, y=alto/2-82, anchor='n')
        Label(ventana,text='q',background='white', font = 12).place(x=125, y=alto/2-25, anchor='center')

        Label(ventana,text='pop', font = 12).place(x=225, y=alto/2-85, anchor='s')
        Label(ventana,text='1', font = 12).place(x=225, y=alto/2-82, anchor='n')
        Label(ventana,text='p',background='white', font = 12).place(x=225, y=alto/2-25, anchor='center')

        Label(ventana,text='f',background='white', font = 12).place(x=325, y=alto/2-25, anchor='center')

        Label(ventana,text='Start', font = 12).place(x=50, y=alto/2-26, anchor='s')
        Label(ventana,text='pop', font = 12).place(x=175, y=alto/2-26, anchor='s')
        Label(ventana,text='1', font = 12).place(x=175, y=alto/2-23, anchor='n')
        Label(ventana,text='Z', font = 12).place(x=275, y=alto/2-26, anchor='s')
        Label(ventana,text='ε', font = 12).place(x=275, y=alto/2-23, anchor='n')

        canv.create_line(50,alto/2-25, 300,alto/2-25, width=2)
        canv.create_oval(105,alto/2-45, 145,alto/2-85, width=2)
        canv.create_oval(205,alto/2-45, 245,alto/2-85, width=2)

        canv.create_oval(100,alto/2, 150,alto/2-50, width=2, fill='white', outline='red')
        canv.create_oval(200,alto/2, 250,alto/2-50, width=2, fill='white')
        canv.create_oval(296,alto/2+4, 354,alto/2-54, width=2, fill='white')
        canv.create_oval(300,alto/2, 350,alto/2-50, width=2, fill='white')

        canv.create_polygon(100,alto/2-25, 94,alto/2-30, 94,alto/2-20)
        canv.create_polygon(200,alto/2-25, 194,alto/2-30, 194,alto/2-20)
        canv.create_polygon(296,alto/2-25, 290,alto/2-30, 290,alto/2-20)

        for i in range(len(cad)):
            canv.create_line(42+30*i,alto/2+70, 68+30*i,alto/2+70, width=2)
            Label(ventana, text=cad[i], font = 12).place(x=55+30*i, y=alto/2+69, anchor='s')

        flecha=canv.create_polygon(55,alto/2+75, 50,alto/2+85, 60,alto/2+85,tags='flecha')

        canv.create_line(ancho-80,alto-60, ancho-10,alto-60, width=2)
        Label(ventana, text='Z', font = 12).place(x=ancho-45, y=alto-59, anchor='n')

    with open('Evaluación.txt', 'a', encoding='utf-8') as reg:
        reg.write('Registro evaluación del autómata de pila\n\n')
        aceptada=True
        pila = Pila()
        estado = 'q'
        i=0
        while cad != '':

            caracter = cad[0]
            reg.write('('+estado+', '+cad+', '+pila.estado()+')')
            if estado == 'q':
                if caracter == '0':
                    pila.push()

                elif caracter == '1':
                    estado = 'p'
                    if pila.pop() == -1:
                        aceptada=False
                        break

                else:
                    aceptada=False
                    break

            elif estado == 'p':
                if caracter == '1':
                    if pila.pop() == -1:
                        aceptada=False
                        break

                elif caracter == '0':
                    aceptada=False
                    break

                else:
                    aceptada=False
                    break

            if animacion:
                if estado=='q':
                    canv.create_oval(100,alto/2, 150,alto/2-50, width=2, fill='white', outline='red')
                    canv.create_oval(200,alto/2, 250,alto/2-50, width=2, fill='white')
                elif estado=='p':
                    canv.create_oval(100,alto/2, 150,alto/2-50, width=2, fill='white')
                    canv.create_oval(200,alto/2, 250,alto/2-50, width=2, fill='white', outline='red')
                
                canv.delete(flecha)
                flecha=canv.create_polygon(55+30*i,alto/2+75, 50+30*i,alto/2+85, 60+30*i,alto/2+85)
                
                if len(bloques)>0:
                    for k in bloques:
                        canv.delete(k)

                texBloques=['  ','  ','  ','  ','  ','  ','  ','  ','  ','  ']

                for j in range(len(pila.estado())-1):
                    bloques.append(canv.create_rectangle(ancho-65, alto-61-(20*j), ancho-25, alto-85-(20*j), width=2, fill='white'))
                    texBloques[j]='X'

                for l in range(10):
                    Label(ventana, text=texBloques[l], font = ('Arial', 12)).place(x=ancho-45, y=alto-61-(20*l), anchor='s') 

                ventana.update()
                time.sleep(1)

            reg.write(' » ')
            cad = cad[1:]
            i+=1

        if animacion:
            if estado=='q':
                canv.create_oval(100,alto/2, 150,alto/2-50, width=2, fill='white', outline='red')
                canv.create_oval(200,alto/2, 250,alto/2-50, width=2, fill='white')
            elif estado=='p':
                canv.create_oval(100,alto/2, 150,alto/2-50, width=2, fill='white')
                canv.create_oval(200,alto/2, 250,alto/2-50, width=2, fill='white', outline='red')
        
        if pila.getSize()>0:
            aceptada=False

        if aceptada:
            reg.write('(f , ε, Z)\n\n')
            if animacion:
                canv.create_oval(100,alto/2, 150,alto/2-50, width=2, fill='white')
                canv.create_oval(200,alto/2, 250,alto/2-50, width=2, fill='white')
                canv.create_oval(296,alto/2+4, 354,alto/2-54, width=2, fill='white', outline='red')
                canv.create_oval(300,alto/2, 350,alto/2-50, width=2, fill='white', outline='red')
            return 'La cadena es parte del lenguaje'
        else:
            if len(cad)==0:
                reg.write('('+estado+', ε, '+pila.estado()+')\n\n')
            else:
                reg.write('\n\n')
            return 'La cadena no es parte del lenguaje'

open('Evaluación.txt','w').close()

while True:
    op=menu()
    if op==1:       # Ingresar una cadena
        print('\nEvaluacion finalizada: ',automata(input('\nIngrese la cadena a evaluar: ')))

    elif op==2:     # Generar una cadena
        cad=''
        n = random.randint(1,100000)
        print('\nCadena generada con',n,'caracteres')
        aux=random.randint(1,n)
        for i in range(aux):
            cad += '0'
        for i in range(n-aux):
            cad += '1'
        print('\nEvaluacion finalizada: ',automata(cad))


    elif op==3:     # Salir
        print('\nHasta luego :D\n')
        break