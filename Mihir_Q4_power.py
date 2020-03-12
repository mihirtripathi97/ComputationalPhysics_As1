
import numpy as np

def eigenvalue(A, v):   #Calculates eigen value of given matrix and eigen vector, Here eigen vector is normalized
    Av = np.dot(A,v)
    return v.dot(Av)

def power_iteration(A):
    n, d = A.shape

    v = np.ones(d) / np.sqrt(d)      #Initial guess for eigen vector
    ev = eigenvalue(A, v)

    while True:
        Av = A.dot(v)
        v_n = Av / np.linalg.norm(Av)    #Calculates eigenvector (normalized)

        ev_n = eigenvalue(A, v_n)      #Finds corresponding eigen value
        if np.abs((ev - ev_n)/ev) < 0.01:     #If new eigenvalue is within 1% of old one then breaks the loop
            break

        v = v_n       #stores new eigenvector in old eigenvector 
        ev = ev_n     #stores new eigenvalue in old eigenvalue 

    return ev_n, v_n

A = np.array([[2,-1,0],[-1,2,-1],[0,-1,2]])
E,V = power_iteration(A)
print("The dominant eigen value is : ",E)
print("The dominant eigen vactor is : ",V)







