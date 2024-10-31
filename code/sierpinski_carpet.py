# Es defineix la funció com a carpet() i li posem els paràmetres següents:
# ite = iteracions.
# x,y,z,q = valors del pla.
def carpet(x,y,z,q,ite):
    # 1r Condicional per obtenir l'iniciador, en aquest cas, un quadrat.
    if ite == 0:
        # Amb el plt.fill es traça el quadrat seguint els punts x,y,z,q.
        plt.fill([x[0],y[0],z[0],q[0],x[0]],[x[1],y[1],z[1],q[1],x[1]],color ='red')
    # Amb el 2n Condicional s'obtenen més punts mitjançant operacions.   
    else:
        a = x + (y-x)/3
        b = x + 2*(y-x)/3
        c = y + (z-y)/3
        d = y + 2*(z-y)/3
        e = z + (q-z)/3
        f = z + 2*(q-z)/3
        g = q + (x-q)/3
        h = q + 2*(x-q)/3
        r = x + (z-x)/3
        s = y + (q-y)/3
        t = x + 2*(z-x)/3
        u = y + 2*(q-y)/3
        # Traçem el primer generador amb la funció carpet().
        carpet(x,a,r,h,ite-1)
        carpet(a,b,s,r,ite-1)
        carpet(b,y,c,s,ite-1)
        carpet(h,r,u,g,ite-1)
        carpet(s,c,d,t,ite-1)
        carpet(g,u,f,q,ite-1)
        carpet(u,t,e,f,ite-1)
        carpet(t,d,z,e,ite-1)
        
# Utilitzarem els punts següents com punts inicials.
a = np.array([0,0])
b = np.array([1,0])
c = np.array([1,1])
d = np.array([0,1])

# Per últim, agafem els punts anteriors com a paràmetres de carpet() i els iterem 4 vegades.
carpet(a,b,c,d,4)
plt.axis('equal')
plt.axis('off')
