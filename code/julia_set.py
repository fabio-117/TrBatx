# Fem una nova funció, la qual, anomenarem max_iteration(). Els paràmetres d'aquesta funció seran:
# z = nombres complexos.
# c = nombre d'un complex concret.
# ite = iteracions
def max_iteration(z,c,ite):
    # Utilitzem un bucle for, amb el qual, obtindrem la iteració 'k', on el valor del mòdul és |z| > 2.
    for k in range(ite):
        z = z**2+c
        if(abs(z)>2):
            break
    # Amb el return k, guardem l'última iteració on z és major de 2.        
    return k       
    
# Definim una nova funció com a plot_julia(). Els paràmetres de la funció són:
# n = nombre de punts en un rang de -2 a 2 per a 'x' i 'y'.
# c = nombre complex fix de la funció f(z) = z*z+c
# ite = nombre de iteracions
def plot_julia(n,c,ite):
    # Construïm dos eixos de -2 a 2 en 'x' i 'y'. 
    x = np.linspace(-2,2,n)
    y = np.linspace(-2,2,n)
    # Construïm una matriu de zeros de dimensió nxn.
    A = np.zeros((n,n))
    # Amb dos bucles for, construïm una malla de nombres complexos 'z' amb els valors 'x' i 'y'. 
    for p in range(n):
        for q in range(n):
            z = complex(x[p],y[q])
            # Actualitzem la matriu, substituint cada zero pel valor de 'k' que retorna la funció max_iteration().
            A[p,q] = max_iteration(z,c,ite)
    # Matriu actualitzada amb els valors de 'k' de cada complex 'z'. 
    return A
    
# Dibuixem el conjunt amb les següents caracteristiques:
# n = 500 punts
# c = -0.5-1j*0.5
# ite = 30
A = plot_julia(500,-0.5-1j*0.5,30)

# Amb la libreria matplotlib dibuixem la matriu A. 
plt.figure(figsize=(10, 10))
plt.imshow(A.T, interpolation="nearest");
