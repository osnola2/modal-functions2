import tau1

def mod(fun1, fun2, prop1):
        if fun1 in tau1:    
            if fun2 in tau1:
                if prop1 in [2,3,4,5,6,9]:
                    return fun1(prop1)
                if prop1 in [0,1]:
                    return fun2(prop1)
