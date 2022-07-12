K = int(input())
for _ in range(K):
    N = int(input())
    d = [''] * 9999
    d[0] = 'Hello '
    d[1] = "Hello Algo "

    for i in range(2, 10):
        d[i] = d[i-2] + d[i-1]

    k = N//11
    c = N%11
    d1 = d[((k+1) * 2) -1]
    if d1[N-1] == ' ':
        print("Hello Algo ")
        continue
    print(d1[N-1])
