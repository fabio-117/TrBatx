# Comencem construint una funció, la qual, anomenarem cantor_set(). Els paràmetres d'aquesta funció seran els següents:
# a0 = coordenada x del punt 'a'
# a1 = coordenada y del punt 'a'
# b0 = coordenada x del punt 'b'
# b1 = coordenada y del punt 'b'
# ite = nombre d'iteracions
def cantor_set(a0,b0,a1,b1,ite):
    # Primer condicional.
    if ite==0:
        # Usem les coordenades 'x' i 'y' de 'a' i 'b' per construir l'iniciador.
        plt.plot([a0,b0],[a1,b1],color='black')
    # Segon condicional.
    else:
        # Mitjançant operacions, trobem les coordenades 'c0' i 'd0' en l'eix 'x'.
        c0=a0+(b0-a0)/3.0
        d0=a0+2*(b0-a0)/3.0
        # Cridem a la funció cantor_set() i afegint els nous paràmetres construïm el 1r generador.
        cantor_set(a0,c0,a1-0.05,a1-0.05,ite-1)
        cantor_set(d0,b0,b1-0.05,b1-0.05,ite-1)
        
# Dibuixem el conjunt de Cantor amb 5 iteracions.
for k in range(0,5):
    cantor_set(0,1,0,0,k)
    plt.axis('off')
