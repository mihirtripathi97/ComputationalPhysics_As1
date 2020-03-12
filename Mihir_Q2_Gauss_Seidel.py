
#Gauss Seidel to solve system of linear equations
import numpy as np
import numpy.linalg as npl

def check(b,B):
    c = b-B
    d = np.sqrt(np.dot(c,c))
    return(d)

A = np.array([[0.2, 0.1, 1, 1, 0], [0.1, 4, -1, 1, -1], [1, -1, 60, 0, -2], [1, 1, 0, 8, 4], [0, -1, -2, 4, 700]])     #A matrix of Ax=b
b=np.array([1,2,3,4,5])   # b
B=np.array([0,0,0,0,0])     #B for initial tollrence

L = np.zeros((5,5))   
U = np.zeros((5,5))

for i in range (0,5):
    for j in range(0,5):

        if(j<=i):
            L[i][j]=A[i][j]         #creating Lower triangular matrix 
        elif(j>i):
            U[i][j]=A[i][j]         #creating Upper triangular matrix
#print(U)
#print(L)
x = np.array([7,1,0,-4,0]) 
IL = npl.inv(L)         #Inverting L
k = check(b,B)

i=0
while k>0.01:                   #For Gauss Seidel method, X(k+1) = inv(L)(b-UX(k)) , this loop calculates X iteratively till dot(B,b)<0.01 where B= AX(k)
    i= i+1
    WD = b-np.dot(U,x)  
    x = np.dot(IL,WD)
    #print('WD:',WD)
    #print('x:',x)
    B = np.matmul(A,x)
    #print(B)
    k = check(b,B)
    #print('k: ',k)   

print(x)
print('Number of iterations: ',i)


        
    
