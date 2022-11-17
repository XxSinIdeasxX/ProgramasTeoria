from tkinter import *
import time
import random

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

def maquina(cadena):
    Acepta = False
    animacion = False
    cad=[]
    
    cad.append('-')
    for i in cadena:
        cad.append(i)
    cad.append('-')

    if len(cadena) <= 10:
        animacion = True
        ventana = Tk()
        ventana.wm_attributes("-topmost", True)
        ventana.resizable(False, False)
        ancho = 300
        alto = 200
        canv = Canvas(ventana, width=ancho, height=alto)
        
        ventana.title('Maquina de Turing')
        canv.pack()
        canv.create_rectangle(((ancho/2)-20), 80, ((ancho/2)+20), 40, width=2, fill='white')
        canv.create_polygon((ancho/2), 105, ((ancho/2)-15), 85, ((ancho/2)+15), 85)
        canv.create_rectangle(5,110,ancho-5,109)
        canv.create_rectangle(5,140,ancho-5,141)
        for i in range(9):
            canv.create_rectangle(15+(30*i), 110, 45+(30*i), 140, fill='white')

    with open('Registro.txt', 'a', encoding='utf-8') as reg:
        reg.write('Registro evaluación de la máquina de Turing\n\n'+cadena+'\n1'+''.join(cad[2:-1])+'\n')
        estado = 1
        i = 1
        while True:
            try:
                if animacion:
                    Label(ventana,text=str(estado), background='white', font = 12).place(x=ancho/2, y=60, anchor='center')
                    Label(ventana, text='Cinta: '+''.join(cad),font=('Arial',12)).place(x=ancho/2, y=alto-15, anchor='s')
                    for j in range(i-4,i+5):
                        if j<0 or j>len(cad)-1:
                            Label(ventana, text='-', background='white', font = ('Arial', 10)).place(x=ancho/2+(30*(j-i)), y=125, anchor='center')
                        else:
                            Label(ventana, text=cad[j], background='white', font = ('Arial', 10)).place(x=ancho/2+(30*(j-i)), y=125, anchor='center')
                    ventana.update()
                    time.sleep(1)
            except:
                animacion=False
            caracter = cad[i]
            if estado == 1:
                if caracter == '*':
                    cad[i] = 'X'
                    i += 1
                    estado = 2
                else:
                    break
            elif estado == 2:
                if caracter == '*':
                    i += 1
                    estado = 3
                elif caracter == '|':
                    i += 1
                else:
                    break
            elif estado == 3:
                if caracter == '*':
                    cad[i]='X'
                    i -= 1
                    estado = 4
                elif caracter == '|':
                    i += 1
                else:
                    break
            elif estado == 4:
                if caracter == '*':
                    i -= 1
                elif caracter == '|':
                    cad[i]='a'
                    i += 1
                    estado = 5
                elif caracter == 'X':
                    i += 1
                    estado = 7
                else:
                    break
            elif estado == 5:
                if caracter == '-':
                    cad[i] = '|'
                    cad.append('-')
                    i -= 1
                    estado = 6
                elif caracter == '*':
                    i += 1
                elif caracter == '|':
                    i += 1
                elif caracter == 'X':
                    i += 1
                else:
                    break
            elif estado == 6:
                if caracter == '*':
                    i -= 1
                elif caracter == '|':
                    i -= 1
                elif caracter == 'a':
                    cad[i] = '|'
                    i -= 1
                    estado = 4
                elif caracter == 'X':
                    i -= 1
                else:
                    break
            elif estado == 7:
                if caracter == '*':
                    i += 1
                    estado = 8
                elif caracter == '|':
                    i += 1
                else:
                    break
            elif estado == 8:
                if caracter == '-':
                    cad[i] = '*'
                    cad.append('-')
                    i -= 1
                    estado = 9
                elif caracter == '|':
                    i += 1
                elif caracter == 'X':
                    cad[i] = '*'
                    i += 1
                else:
                    break
            elif estado == 9:
                if caracter == '*':
                    i -= 1
                elif caracter == '|':
                    i -= 1
                elif caracter == 'X':
                    cad[i] = '*'
                    Acepta = True
                    break
                else:
                    break
            reg.write(''.join(cad[1:i])+str(estado)+''.join(cad[i+1:-1])+'\n')
        
        if Acepta:
            reg.write(''.join(cad[1:i])+'f'+''.join(cad[i+1:-1])+'\n\n\n')
            if animacion:
                Label(ventana,text='f', background='white', font = 12).place(x=ancho/2, y=60, anchor='center')
                Label(ventana, text='*', background='white', font = ('Arial', 10)).place(x=ancho/2, y=125, anchor='center')
                ventana.update()
                time.sleep(2)
                ventana.destroy()
            return 'Aceptada '+''.join(cad[1:-1])
        reg.write('\n\n\n')
        if animacion:
            time.sleep(2)
            ventana.destroy()
        return 'Rechazada '+''.join(cad[1:-1])

open('Registro.txt','w').close()

while True:
    op=menu()
    if op==1:       # Ingresar una cadena
        print('\nEvaluacion finalizada: ',maquina(input('\nIngrese la cadena a evaluar: ')))

    elif op==2:     # Generar una cadena
        cad=''

        if random.randint(0,2): cad+='*'
        else: cad+='|'

        for i in range(random.randint(0,49)):
            if random.randint(0,10): cad+='|'
            else: cad+='*'
            
        print('Cadena generada:',cad,'\nEvaluacion finalizada: ',maquina(cad))

    elif op==3:     # Salir
        print('\nHasta luego :D\n')
        break