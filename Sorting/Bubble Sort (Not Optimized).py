def bubble_sort(A):

    #assume not sorted
    swapped = True

    #while swapped: as long as its not swapped
    while swapped:

        swapped = False

        #for loop: iterate through all the elements from index 1 to end
        for i in range(1, len(A)):

            #if the previous element > element after it 
            if A[i-1] > A[i]:

                #swap their places
                A[i-1], A[i] = A[i], A[i-1]

                #swapped is done for this element
                swapped = True

                #and it goes back to the next element in the for loop

    #return the sorted array/list
    return A

#main
A = [4,5,3,123,32,6,2]
print(bubble_sort(A))
