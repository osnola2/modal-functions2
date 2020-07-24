def conj(prop1, prop2): 
    if prop1 == prop2:
        return prop1
    if prop1 == 0 or prop2 == 0:
        return 0
    if prop1 == 1:
        return prop2
    if prop2 == 1:
        return prop1
    if prop1 == 5 and prop2 == 4:
        return 6
    if prop2 == 5 and prop1 == 4:
        return 6
    if prop1 == 5 and prop2 == 9:
        return 2
    if prop2 == 5 and prop1 == 9:
        return 2
    if prop1 == 5 and prop2 == 3:
        return 0
    if prop2 == 5 and prop1 == 3:
        return 0
    if prop1 == 5 and prop2 in [6,2]:
        return prop2
    if prop2 == 5 and prop1 in [6,2]:
        return prop1
    if prop1 == 4 and prop2 == 9:
        return 3
    if prop2 == 4 and prop1 == 9:
        return 3
    if prop1 == 4 and prop2 == 2:
        return 0
    if prop2 == 4 and prop1 == 2:
        return 0
    if prop1 == 4 and prop2 in [6,3]:
        return prop2
    if prop2 == 4 and prop1 in [6,3]:
        return prop1
    if prop1 == 9 and prop2 == 6:
        return 0
    if prop2 == 9 and prop1 == 6:
        return 0
    if prop1 == 9 and prop2 in [2,3]:
        return prop2
    if prop2 == 9 and prop1 in [2,3]:
        return prop1
    if prop1 == 6 and prop2 in [2,3]:
        return 0
    if prop2 == 6 and prop1 in [2,3]:
        return 0
    if prop1 == 2 and prop2 == 3:
        return 0
    if prop2 == 2 and prop1 == 3:
        return 0

def box(prop1):
    if prop1 == 1:
        return 1
    else:
        return 0
    
def neg(prop1):
    if prop1 == 1:
        return 0
    if prop1 == 5:
        return 3
    if prop1 == 4:
        return 2
    if prop1 == 9:
        return 6
    if prop1 == 2:
        return 4
    if prop1 == 6:
        return 9
    if prop1 == 3:
        return 5
    if prop1 == 0:
        return 1

def diam(prop1):
    return(neg(box(neg(prop1))))