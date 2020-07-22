for f in tau2:
    for i in M1:
        for j in i:
            for k in i:
                if (f(j, k)) not in i:
                    print(j, k, f(j, k),f, 'doesnt preserve', i) 
                    
for f in tau2:
    for i in M2:
        for j in i:
            for k in i:
                if ([f(j[0], k[0]), f(j[1], k[1])]) not in i:
                    print(j[0], k[0], j[1], k[1], [f(j[0], k[0]), f(j[1], k[1])], f, 'doesnt preserve', i)

for f in tau2:
    for i in M3:
        for j in i:
            for k in i:
                if([f(j[0], k[0]), f(j[1], k[1]), f(j[2], k[2])]) not in i:
                    print(j[0], k[0], j[1], k[1], j[2], k[2],[f(j[0], k[0]), f(j[1], k[1]), f(j[2], k[2])],f, 'doesnt preserve', i)
        
for f in tau2:
    for i in M4:
        for j in i:
            for k in i:
                if ([f(j[0], k[0]), f(j[1], k[1]), f(j[2], k[2]), f(j[3],k[3])]) not in i:
                    print(j[0], k[0], j[1], k[1], j[2], k[2], j[3], k[3], [f(j[0], k[0]), f(j[1], k[1]), f(j[2], k[2]),f(j[3], k[3])], f, 'doesnt preserve', i)        
