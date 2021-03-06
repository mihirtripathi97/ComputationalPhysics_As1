
#Jacobi method to solve system of linear equations

import numpy as np
import numpy.linalg as npl

def check(b,B):
    c = b-B
    d = np.sqrt(np.dot(c,c))
    return(d)

A = np.array([[0.2, 0.1, 1, 1, 0], [0.1, 4, -1, 1, -1], [1, -1, 60, 0, -2], [1, 1, 0, 8, 4], [0, -1, -2, 4, 700]])     #A matrix of Ax=b
b=np.array([1,2,3,4,5])   # b
B=np.array([0,0,0,0,0]) 

D = np.zeros((5,5))   #Creating a  matrix which will act as a diagonal matrix
R = np.zeros((5,5))   #R matrix which wil have zero values on diagonal

for j in range(0,5):
    for i in range (0,5):
        if i != j:
            R[i][j] = A[i][j]#Assigning values in R
        else:
            D[i][i] = A[i][i]


x = np.array([7,1,0,-4,0])  #initial guess 
k = (check(b,B))               #Tolarance check


ID = npl.inv(D)         #Inverting D

i=0

while k>0.01:                   #For Jacobi method, X(k+1) = inv(D)(b-RX(k)) , this loop calculates X iteratively till dot(B,b)<0.01 where B= AX(k)
    i= i+1
    WD = b-np.dot(R,x)  
    x = np.dot(ID,WD)
    #print('WD:',WD)
    #print('x:',x)
    B = np.matmul(A,x)
    #print(B)
    k = check(b,B)
    #print('k: ',k)   

print(x)
print('Number of iterations: ',i)










9
