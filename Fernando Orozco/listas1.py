#!/usr/bin/python -tt
# -*- coding: UTF-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Ejercicios básicos de listas
# Llenar el código de las funciones abajo. main() ya está armado
# para llamar a las funciones con algunas entradas,
# imprime 'OK' cuando cada función es correcta.
# El código inicial para cada función incluye un 'return'
# que es sólo un comodín para tu código.

# A. match_ends
# Dada una lista de cadenas, retornar la cantidad del número de cadenas
# donde la longitud de cadenas es 2 o más y el primer y último
# caracter de la cadena son el mismo.
# Nota: python no tiene un operador ++, pero += funciona.


def match_ends(words):
    # +++tu código aquí+++
    cantidad = 0
    for cadena in words:
        a = cadena[0:1]
        b = cadena[-1:]
        if (len(cadena) >= 2 and a == b):
            cantidad += 1
    return cantidad


# B. front_x
# Dada una lista de cadenas, retornar una lista con las cadenas
# ordenadas, pero agrupar todas las cadenas que comienzan con x primero.
# ej. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] devuelve
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Pista: Esto puede ser hecho con 2 listas y ordenándolas por separado
# antes de combinarlas.
def front_x(words):
    # +++tu código aquí+++
    list1 = []
    list2 = []
    for cadena in words:
        if cadena[0:1] == 'x':
            list1.append(cadena)
        else: 
            list2.append(cadena)
    listaOrdenada = sorted(list1) + sorted(list2)    
    return listaOrdenada

# C. sort_last
# Dada una lista de tuplas no-vacías, retornar una lista ordenada en orden
# incremental considerando el último elemento en cada tupla.
# ej. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] devuelve
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Pista: utilizar una función personalizada key= para extraer el último
# elemento de una tupla.
def sort_last(tuples):
    # +++tu código aquí+++
    t = sorted (tuples, key=lambda tuples: tuples[-1:])
    return t


# Función simple test() utilizada en main() para mostrar
# lo que retorna cada función vs lo que debería retornar.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s obtuvo: %s se esperaba: %s' % (prefix, repr(got), repr(expected))


# Función main() llama a las funciones de arriba con entradas interesantes,
# utilizando test() para verificar si cada resultado es correcto o no.
def main():
    print 'match_ends'
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print
    print 'front_x'
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    print
    print 'sort_last'
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
    main()
