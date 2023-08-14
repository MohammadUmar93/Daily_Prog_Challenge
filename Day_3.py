# Day_3 : Given an array arr[] of non-negative integers and an integer sum, find a subarray that adds to a given sum.
# There may be more than one subarray with sum as the given sum, print first such subarray.
def firstSubArrayWithSum(arr, sum):
    Sum = 0
    subArray = []
    for i in range(len(arr)):
        if Sum < sum :
            # print(f"Sum before adding {arr[i]} = {Sum}")
            Sum += arr[i]
            # print(f"Sum after adding {arr[i]} = {Sum}")
            # print(f"SubArray before appending {arr[i]} = {subArray}")
            subArray.append(arr[i])
            # print(f"SubArray after appending {arr[i]} = {subArray}")
            i += 1
            if Sum == sum :
                return subArray
            else :
                j = 0
                while Sum > sum : 
                    if arr[j] not in subArray:
                        return None
                    # print(f"Sum before subtracting {arr[j]} = {Sum}")
                    Sum -= arr[j]
                    # print(f"Sum after subtracting {arr[j]}  = {Sum}")
                    # print(f"SubArray before removing {arr[j]} = {subArray}")
                    subArray.remove(arr[j])
                    # print(f"SubArray after removing {arr[j]} = {subArray}")
                    j += 1
                    if Sum == sum :
                        return subArray
    return None 

def createArray():
    List = []
    choice = 'y'
    while choice == 'y':
        elem = int(input("Enter element of the list/array : "))
        List.append(elem)
        print(f"Array = {List}")
        choice = input("Do you want to add more elements(y/n) : ")
    return List
        
inp = 1
while inp == 1:
    l1 = createArray()
    sum = int(input("Enter the Sum : "))
    firstArray = firstSubArrayWithSum(l1, sum)
    print(firstArray)
    inp = int(input("Enter 1 to continue"))