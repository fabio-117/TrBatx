def mandelbrot(c,ite):
    # Usem com a punt d'inici el nombre complex z=0+0i
    z=complex(0,0)
    # Amb el següent bucle es crea una successió de nombres complexos c(0), c(1), c(2), etc. Aquest procés s'executarà fins que es trobi la iteració c(k). Tal que
    # |c(k)|>2. 
    for k in range(ite):
        z=z*z+c
        if abs(z)>2:
            break
    return k
# Definim una altra funció, que servirà per dibuixar regions del conjunt de Mandelbrot, utilitzant un nombre complex 'z' concret.
# z = nombres complexos
# dx = rang de capacitat pels valors reals, per obtenir la regió a graficar.
# dy = rang de capacitat pels valors imaginaris, per obtenir la regió a graficar.
# n = nombre de punts en la regió en els eixos x i y.
def plot_mandelbrot3D(z,dx,dy,n):
    # Construïm la regió de [real(z)-dx,real(z)+dx]X[imag(z)-dy,imag(z)+dy]. 
    x=np.linspace(np.real(z)-dx,np.real(z)+dx,n)
    y=np.linspace(np.imag(z)-dy,np.imag(z)+dy,n)
    # Fem una matriu de zeros de dimensió nxn.
    a=np.zeros((n,n))
    # Amb dos bucles for, construïm una malla de nombres complexos 'c' amb els valors 'x' i 'y'. 
    for k in range(n):
        for j in range(n):
            c=complex(x[k],y[j])
            # Actualitzem la matriu, substituint cada zero pel valor de 'k' que retorna la funció mandelbrot(). 
            # c = tots el nombres complexos.
            a[k,j]=mandelbrot(c,40)
            # La matriu s'actualitzarà amb els valors de 'a' obtinguts en cada nova iteració. 
    mayavi.mlab.figure(bgcolor=(1, 1, 1))
    smoothed_atlas = scipy.ndimage.gaussian_filter(a.T, 2)
    mayavi.mlab.surf(smoothed_atlas, warp_scale=5.5,colormap = 'terrain')
    mayavi.mlab.show()
