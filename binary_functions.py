from basic_functions import *


def falsum(prop1, prop2):
    return 0
    
def verum(prop1, prop2):
    return 1

def disj(prop1, prop2):
    return neg(conj(neg(prop1), neg(prop2)))

def imp(prop1, prop2):
    return disj(neg(prop1), prop2)

def cimp(prop1, prop2):
    return imp(prop2, prop1)

def eq(prop1, prop2):
    return conj(imp(prop1, prop2), cimp(prop1, prop2))

def xor(prop1, prop2):
    return eq(neg(prop1), prop2)

def nimp(prop1, prop2):
    return neg(imp(prop1, prop2))

def ncimp(prop1, prop2):
    return neg(cimp(prop1, prop2))

def pr1(prop1, prop2):
    return prop1

def pr2(prop1, prop2):
    return prop2

def neg1(prop1, prop2):
    return neg(prop1)

def neg2(prop1, prop2):
    return neg(prop2)

def shef(prop1, prop2):
    return neg(conj(prop1, prop2))

def peir(prop1, prop2):
    return neg(disj(prop1, prop2))


tau2 = [falsum, verum, conj, disj, imp, cimp, eq, xor, nimp, ncimp, pr1, pr2, neg1, neg2, shef, peir]

K = [[0], [1], [[0, 1], [1, 0]], [[0, 0], [0, 1], [1, 1]],
         [[0, 0, 0, 0], [0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 1, 0, 0], [1, 1, 1, 1]],
         [6], [0, 9, 1], [6, 9], [[0, 0], [0, 6], [0, 9], [1, 1]], [[0, 0], [1, 6], [1, 9], [1, 1]],
         [[0, 0], [0, 6], [1, 9], [1, 1]], [[0, 0], [0, 6], [0, 9], [1, 6], [1, 9], [1, 1]],
         [[0, 0], [0, 6], [0, 9], [0, 1], [1, 0], [1, 1]], [[0, 0], [0, 1], [1, 0], [1, 6], [1, 9], [1, 1]],
         [[0, 0], [0, 1], [6, 6], [9, 9], [1, 0], [1, 1]],
         [[0, 0], [0, 1], [6, 6], [6, 9], [9, 6], [9, 6], [9, 9], [1, 0], [1, 1]],
         [[0, 0], [6, 6], [6, 9], [9, 6], [9, 9], [1, 1]],
         [[0, 0], [0, 6], [0, 9], [0, 1], [6, 0], [6, 1], [9, 0], [9, 1], [1, 0], [1, 6], [1, 9], [1, 1]],
         [[0, 0, 0], [0, 0, 1], [0, 6, 0], [0, 9, 0], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 6, 1], [1, 9, 1], [1, 1, 0], [1, 1, 1]],
         [[0, 0, 0], [0, 6, 0], [0, 6, 1], [0, 9, 0], [0, 9, 1], [0, 1, 0], [1, 0, 1], [1, 6, 0], [1, 6, 1], [1, 9, 0], [1, 9, 1], [1, 1, 1]],
         [0, 6, 2, 4, 9, 1], [[0, 0], [6, 9], [2, 9], [3, 9], [5, 6], [4, 6], [9, 6], [1, 1]],
         [[0, 0], [6, 6], [2, 4], [3, 5], [5, 3], [4, 2], [9, 9], [1, 1]],
         [[0, 0], [6, 9], [2, 5], [3, 4], [5, 2], [4, 3], [9, 6], [1, 1]]]
