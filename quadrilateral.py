import numpy as np

def quadrilateral(x1y1z1, d1, x2y2z2, d2, x3y3z3, d3, x4y4z4, d4):
    x1, y1, z1 = x1y1z1
    x2, y2, z2 = x2y2z2
    x3, y3, z3 = x3y3z3
    x4, y4, z4 = x4y4z4
    A11 = 2 * (x1 - x2)
    A12 = 2 * (y1 - y2)
    A13 = 2 * (z1 - z2)
    A21 = 2 * (x1 - x3)
    A22 = 2 * (y1 - y3)
    A23 = 2 * (z1 - z3)
    A31 = 2 * (x1 - x4)
    A32 = 2 * (y1 - y4)
    A33 = 2 * (z1 - z4)
    temp1 = d1**2 - x1**2 - y1**2 - z1**2
    b1 = d2**2 - x2**2 - y2**2 - z2**2 - temp1
    b2 = d3**2 - x3**2 - y3**2 - z3**2 - temp1
    b3 = d4**2 - x4**2 - y4**2 - z4**2 - temp1
    A = np.array([[A11, A12, A13], 
                     [A21, A22, A23], 
                     [A31, A32, A33]])
    b = np.array([[b1],
                     [b2],
                     [b3]])
    AInv = np.linalg.inv(A)
    result = AInv.dot(b)
    return result[0, 0], result[1, 0], result[2, 0]