from collections import deque
R = [[0,2,3],[0,2,3],[4,5,5]]
R = deque(R)
for r in R.copy():
    a,b,c, = r
    if a == 0:
        for i,y in enumerate(R):
            d,f,g = y
            if a == d:
                R[i] = [d-1,f,g]

print(R)