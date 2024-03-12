import os

def fnt_limpiarpantalla():
    os.system('cls')
    print('Sistema de control de inventario')
    print('Autor: Michell A. Mosquera P. (c) - 2024')
    print('Universidad católica Luis Amigo')
    print('\n\n')

def fnt_menu(repetir):
    while repetir == True:
        fnt_limpiarpantalla()
        opcionStr = input('---- MENU DE OPCIONES ----\n1. SUMAR\n2. RESTAR\n3. MULTIPLICAR\n4. DIVIDIR\n--> ')
        if opcionStr == 'F' or opcionStr == 'f':
                repetir = False 
        else:
            if int(opcionStr) >= 1 and int(opcionStr) <= 4:
                numero1Flt = float(input('Ingrese el primer numero:'))
                numero2Flt = float(input('Ingrese el segundo numero:'))
                fnt_operaciones(numero1Flt, numero2Flt,opcionStr)
                
            else:
                print('\nOpcion incorrecta')
                enter = input('\n<ENTER>')
        
def fnt_operaciones(n1,n2,op):
    if op == '1':
        resultadoFlt =  n1 + n2
        operadorStr = '+'
    if op == '2':
        resultadoFlt =  n1 - n2
        operadorStr = '-'
    if op == '3':
        resultadoFlt =  n1 * n2
        operadorStr = 'x'
    if op == '4':
        if n2 == 0:
            enter = input('\n No se puede dividir por 0 <ENTER>')
        else:
            resultadoFlt =  n1 / n2
            operadorStr = '/'
    print(n1,' ', operadorStr, ' ', n2, '=', resultadoFlt)
    enter = input('\n<ENTER>')
    
fnt_menu(True)
