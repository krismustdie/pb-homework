def Check(A):
    flag = True
    for i in range(len(A) - 1):
        if A[i] > A[i + 1]:
            flag = False
            break
    return flag


def Bubble_Sort(A):  # Обменная сортировка (метод пузырька)
    for i in range(1, len(A)):
        for n in range(len(A) - 1, i - 1, -1):
            if A[n] < A[n - 1]:
                A[n], A[n - 1] = A[n - 1], A[n]
    return A


def Merge_Sort(A): # Сортировка слиянием
    if len(A) <= 1:
        return A
    else:
        m = len(A) // 2
        L = Merge_Sort(A[:m])
        R = Merge_Sort(A[m:])
        return Merge(L, R)


def Merge(L, R):
    i, j = 0, 0
    B = []
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            B.append(L[i])
            i += 1
        else:
            B.append(R[j])
            j += 1
    for i in range(i, len(L)):
        B.append(L[i])
    for j in range(j, len(R)):
        B.append(R[j])
    return B


def Insert_Sort(A):  # Сортировка простыми вставками
    counter = 0
    for k in range(1, len(A)):
        B = A[k]
        if max(A[0:k]) > B:
            j = 0
            while A[j] < B:
                j += 1
            A[j + 1:k + 1] = A[j:k]
            A[j] = B
            counter += 1
    print(counter)
    return A


def Quick_Sort(A):
    less = []
    equal = []
    greater = []
    if len(A) > 1:
        p = A[len(A)//2]
        for x in A:
            if x < p:
                less.append(x)
            if x == p:
                equal.append(x)
            if x > p:
                greater.append(x)
        return Quick_Sort(less) + equal + Quick_Sort(greater)
    else:
        return A
