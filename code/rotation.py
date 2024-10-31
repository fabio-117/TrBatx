# Primer definim la funció rotation i afegim els paràmetres següents (punt inicial, punt final, angle)
def rotation(start, end, angle): 
    # Construim la matriu
    M = np.array([[np.cos(angle),-np.sin(angle)],[np.sin(angle), np.cos(angle)]])
    # Construim un vector D, i l'igualem al punt inicial més + la matriu
    D = start + M@(end-start)
    # Quan s'executa la línia anterior guarda el vector rotat D
    return D
