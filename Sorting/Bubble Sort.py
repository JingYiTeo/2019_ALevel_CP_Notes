def Bubble_Sort(A):
    passes = len(A) - 1 # for n items, need n-1 passes
    #Create a for loop for the number of comparisons needed
    for i in range(passes):
        #for loop for each round which we will be comparing the current j with the next j value.
        for j in range(passes - i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    return A


#main
A = [432,12,4,3,6,321]
print(Bubble_Sort(A))
