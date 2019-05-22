def insertion_sort(A):

    #for loop: from the start index of 1 to end of array/list as j
    for j in range(1, len(A)):

        #stores into 'num' the value of the array positioned at index j
        num = A[j]

        #i = j - 1 (think of it as numbers) 
        i = j - 1

        #as long as i is not negative and the value in array at index i > num (which is value at index j)
        while (i >= 0 and A[i] > num):

            #insert the smaller number (j) as A[i] since (i + 1) = j
            A[i + 1] = A[i]

            i = i -1
        #replace the original num with the new displaced num
        A[i + 1] = num

    return A


#main
x = insertion_sort([12,123,334,2,13,8])
print(x)
