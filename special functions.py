def S(prop1, prop2):
    return disj(box(disj(prop1, prop2)), disj(box(imp(prop1,prop2)), box(cimp(prop1, prop2))))
    
def phi(prop1, prop2):
    return conj(conj(S(prop1, prop2),S(prop1, neg(prop2))), conj(S(neg(prop1), prop2),S(neg(prop1), neg(prop2))))

def pi211(prop1, prop2):
    return imp(phi(prop1, prop2), conj(imp(prop1, prop2), neg(box(prop2))))

def pi212(prop1, prop2):
    return disj(prop1, disj(prop2, S(prop1, prop2)))

def pi213(prop1, prop2):
    return disj(conj(prop1, prop2), S(neg(prop1), neg(prop2)))
    
def pi21(prop1, prop2):
    return conj(pi211(prop1, prop2), conj(pi212(prop1, prop2), pi213(prop1, prop2)))
