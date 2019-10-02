

import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

V=np.array(([2,-1,-1],[-1,2,-1],[-1,-1,2]))
eigval,eigvec = LA.eig(V)

D = np.diag(eigval)
P = eigvec
print("D=\n",D)
print("P=\n",P)

pi=LA.inv(P)
print("A\n",pi@D@P)
