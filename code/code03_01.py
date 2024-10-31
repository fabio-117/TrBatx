# c és nombre complex arbitrari
# max_iter és el nombre màxim d'iteracions
def successio_c(c,max_iter):
    z=0
    dict_successio={'c[k]':[],'successió_c[k]':[],'mòdul_c[k]':[]}
    for i in range(0,max_iter):
        z=z**2+c
        dict_successio['c[k]'].append(f'c{[k]}')
        dict_successio['successió_c[k]'].append(z)
        dict_successio['mòdul_c[k]'].append(abs(z))
    df=pd.DataFrame(dict_successio)
    return df
