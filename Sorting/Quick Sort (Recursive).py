def quicksort(elements):

    #check if array is empty
    if elements == []:

        #if it is return null array
        return []

    #otherwise: array has items
    else:

        #the first element is the comparison element
        pivot = elements[0]
        
        #create 2 empty arrays
        less = []
        great = []

        #for loop in iterating through the elements from 2nd element [1] (Cuz first element [0] is pivot value) to end
        for item in elements[1:]:

            
            if item < pivot:
                less.append(item)
            else:
                great.append(item)

        less = quicksort(less)
        great = quicksort(great)
        return less + [pivot] + great

#main
A = [12,32,323,23,1,23,57,5,68]
print(quicksort(A))
