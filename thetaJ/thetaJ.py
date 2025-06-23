### Encodage de la fonction Theta de Jacobi
from math import exp, pi
thetaJ(n,x):
    vect = [ exp(-pi*i*n**2) for i in range(-n,n)]
    return(sum(vect))

print thetaJ(3,5)
