# Per construir l'esponja de Menger utilitzarem la funció carpet().
# Utilitzarem els punts a, b, c i d com a punts inicials. Aquests punts s'utilitzaran per generar els extrems del cub.
a = np.array([0,0])
b = np.array([1,0])
c = rotation(b,a,-np.pi/2)
d = rotation(a,b,np.pi/2)
# Per trobar 'e' es construeix una recta 'bc' i rotem -45º.
# En el cas de 'f' es construeix una recta 'cd' i es gira 135º.
# Per 'g' es gira una recta 'dc' 45º. 
e = rotation(b,c,-np.pi/4)
f = rotation(c,b,3*np.pi/4)
g = rotation(d,c,np.pi/4)
# Mitjançant operacions, obtenim tres punts més, els quals ens serviran per tancar el cub.
m = b + 3*(e-b)/4
n = c + 3*(f-c)/4
o = d + 3*(g-d)/4
# Amb la funció carpet() dibuixarem les cares del cub utilitzant els punts obtinguts com a paràmetres i els iterem 4 vegades.
carpet(a,b,c,d,3)
carpet(b,m,n,c,3)
carpet(d,c,n,o,3)
plt.axis('equal')
plt.axis('off')
