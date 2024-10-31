# Definim la funció triangle() amb els paràmetres següents:
# ite = iteracions
# x,y,z = punts en el pla
def triangle(x,y,z,ite):
    # Fem un condicional per a l'iniciador.
    if ite == 0:
        # Tracem un triangle amb els punts a, b, c
        plt.fill([x[0],y[0],z[0],x[0]],[x[1],y[1],z[1],x[1]], color = 'cyan')
    # Segon condicional per trobar altres punts.    
    else:
        # Definim els punts u, v, w. Per fer-ho, operem amb els punts x i y.
        u = x + (z-x)/2
        v = z + (y-z)/2
        w = x + (y-x)/2
        # Tracem el 1r generador amb la funció triangle().
        triangle(x,w,u,ite-1)
        triangle(w,y,v,ite-1)
        triangle(u,v,z,ite-1)

# Agafem els punts a, b, c com a valors inicials al pla.
a = np.array([0,0])
b = np.array([1,0])
c = rotation(a,b,np.pi/3)

# Passem els punts com a valors de la funció triangle() i li assignem 4 iteracions. 
triangle(a,b,c,4,)
plt.axis('equal')
plt.axis('off')
