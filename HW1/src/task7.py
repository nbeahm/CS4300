import numpy as np
from sympy import *
matrix = Matrix([[1, 0, 1, 0 , 0 , 0 , 0 , 600],
                    [1, 1, 0, 1 , 0 , 0 , 0 , 0],
                    [0, 1, 0, 0 , 1 , 0 , 0 , 500],
                    [0, 0, 1, 0 , 0 , 1 , 0 , 600],
                    [0, 0, 0, 1 , 0 , 1 , 1 , 0],
                    [0, 0, 0, 0 , 1 , 0 , 1 , 500]
                    ])
M_rref = matrix.rref()
print(M_rref)