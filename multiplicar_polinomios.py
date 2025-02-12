# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 20:30:13 2024

@author: ahino
"""

def lee_lista(n):  
    a = []
    if n>0:
        cadenaEntrada = input()
        for i in range(0, n): 
            elemento = int(cadenaEntrada.split(" ")[i])
            a.append(elemento)
            
    return a


def imprimir_polinomio(a,primero=True):
    grado=len(a)-1
        
    if grado==0:  #caso base
        coeficiente=a[0]
        if coeficiente<0:
            signo="-"
        else:
            signo="+"
            
        if a[0]!=0 or primero:#no se pueda imprimir un + 0 en caso de que no sea el primer termino, es decir solo haya una constante y hay que colocar el espacio de delante 
            print(f" {signo} {abs(a[0])}")
            
    else:
        coeficiente= a[grado]
        if coeficiente!=0:#no se pueda imprimir un + 0x^..
            if coeficiente<0:
                signo="-"
            else:
                signo="+"
            
            if primero:
                print(f" {signo} {abs(coeficiente)}x^{grado}", end=" ")#como imprimer el primer término que coloque un espacio al principio
            
            else:
                print(f"{signo} {abs(coeficiente)}x^{grado}", end=" ")#al terminar la cadena colocar un espaciono salto de linea
            
            primero=False
                  
        imprimir_polinomio(a[:-1],primero)
 
        
def sumar_polinomios(a,b):
    if len(a)==1:
        return [a[0]+b[0]] + b[1:]
    if len(b)==1:
        return [a[0]+b[0]] + a[1:]
    
    return [a[0]+b[0]] + sumar_polinomios(a[1:],b[1:])

def restar_polinomios(a,b):
    if len(a)==1:#a solo tiene un termino
        if len(b)>1:#b tiene mas de un termino que restar 
            return [a[0]-b[0]] + [-x for x in b[1:]]#se resta el primer elemento de b y el resto se les cambia al signo opuesto que tenian al tratatarse de una resta
        else:
            return [a[0]-b[0]]#tanto a como b solo les queda 1 elemento se restan y punto
    if len(b)==1:
        if len(a)>1:#solo queda un elemento en b y a tiene mas se hace la resta y se añade a los que quedan de a
            return [a[0]-b[0]] + a[1:]
        else:#ambos polinomios tiene solo un elemento
            return [a[0]-b[0]] 
    
    return [a[0]-b[0]] + restar_polinomios(a[1:],b[1:])

def multiplicar_polinomios_karatsuba(x, y):
    if len(x)==1 and len(y)==1:#caso base: ambas listas de tamaño 1
       return [x[0] * y[0]]
    if len(x)==1:
        return [x[0]*y[i] for i in range(len(y))] #una de las listas de tamaño 1
    if len(y)==1:
       return [y[0]*x[i] for i in range(len(x))]
   
    m=min(len(x)//2, len(y)//2)
    
    a = x[:m]
    b = x[m:]
    c = y[:m]
    d = y[m:]

    ac = multiplicar_polinomios_karatsuba(a, c)
    bd = multiplicar_polinomios_karatsuba(b, d)

    suma_a_b = sumar_polinomios(a, b)
    suma_c_d = sumar_polinomios(c, d)

    t = multiplicar_polinomios_karatsuba(suma_a_b, suma_c_d)
    t = restar_polinomios(t, ac)
    t = restar_polinomios(t, bd)

    resultado = [0] * (len(x) + len(y) - 1)  # Inicializar resultado con el tamaño correcto a todo 0's

    for i in range(len(ac)):
        resultado[i] += ac[i]#añade los coeficientes del polinomio ac al resultado en la parte baja

    for i in range(len(t)):
        resultado[i + m] += t[i]#se desplaza para añadir los coeficientes de t en la parte media

    for i in range(len(bd)):
        resultado[i + 2 * m ] += bd[i]#se desplaza mas aun para añadir los coeficientes de bd en la parte alta del producto

    return resultado

grado1=int(input())
lista1=lee_lista(grado1+1)
grado2=int(input())
lista2=lee_lista(grado2+1)
resultado=multiplicar_polinomios_karatsuba(lista1,lista2)
imprimir_polinomio(resultado)