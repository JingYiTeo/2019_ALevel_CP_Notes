#elements have to be sorted before it can be used on Binary Search

def Binary_Search(elements, target):

    #define the starting index
    low = 0

    #end of array = total items - 1 #since the array index starts from 0
    high = len(elements) - 1

    #while loop : as long as the array is not empty
    #when array is empty len(elements) == 0 and high = 0-1 = -1 so low > high == array is empty
    while low <= high:

        #define the middle index
        mid = (low + high) // 2

        #case 1: middle value is the terminating case
        if elements[mid] == target:
            return target

        #case 2: target is smaller than middle therefore it lies on the left side of array == maximum possible value < middle value (so -1 to go to the index on the left of the middle)
        elif target < elements[mid]:
            high = mid - 1

        #case 3:  target is larger than middle therefore it lies on the right side of array == minimum possible value > middle value (so + 1 to go to the index on the right of the middle)
        else:
            low = mid + 1

    #if the array is empty, returns -1
    return -1

#main
items = [21,22,54,123,146,532]
print(Binary_Search(items, 22)) # it will print the item in the array if it exists.
