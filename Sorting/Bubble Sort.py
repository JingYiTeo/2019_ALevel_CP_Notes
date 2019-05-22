def Bubble_Sort(A):
    passes = len(A) - 1 # for n items, need n-1 passes
    swapped = True # assume not sorted
    while swapped:
        swapped = False
        i = 1
        while i <= passes:
            if A[i-1] > A[i]:
                A[i-1], A[i] = A[i], A[i-1]
                swapped = True
                i = i + 1
            passes = passes - 1
    return A


#main
A = [432,12,4,3,6,321]
print(Bubble_Sort(A))
