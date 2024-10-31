# Per a construir el tetraedre reutilitzarem la funció triangle() i afegirem algunes ordres més.
# Agafarem els punts 'b' i 'c' com a punts inicials.
b = np.array([0,0])
c = np.array([-0.5,2.5])
# Per trobar 'a' construirem una recta 'cb' i la rotarem amb la funció rotation -50º.
# Per a 'd' rotarem la recta 'cd' 30º. 
a = rotation(c,b,-5*np.pi/18)
d = rotation(c,b,np.pi/6)
# Reutilitzem la funció triangle() amb els nous punts i li afegirem 4 iteracions.
triangle(a,b,c,4)
triangle(b,d,c,4)
plt.axis('equal')
plt.axis('off')
