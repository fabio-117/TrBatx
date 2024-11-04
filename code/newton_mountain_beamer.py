def newton_fractal(f,df,z0,ite):
    # tol = La tolerància: un petit valor que serveix com a valor límit, és a dir, només agafem els valors que siguin majors a la tolerància.
    tol = 1e-8
    z=z0
    for k in range(ite):
        dz = f(z)/df(z)
        if abs(dz)<tol:
            return k
        z = z - 1.25*dz       

f=lambda z : z**(4 + 3j) - 1
df=lambda z : (4 + 3j)*z**(3 + 3j)
x_min = 0.4
x_max = 0.9
y_min = -0.9
y_max = -0.3

n_space = 300
x_values=np.linspace(x_min,x_max,n_space)
y_values=np.linspace(y_min,y_max,n_space)
n=len(x_values)
m=len(y_values)
a=np.zeros((n,m))
for k in range(n):
    for j in range(m):
        z=complex(x_values[k],y_values[j])
        # Actualitzem la matriu, substituint cada zero pel valor del mòdul de 'z' que retorna la funció newton_fractal(). 
        # z = tots el nombres complexos.
        a[k,j]=newton_fractal(f,df,z,200)
        # La matriu s'actualitzarà amb els valors de 'a' obtinguts en cada nova iteració. 
        pass
    pass
mayavi.mlab.figure(bgcolor=(1, 1, 1))   
smoothed_atlas = scipy.ndimage.gaussian_filter(a.T, 1.5)
mayavi.mlab.surf(smoothed_atlas, warp_scale=2.5,colormap = 'GnBu')
mayavi.mlab.show()


