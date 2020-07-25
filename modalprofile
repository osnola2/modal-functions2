def cp(prop1, prop2): #defining compatibility function

    if diam(conj(prop1, prop2)) == 1:
        return 1
    else:
        return 0
       
def modpro(prop1, prop2): #return modal profile
    return  [cp(prop1, prop2), cp(prop1, neg(prop2)), cp(neg(prop1), prop2), cp(neg(prop1), neg(prop2))] 
