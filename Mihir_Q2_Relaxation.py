

import numpy as np
from numpy import linalg as LA


def check(b,B):
    c = b-B
    d = np.sqrt(np.dot(c,c))
    return(d)



A = np.array([[0.2, 0.1, 1, 1, 0], [0.1, 4, -1, 1, -1], [1, -1, 60, 0, -2], [1, 1, 0, 8, 4], [0, -1, -2, 4, 700]])     #A matrix of Ax=b
b=np.array([1,2,3,4,5])   # b
B=np.array([0,0,0,0,0])     #B for initial tollrence
x= np.array([1,0,1,1,1])
w=1.25
D = np.zeros((5,5))
L = np.zeros((5,5))   
U = np.zeros((5,5))

for i in range (0,5):
    for j in range(0,5):

        if(j<=i):
            L[i][j]=A[i][j]         #creating Lower triangular matrix 
        elif(j>i):
            U[i][j]=A[i][j]
        elif(j==i):
            D[i][i] = A[i][i]

    


while check(b,B)>0.01:                  #derivation for this algorythm - wikipedia 
    
    LU_i = LA.inv(D+w*L)
    As = w*U + (w-1)*D
    b_n = w*b
    Asx = np.dot(As,x)
    
    Af = b_n - Asx
    
    x = np.dot(LU_i,Af)
    
    B = np.dot(A,x)

print(x)
#print(B)





