def quicksort(elements):
    #see if the array is empty
    if len(elements) == 0:
        #if it is, return the null array
        return []

    #otherwise == array has items
    else:
                #for loop through the array from 2nd element [1] to end then if i < first element [0] put in the first quicksort 
        return (quicksort([i for i in elements[1:]
                          if i < elements[0]])

                #first element is the pivot/comparison element, anything lesson goes before and larger goes behind, it changes after every sort
                + [elements[0]]

                #same as first quicksort but now is i >= pivotal element so put to the right (2nd quicksort)
                + quicksort([i for i in elements[1:]
                             if i >= elements[0]]))

#main
print(quicksort([12,23,4,2,5,6,434,2345,3,234,223]))
