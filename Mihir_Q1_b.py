import numpy as np


L = [[1,0.67,0.33],[0.45,1,0.55],[0.67,0.33,1]]
b = [2,2,2]

x =  np.linalg.solve(L,b)

print('x[0] = "\'%.9f'%x[0])
print('x[1] = "\'%.9f'%x[1])

print('x[2] = "\'%.9f'%x[2])

