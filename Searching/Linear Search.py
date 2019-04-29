#Linear Search
#1----------Last
#start from 1 and search for target and return target position
#else return -1

def linear_search(elements, target): #This function takes in 2 parameters, 1 array where the target is in and the target.
    for i in range(len(elements)):  # A for loop to iterate through all elements in the array
        if elements[i] == target:
            return i #the i will include 0 since array index in python starts from 0
    return -1

#main
items = [12,32,6,2,3,5,7]
print(linear_search(items, 7))

#Efficiency of the search: Not efficient as it would only be quick if the target is at the front or the array size is small.
#On Avg will search n/2 items (half the array)
#Worst Case senario = O(n) [Search n items, the whole array]
