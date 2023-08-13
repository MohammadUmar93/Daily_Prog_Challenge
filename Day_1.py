# Day_1 : Find Kth largest element in a given array
def kthLargest(l1, k):
    for i in range(len(l1)):
        for j in range(i):
            if l1[i] > l1[j]:
                temp = l1[i]
                l1[i] = l1[j]
                l1[j] = temp
    return l1[k-1]
l1 = [13, 52, 10, 70, 46, 11, 25, 49, 33, 29]
k = int(input("Which largest element you want?"))
if k == 1:
    print(f"{k}st largest element of the array {l1} is : " + str(kthLargest(l1, k)))
elif k == 2:
    print(f"{k}nd largest element of the array {l1} is : " + str(kthLargest(l1, k)))
elif k == 3:
    print(f"{k}rd largest element of the array {l1} is : " + str(kthLargest(l1, k)))
else:
    print(f"{k}th largest element of the array {l1} is : " + str(kthLargest(l1, k)))
