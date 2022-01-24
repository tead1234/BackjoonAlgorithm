import numpy as np
matrix=[[1,3,5,7,9],[2,4,6,8,10],[11,13,15,17,19],[12,14,16,18,20],[21,22,23,24,25]]

row = 0
col = 0

target =13
def solu(matrix,target):
    mt = np.array(matrix)
    for n, i in enumerate(matrix[0]):
        if i == target:
            return True
        if i < target:
            row = n
        if target in mt[:,row]:
            return True

    for m,k in enumerate(mt[:, 0]):
        if k == target:
            return True
        if k< target:
            col = m
        if target in matrix[col]:
            return True
    return False

print(solu(matrix,13))