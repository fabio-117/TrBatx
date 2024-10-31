# Començem definint la funció koch() amb els seus parèmetres
# ite = iteracions
# x,y = punts en el pla. 
def koch(x,y,ite): 
    # Fem un condicional per la iteració 0, és a dir, l'iniciador.
    if ite == 0:
        # Amb el plt.plot és traça una linia recta de a=(0,0) a b=(1,0) en el pla. 
        plt.plot([x[0],y[0]],[x[1],y[1]],color ='red')
    # Posem un segon condicional que servirà per construir altres punts i les iteracions del fractal.    
    else:
        # Definim els punts u, v, w. Per fer-ho operem amb els punts x i y.
        u = x + (y-x)/3
        v = x + 2 * (y-x)/3
        w = rotation(u,v,np.pi/3)
        # Un cop obtenim els punts utilitzem la funció koch() per traçar el 1r generador
        koch(x,u,ite-1)
        koch(u,w,ite-1)
        koch(w,v,ite-1)
        koch(v,y,ite-1)
