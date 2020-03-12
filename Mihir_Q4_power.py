{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The dominant eigen value is :  3.414141414141414\n",
      "The dominant eigen vactor is :  [ 0.50251891 -0.70352647  0.50251891]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "def eigenvalue(A, v):   #Calculates eigen value of given matrix and eigen vector, Here eigen vector is normalized\n",
    "    Av = np.dot(A,v)\n",
    "    return v.dot(Av)\n",
    "\n",
    "def power_iteration(A):\n",
    "    n, d = A.shape\n",
    "\n",
    "    v = np.ones(d) / np.sqrt(d)      #Initial guess for eigen vector\n",
    "    ev = eigenvalue(A, v)\n",
    "\n",
    "    while True:\n",
    "        Av = A.dot(v)\n",
    "        v_n = Av / np.linalg.norm(Av)    #Calculates eigenvector (normalized)\n",
    "\n",
    "        ev_n = eigenvalue(A, v_n)      #Finds corresponding eigen value\n",
    "        if np.abs((ev - ev_n)/ev) < 0.01:     #If new eigenvalue is within 1% of old one then breaks the loop\n",
    "            break\n",
    "\n",
    "        v = v_n       #stores new eigenvector in old eigenvector \n",
    "        ev = ev_n     #stores new eigenvalue in old eigenvalue \n",
    "\n",
    "    return ev_n, v_n\n",
    "\n",
    "A = np.array([[2,-1,0],[-1,2,-1],[0,-1,2]])\n",
    "E,V = power_iteration(A)\n",
    "print(\"The dominant eigen value is : \",E)\n",
    "print(\"The dominant eigen vactor is : \",V)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
