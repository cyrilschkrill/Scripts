import random as rd 
def odd2(n):
    odd = rd.randrange(n)
    while odd % 2 == 0:
        odd = rd.randrange(n)
    return(odd)
#
def odd(m):
    return(2*m+1)

def syracuse(u):

    strat = list()
    strat.append(u)
    
    print(strat[0])

    while u != 1:
        if u % 2 == 0:
            v = int(u / 2)
            strat.append(v)
        else:
            v = int((3 * u + 1)/2)
            strat.append(v)
        u = v
        print(v)
    return("#")


# for i in syracuse(17):
#     print(i)

syracuse(7)
