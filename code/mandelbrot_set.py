# Creem una nova funció, la qual anomenarem plot_mandelbrot(). Aquesta funció tindrà els paràmetres següents:
# n = nombre de punts en un rang de -2 a 2.
# ite = nombre d'iteracions.
def plot_mandelbrot(n,ite):
    # Construïm dos eixos de -2 a 2 en 'x' i 'y'. També farem una matriu de zeros de dimensió nxn.
    x = np.linspace(-2,2,n)
    y = np.linspace(-2,2,n)
    A = np.zeros((n,n))
    # Amb dos bucles for, construïm una malla de nombres complexos 'c' amb els valors 'x' i 'y'. 
    for p in range(n):
        for q in range(n):
            c = complex(x[p],y[q])
            # Actualitzem la matriu, substituint cada zero pel valor de 'k' que retorna la funció max_iteration(). En aquest cas, z = 0. Al definir'z' com a 0 estem actualitzant el valor de c.
            # c = tots el nombres complexos.
            A[p,q] = max_iteration(0,c,ite)
     # La matriu s'actualitzara amb els valors de 'A' obtinguts en cada nova iteració.        
    return A

# Ara imprimim els resultats amb 300 i 30 iteracions, per a la matriu A.
A = plot_mandelbrot(300,30)
# Amb la libreria matplotlib dibuixem la matriu A. 
plt.figure(figsize=(10, 10))
plt.imshow(A.T, interpolation="nearest");