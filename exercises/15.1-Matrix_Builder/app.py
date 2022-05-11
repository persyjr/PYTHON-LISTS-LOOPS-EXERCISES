#Import random
import math
#Create the function below:
def matrixBuilder(n):
    filas=[]
    columnas=[]
    for i in range(0,n):
        filas.append(1)
    for i in range(0,n):
        columnas.append(filas)
    
    return columnas

resultado=matrixBuilder(5)
print(resultado)