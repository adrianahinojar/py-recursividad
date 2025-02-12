# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 19:07:57 2024

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

        
def encontrar_elemento_en_posicion(a,inicio,fin):

    if inicio>fin:#caso base
        return -1
    
    mitad=(inicio+fin)//2
    
    if a[mitad]==mitad:
        return mitad
    
    resultado_izq = encontrar_elemento_en_posicion(a, inicio, mitad - 1)  # primero buscar en la mitad de la izquierda
    if resultado_izq != -1:
        return resultado_izq #devolver el resultado si el valor y su posicion coinciden (si no se encuentra resultado_izq sería un -1)
    
    return encontrar_elemento_en_posicion(a, mitad + 1, fin)  # sino hay que buscar en la mitad de la derecha


n=int(input())
lista = list(map(int, input().split()))
#lista=lee_lista(n) DA ERROR EL LEE_LISTA timelimit error
resultado=encontrar_elemento_en_posicion(lista,0,n-1)
print(resultado)