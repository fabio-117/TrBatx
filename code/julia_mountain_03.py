# Nombre complex específic
c = complex(0,0.8)

# Dibuixem el paisatge amb l'opció 1.
mayavi.mlab.surf(a.T, warp_scale=2.5,colormap = 'YlGn')
plot_julia3D(x_min,x_max,y_min,y_max,c,n)

