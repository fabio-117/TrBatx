# Definim la nostra funció com a drac(), i li agreguem els paràmetres següents:
# ite = iteracions
# x,y,z = valors al pla
def drac(x,y,z,ite):
    # El 1r condiconal servirà per generar l'iniciador. 
    if ite == 0:
        # Utilitzem els punts x, y i z.
        plt.plot([x[0],y[0],z[0]],[x[1],y[1],z[1]])
    # En el 2n condicional generem dos punts: 'u' i 'v'.
    else:
        u = x + (z-x)/2
        v = rotation(x,u,np.pi/2)
        # Posem els paràmetres a la funció drac() i tracem el 1r generador.
        drac(x,v,y,ite-1)
        drac(z,u,y,ite-1)
        
# Agafem els punts 'a', 'b' i 'c' com a punts inicials.
a = np.array([0,0])
b = np.array([.5,.5])
c = np.array([1,0])

# Agafem els punts anteriors com a paràmetres en drac(). Iterem els punts 10 vegades.
drac(a,b,c,10)
plt.axis('equal')
plt.axis('off');
