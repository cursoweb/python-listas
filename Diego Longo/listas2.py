#!/usr/bin/python -tt
# -*- coding: UTF-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Ejercicios de listas básicos adicionales

# D. Dada una lista de números, retornar una lista donde
# todos los elementos adjacentes iguales se reducen a un solo elemento,
# así [1, 2, 2, 3] retorna [1, 2, 3]. Pueden crear una nueva lista o
# modificar la lista enviada.
def remove_adjacent(nums):
    return


# E. Dadas 2 listas ordenadas en orden incremental, crear y retornar una lista
# fusionada de todos los elementos en orden. Puedes modificar las listas pasadas.
# Idealmente, la solución debería funcionar en tiempo "linear", haciendo una sola
# pasada de ambas listas.
def linear_merge(list1, list2):
    lista_fusion = list1 + list2
    lista_fusion.sort()
    return lista_fusion

# Nota: la solución de arriba es interesante, pero desafortunadamente.pop(0)
# no es constante en el tiempo con la implementación estándar de listas, así
# que lo de arriba no es un tiempo estrictamente lineal.
# Una aproximación alternativa utiliza pop(-1) para quitar los últimos elementos
# para cada lista, construyendo una lista solución que está invertida.
# Entonces utilizar reversed() para poner el resultado de vuelta en el orden correcto. 
# Esa solucion funciona en tiempo linear, pero es mas desprolijo.


# Función simple test() utilizada en main() para mostrar
# lo que retorna cada función vs lo que debería retornar.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '    X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Función main() llama a las funciones de arribacon entradas interesantes,
# utilizando test() para verificar si cada resultado es correcto o no.
def main():
    print 'remove_adjacent'
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])

    print
    print 'linear_merge'
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
             ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
             ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
             ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
    main()
