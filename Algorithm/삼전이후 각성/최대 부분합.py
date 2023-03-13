def dynamic_programming(arr):
    cache = [None] * len(arr)
    # 1.
    cache[0] = arr[0]

    # 2.
    for i in range(1, len(arr)):
        cache[i] = max(0, cache[i-1]) + arr[i]

    return max(cache)

def solution(sequence):
    A = [1,-1]
    B = [-1,1]
    length = len(sequence)
    test1 = []
    test2 = []
    if length % 2 == 0:
        test1 = A * (length // 2)
        test2 = B * (length // 2)
    else:
        test1 = A * (length // 2) + [1]
        test2 = B * (length // 2) + [-1]
    for i in range(length):
        test1[i] *= sequence[i]
        test2[i] *= sequence[i]
    a = dynamic_programming(test1)
    b = dynamic_programming(test2)
    if a >= b:
        return a
    else:
        return b
