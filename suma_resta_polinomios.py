# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 18:32:46 2024

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
            
        if a[0]!=0: 
            print(f" {signo} {abs(a[0])}")
        elif primero:#no se pueda imprimir un + 0 en caso de que no sea el primer termino, es decir solo haya una constante y hay que colocar el espacio de delante
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
        
def sumar_restar_polinomios(a,b,suma=None, resta=None):
    #si no existe iniciarlizar la lista suma y resta que será necesario para imprimirla con el metodo
    if suma is None:
        suma=[]
    if resta is None:
        resta=[]
    
    if len(a)==0 and len(b)==0: #ya no hay nada que sumar o restar,caso base
        imprimir_polinomio(suma)
        imprimir_polinomio(resta)
        return
    
    if len(a)>0:
        coeficiente_a=a[0]
    else:
        coeficiente_a=0 #no tiene valor hacer los calculos usando un 0
        
    if len(b)>0:
        coeficiente_b=b[0]
    else:
        coeficiente_b=0    
    
    suma_coeficiente= coeficiente_a + coeficiente_b
    resta_coeficiente= coeficiente_a - coeficiente_b
    
    suma +=[suma_coeficiente] # concatenar el resultado a sus respectivas listas 
    resta +=[resta_coeficiente]
    
    sumar_restar_polinomios(a[1:],b[1:],suma,resta)

grado1=int(input())
lista1=lee_lista(grado1+1)
grado2=int(input())
lista2=lee_lista(grado2+1)

print(lista1,lista2)

sumar_restar_polinomios(lista1,lista2)