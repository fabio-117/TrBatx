# Fem una nova funció, anomenada plot_hilbert() i li afegim com a únic paràmetre n.
def plot_hilbert(n):
    # Utilitzem la funció points_hilbert() i li posem de paràmetre n.
    # n = nombre d'iteracions.    
    x,y = points_hilbert(n)
    # Canviem la funció points_hilbert() perquè pugui imprimir els valors com un espai 1-dimensional.
    X = np.reshape(a,4**n)
    Y = np.reshape(b,4**n)
    plt.plot(X,Y,color = 'purple')
    plt.axis('off')
    plt.axis('equal')
