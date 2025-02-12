# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 13:56:48 2024

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
            
        if a[0]!=0 or primero: #no se pueda imprimir un + 0 en caso de que no sea el primer termino, es decir solo haya una constante y hay que colocar el espacio de delante
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
    
grado1=int(input())
lista1=lee_lista(grado1+1)
grado2=int(input())
lista2=lee_lista(grado2+1)

suma=sumar_polinomios(lista1,lista2)
imprimir_polinomio(suma)
resta=restar_polinomios(lista1,lista2)
imprimir_polinomio(resta)