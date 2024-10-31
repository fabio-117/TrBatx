matriu_iteracions=np.zeros((n,m))
for l in range(n):
    for j in range(m):
        c=complex(x_values[l],y_values[j])
        matriu_iteracions[l,j]=obtenir_iteracio(c,20)  
        
data_iterations=pd.DataFrame(matriu_iteracions)
data_iterations        
        
