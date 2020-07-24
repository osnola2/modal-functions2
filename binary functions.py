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
