{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 7.74629295  0.4213137  -0.07173251 -0.52620804  0.01054669]\n",
      "Number of iterations: 14\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "from numpy import linalg as LA\n",
    "\n",
    "\n",
    "def check(b,B):\n",
    "    c = b-B\n",
    "    d = np.sqrt(np.dot(c,c))\n",
    "    return(d)\n",
    "\n",
    "\n",
    "\n",
    "A = np.array([[0.2, 0.1, 1, 1, 0], [0.1, 4, -1, 1, -1], [1, -1, 60, 0, -2], [1, 1, 0, 8, 4], [0, -1, -2, 4, 700]])     #A matrix of Ax=b\n",
    "b=np.array([1,2,3,4,5])   # b\n",
    "B=np.array([0,0,0,0,0])     #B for initial tollrence\n",
    "x= np.array([1,0,1,1,1])\n",
    "w=1.25\n",
    "D = np.zeros((5,5))\n",
    "L = np.zeros((5,5))   \n",
    "U = np.zeros((5,5))\n",
    "\n",
    "for i in range (0,5):\n",
    "    for j in range(0,5):\n",
    "\n",
    "        if(j<=i):\n",
    "            L[i][j]=A[i][j]         #creating Lower triangular matrix \n",
    "        elif(j>i):\n",
    "            U[i][j]=A[i][j]\n",
    "        elif(j==i):\n",
    "            D[i][i] = A[i][i]\n",
    "\n",
    "    \n",
    "i=0\n",
    "\n",
    "while check(b,B)>0.01:                  #derivation for this algorythm - wikipedia \n",
    "    \n",
    "    LU_i = LA.inv(D+w*L)\n",
    "    As = w*U + (w-1)*D\n",
    "    b_n = w*b\n",
    "    Asx = np.dot(As,x)\n",
    "    \n",
    "    Af = b_n - Asx\n",
    "    \n",
    "    x = np.dot(LU_i,Af)\n",
    "    \n",
    "    B = np.dot(A,x)\n",
    "    i=i+1\n",
    "\n",
    "print(x)\n",
    "print(\"Number of iterations:\",i)\n",
    "#print(B)\n",
    "\n",
    "\n",
    "\n"
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
