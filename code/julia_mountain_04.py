# Nombre complex específic
c = complex(0.4,0.4)

# Dibuixem el paisatge amb l'opció 2.
smoothed_atlas = scipy.ndimage.gaussian_filter(a.T, 2)
mayavi.mlab.surf(smoothed_atlas, warp_scale=2.5,colormap = 'terrain')
plot_julia3D(x_min,x_max,y_min,y_max,c,n)

