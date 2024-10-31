# Fem una nova funció anomenada peano(). Els seus paràmetres són els següents:
# ite = iteracions
# x,y = valors al pla
def peano(x,y,ite):
    # Amb el 1r condicional farem l'iniciador.
    if ite == 0:
        #Construim el nostre iniciador amb els punts x=(0,0) i y=(1,0). En aquest cas l'iniciador és una recta.
        plt.plot([x[0],y[0]],[x[1],y[1]],color ='blue')
    # El 2n condicional servirá per trobar els punts per obtenir el 1r generador.
    else:
        # Tracem els punts 'a' i 'b' mitjançant operacions.
        a = x + (y-x)/3
        b = x + 2*(y-x)/3
        # Per obtenir els següents punts utilitzarem rotacions.
        # Per obtenir 'c' girem una recta 'ab' 90º
        # Per obtenir 'd' girem una recta 'by' 90º
        # Per obtenir 'e' girem una recta 'ab' -90º
        # Per obtenir 'f' girem una recta 'by' -90º
        c = rotation(a,b,np.pi/2)
        d = rotation(b,y,np.pi/2)
        e = rotation(a,b,-np.pi/2)
        f = rotation(b,y,-np.pi/2)
        # El següent pas és traçar el 1r generador. Per fer-ho, utilitzarem la funció peano() i usarem de paràmetres els valors obtinguts anteriorment.
        peano(x,a,ite-1)
        peano(a,c,ite-1)
        peano(c,d,ite-1)
        peano(d,b,ite-1)
        peano(b,f,ite-1)
        peano(f,e,ite-1)
        peano(e,a,ite-1)
        peano(a,b,ite-1)
        peano(b,y,ite-1)
        
# Utilitzem els punts 'x' i 'y' com a punts inicials.
x = np.array([0,0]) 
y = np.array([1,0]) 

# Iterem els punts 'x' i 'y' 4 vegades. Obtenint la corba.
peano(x,y,4)
plt.axis('equal')
plt.axis('off')
