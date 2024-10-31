# Comencem fent una funció per trobar els punts per fer la corba. Aquesta funció l'anomenem points_hilbert().
def points_hilbert(ite):
    # Establim el 1r condicional per a la  iteració 0 amb els valors de x i y.
    if ite == 0:
        x = 0 
        y = 0    
    # El 2n condicional servirà per totes les iteracions majors que 1.
    else:
        x0,y0 = points_hilbert(ite-1)
        # Establim una malla d'1X1 que va des de -0.5 fins a 0.5. En ella trobarem tots els valors de x i y necessaris per construir la corba.
        x = 0.5*np.array([-0.5+y0,-0.5+x0,0.5+x0,0.5-y0])
        y = 0.5*np.array([-0.5+x0,0.5+y0,0.5+y0,-0.5-x0])
    # Dins del return guardem tots els valors de x i y que s'obtenen.    
    return x, y
    
# Fem una nova funció, anomenada plot_hilbert() i li afegim com a únic paràmetre n.
def plot_hilbert(n):
    # Utilitzem la funció points_hilbert() i li posem de paràmetre n.
    # n = nombre d'iteracions.    
    x,y = points_hilbert(n)
    # Canviem la funció points_hilbert() perquè pugui imprimir els valors com un espai 1-dimensional.
    X = np.reshape(x,4**n)
    Y = np.reshape(y,4**n)
    plt.plot(X,Y,color = 'purple')
    plt.axis('off')
    plt.axis('equal')
    
plot_hilbert(5)
