# Com a punt de partida, definim una funció com a julia(). Aquesta funció tindrà els paràmetres següents:
# c = nombre complex especific
# z = nombres complexos
# ite = nombre d'iteracions
def julia(c,z,ite):
    for k in range(ite):
        z=z*z+c
        if abs(z)>4:
            break
            pass
        pass
    return k
    
# Valors de la malla.
x_min = -1.5
x_max = 1.5
y_min = -1.5
y_max = 1.5

# A continuació definim una altra funció, la qual, anomenarem plot_julia3D(). Aquesta funció ens servirà per crear el paisatge 3D.
def plot_julia3D():
    # Construïm dos eixos de [x_min, x_max]X[y_min, y_max]. També farem una matriu de zeros de dimensió nxn.
    x=np.linspace(x_min,x_max,n)
    y=np.linspace(y_min,y_max,n)
    a=np.zeros((n,n))
    # Amb dos bucles for, construïm una malla de nombres complexos 'z' amb els valors 'x' i 'y'. 
    for i in range(n):
        for j in range(n):
            z=complex(x[i],y[j])
            a[i,j]=julia(c,z,40)
            #print(a,c)
            pass
        pass
    
    # Amb la primera línia farem que mayavi ens doni els resultats en un fons blanc
    mayavi.mlab.figure(bgcolor=(1, 1, 1))
    # A partir d'aquí tenim dos escenaris diferents:
    
    #1: Si volem un model predeterminat utilitzem la següent línia.
    mayavi.mlab.surf(a.T, warp_scale=2.5,colormap = 'YlGn')
    #2: Si la volem amb més detall, utilitzem les dues línies següents i desactivem l'anterior.
    smoothed_atlas = scipy.ndimage.gaussian_filter(a.T, 2)
    mayavi.mlab.surf(smoothed_atlas, warp_scale=2.5,colormap = 'terrain')
    # Mostrar la imatge
    mayavi.mlab.show()



