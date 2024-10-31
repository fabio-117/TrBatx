# Ara, per construir el fractal agafem els punts A i B com a punt de partida.
A = np.array([0,0])
B = np.array([1,0])
# Passem els punts A i B com a paràmetres de la funció koch i li assignem 4 iteracions.
koch(A,B,4)
plt.axis('equal')
plt.axis('off')
