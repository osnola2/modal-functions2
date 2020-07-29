def pi2(f):
    a = []
    for i in K[2]:
        for j in K[2]:
            if ([f(i[0], j[0]), f(i[1], j[1])]) not in K[2]:
                if a == []:
                    a.append(0)
                print([a])
            else:
                print([[]])
                #ainda não tá funcionando bem
