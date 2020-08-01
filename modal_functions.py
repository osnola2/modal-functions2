from modalprofile import *


def modfun(f2, f3, f4, f5, f6, f7, f8, prop1, prop2):
    if modpro(prop1, prop2) in [[0,0,0,1], [1,1,1,0]]:
        return f2(prop1, prop2)
    if modpro(prop1, prop2) in [[0,0,1,0], [1,1,0,1]]:
        return f3(prop1, prop2)
    if modpro(prop1, prop2) in [[0,1,0,0], [1,0,1,1]]:
        return f4(prop1, prop2)
    if modpro(prop1, prop2) in [[1,0,0,0], [0,1,1,1]]:
        return f5(prop1, prop2)
    if modpro(prop1, prop2) in [[0,0,1,1], [1,1,0,0]]:
        return f6(prop1, prop2)
    if modpro(prop1, prop2) in [[0,1,0,1], [1,0,1,0]]:
        return f7(prop1, prop2)
    if modpro(prop1, prop2) in [[1,0,0,1], [0,1,1,0]]:
        return f8(prop1, prop2)
