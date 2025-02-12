# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 17:14:36 2024

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
                print(f" {signo} {abs(coeficiente)}x^{grado}", end=" ")#como imprimir el primer término que coloque un espacio al principio
            
            else:
                print(f"{signo} {abs(coeficiente)}x^{grado}", end=" ")#al terminar la cadena colocar un espaciono salto de linea
            
            primero=False
                  
        imprimir_polinomio(a[:-1],primero)
            

grado=int(input())
lista=lee_lista(grado+1)

imprimir_polinomio(lista)