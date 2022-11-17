import os
from tkinter import *

## import random
## with open('Prueba.txt','w') as doc:
##     a='wepsbaigtmyr '
##     for i in range(1000000):
##         doc.write(a[random.randint(0,12)])

def menu():
    print('\n\t\t    Menu\n============================================')
    print('1. Ejecutar el automata')
    print('2. Generar los grafos')
    print('3. Salir\n')
    op=int(input('Seleccione una opcion: '))
    while(op<1 or op>3):
        print('\n\t> Error <\n')
        op=int(input('Seleccione una opcion valida: '))
    return op

def archivo():
    while True:
        aux=str(input('\nIngrese el nombre o ruta del archivo: '))
        if os.path.exists(aux):
            return aux
        else:
            print('\n'+aux+' no se encontro o no se puede leer, intentelo de nuevo')

def resultados(cont,tex):
    with open('Resultados.txt','a') as res:
        res.write('Conteo de palabras para '+tex+'\n\tweb: '+str(len(cont[0]))+'\n\t')        
        res.write('page: '+str(len(cont[1]))+'\n\t')
        res.write('site: '+str(len(cont[2]))+'\n\t')
        res.write('ebay: '+str(len(cont[3]))+'\n\t')
        res.write('webpage: '+str(len(cont[4]))+'\n\t')
        res.write('website: '+str(len(cont[5]))+'\n\t')
        res.write('webmaster: '+str(len(cont[6]))+'\n\n')

        res.write('Posiciones\n\n- web -\n'+str(cont[0])+'\n\n')
        res.write('- page -\n'+str(cont[1])+'\n\n')
        res.write('- site -\n'+str(cont[2])+'\n\n')
        res.write('- ebay -\n'+str(cont[3])+'\n\n')
        res.write('- webpage -\n'+str(cont[4])+'\n\n')
        res.write('- website -\n'+str(cont[5])+'\n\n')
        res.write('- webmaster -\n'+str(cont[6])+'\n\n\n')
        print('\nBusqueda finalizada')

def automata(tex):
    web=[]
    page=[]
    site=[]
    ebay=[]
    webpage=[]
    website=[]
    webmaster=[]

    q=0
    with open(tex, 'r') as doc:
        aux=doc.read(1).lower()     # Primer caracter del documento

        with open('Registro.txt', 'a', encoding='utf-8') as reg:
            reg.write('\t\tRegistro ejecución del autómata para '+tex+'\n\n(q0, ε)')

            print('\nEl automata se esta ejecutando...')
            while aux!='':
                # Evaluaciones del automata
                if aux=='w': q=1
                elif aux=='e':
                    if q==1: q=2
                    elif q==24:     # page
                        q=25
                        page.append(doc.tell())
                    elif q==28:     # site
                        q=29
                        site.append(doc.tell())
                    elif q==6:      # webpage page
                        reg.write(' - (q7, e)')
                        aux='ε'
                        q=25
                        webpage.append(doc.tell())
                        page.append(doc.tell())
                    elif q==10:     # website site
                        reg.write(' - (q11, e)')
                        aux='ε'
                        q=29
                        website.append(doc.tell())
                        site.append(doc.tell)
                    elif q==15: q=16
                    else: q=18
                elif aux=='p':
                    if q==3: q=4
                    else: q=22
                elif aux=='s':
                    if q==3: q=8
                    elif q==13: q=14
                    else: q=26
                elif aux=='b':
                    if q==18: q==19
                    elif q==2:      # web
                        q=3
                        web.append(doc.tell())
                    else: q=0
                elif aux=='a':
                    if q==22: q=23
                    elif q==19: q=20
                    elif q==3: q=20
                    elif q==4: q=5
                    elif q==12: q=13
                    else: q=0
                elif aux=='i':
                    if q==26: q=27
                    elif q==8: q=9
                    else: q=0
                elif aux=='g':
                    if q==23: q=24
                    elif q==5: q=6
                    else: q=0
                elif aux=='t':
                    if q==27: q=28
                    elif q==9: q=10
                    elif q==14: q=15
                    else: q=0
                elif aux=='m':
                    if q==3: q=12
                    else: q=0
                elif aux=='y':
                    if q==20:   # ebay
                        q=21
                        ebay.append(doc.tell())
                    else: q=0
                elif aux=='r':
                    if q==16:   # webmaster
                        q=17
                        webmaster.append(doc.tell())
                    else: q=0

                reg.write(' - (q'+str(q)+', '+aux.encode('unicode-escape').decode()+')')
                aux=doc.read(1).lower()
            reg.write('\n\n')
    resultados([web, page, site, ebay, webpage, website, webmaster], tex)

def grafo():
    ancho = 500
    alto = 300
    
    ventana = Tk()
    canv = Canvas(ventana, width=ancho, height=alto)
    ventana.title('Grafo DFA diccionario')
    canv.pack()
    
    ventana.mainloop()

open('Registro.txt','w').close()
open('Resultados.txt','w').close()

while True:
    op=menu()
    if op==1:       # Diccionario
        automata(archivo())

    elif op==2:     # Grafos
        grafo()

    elif op==3:     # Salir
        print('\nHasta luego :D\n')
        break