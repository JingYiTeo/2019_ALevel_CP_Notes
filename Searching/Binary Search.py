def binary_search(elements, target, low, high):

    #define the middle item index
    mid = (high + low) // 2
    if low > high: # not found
        return -1

    #target is exactly in the middle of array
    elif elements[mid] == target: #found
        return mid

    #binary search divides the problem case by half each time
    elif target < elements[mid]: #recursive case 1 : target is smaller than middle so its on the left of array (from low to mid -1)
        return binary_search(elements, target, low, mid-1)

    
    else: #recursive case 2: target is larger than middle so its on the right of array (from mid+1 to high)
        return binary_search(elements, target, mid+1, high)

#main
items = [1,2,3,4,5,6,7,8]
print(binary_search(items, 2, 0, len(items)-1)) #it will print the index of target in the array.
