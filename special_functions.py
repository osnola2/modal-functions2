from basic_functions import *
from binary_functions import *


def S(prop1, prop2):
    return disj(box(disj(prop1, prop2)), disj(box(imp(prop1,prop2)), box(cimp(prop1, prop2))))

def phi(prop1, prop2):
    return conj(conj(S(prop1, prop2),S(prop1, neg(prop2))), conj(S(neg(prop1), prop2),S(neg(prop1), neg(prop2))))

def endem21a(prop1, prop2):
    return imp(phi(prop1, prop2), conj(imp(prop1, prop2), neg(box(prop2))))

def endem21b(prop1, prop2):
    return conj(eq(prop1, S(prop1, prop2)), imp(prop2, S(prop1, prop2)))
def endem21(prop1, prop2):
    return conj(endem21a(prop1, prop2), disj(phi(prop1, prop2), endem21b(prop1, prop2)))


for i in K[21]:
    for j in K[21]:
        if [endem21(i[0], j[0]), endem21(i[1], j[1])] not in K[21]:
            print(i[0], j[0], i[1], j[1], endem21(i[0], j[0]), endem21(i[1], j[1]))
