# c és nombre complex arbitrari
# max_iter és el nombre màxim d'iteracions
def obtenir_iteracio(c,maxiter):
    z=complex(0,0)
    for k in range(maxiter):
        z=z*z+c
        if abs(z)>2:
            break
            pass
        pass
    return k
