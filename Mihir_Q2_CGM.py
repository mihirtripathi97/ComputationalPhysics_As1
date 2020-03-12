import numpy as np


A = np.array([[0.2, 0.1, 1, 1, 0], [0.1, 4, -1, 1, -1], [1, -1, 60, 0, -2], [1, 1, 0, 8, 4], [0, -1, -2, 4, 700]])     #A matrix of Ax=b
b=np.array([1,2,3,4,5])   # b

#initial approximation
x=np.array([1,0,0,2,0])   

r = b - np.dot(A, x)
p = r
r_n_o = np.dot(np.transpose(r), r)   #norm of old residual
r_n_n = np.dot(np.transpose(r), r)   #norm of new residual
i=0

while(r_n_o>0.01):
    Ap = np.dot(A, p)
    alpha = r_n_o / np.dot(np.transpose(p), Ap)
    x = x + np.dot(alpha, p)
    r = r - np.dot(alpha, Ap)
    r_n_n = np.dot(np.transpose(r), r)
    p = r + (r_n_n/r_n_o)*p
    r_n_o = r_n_n
    i=i+1


print("Solution for given problem",x)
print("Number of iterations: ",i)