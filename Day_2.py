# Day_2 : Given a sorted array arr[] and number x, write a function that counts the occurrences of x in arr[]
def Sort(l1): 
    for i in range(len(l1)):
        for j in range(i):
            if l1[i] < l1[j]:
                temp = l1[i]
                l1[i] = l1[j]
                l1[j] = temp
    return l1
def Count(x, l1):
    count = 0
    for i in range(len(l1)):
        if l1[i] == x:
            count += 1
    return count
l1 = Sort([4, 2, 4, 4, 3, 2, 1, 1, 3, 3, 3])
x = int(input(f"Enter the element from {l1} to get its frequency? "))
print(f"The frequency of the element {x} in the array {l1} is {Count(x,l1)}")