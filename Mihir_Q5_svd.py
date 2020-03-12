
#In this code it is assumed that matrix A is of dimensions m,n such that m>n

import numpy as np
from numpy import linalg as la
import time
def svd(A,m,n):
    
    AT=np.transpose(A)
    
    M=np.matmul(AT,A)
    eval,evec=la.eigh(M)
    
    M1=np.matmul(A,AT)
    eval1,evec1=la.eigh(M1)
    
    a=np.arange(0,n)
    b=np.flip(a)
    
    evec[:,a]=evec[:,b]
    
    VT=np.transpose(evec)
    
    U=np.dot(A,evec)
    U=U/np.sqrt(np.flip(eval))
    
    temp_a=np.arange(m-n+1,m)
    temp_col=evec1[:,temp_a]
    
    U=np.column_stack((U,temp_col))
    S=np.zeros(m*n).reshape(m,n)
    
    for i in range (0,m):
        for j in range (0,n):
            if (j<n):
                S[j][j]=np.sqrt(eval[n-j-1])
    return (U,S,VT)


A = np.array([[0,1,1],[0,1,0],[1,1,0],[0,1,0],[1,0,1]])
t0=time.time()
U,S,VT=svd(A,5,3)

t1=time.time()

print ('\nSingular values without using inbuilt function are:', S[0][0],S[1][1],S[2][2])
print ('\nTime taken for evaluation without using inbuilt SVD function',(t1-t0),'sec')

t2=time.time()
U1,S1,V1=la.svd(A)
t3=time.time()
print ('\nSingular values with inbuilt SVD function',S1)
print ('\nTime taken for evaluation with inbuilt SVD function',(t3-t2),'sec')






