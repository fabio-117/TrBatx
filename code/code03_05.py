x_values=np.linspace(-2,2,9)
y_values=np.linspace(-2,2,9)
n=len(x_values)
m=len(y_values)
a=[]
for l in range(n):
    row=[]
    for j in range(m):
        c=complex(x_values[l].round(2),y_values[j].round(2))
        row.append(f'{c.real}+{c.imag}i')
    a.append(row)

data_complex=pd.DataFrame(a)
data_complex    
