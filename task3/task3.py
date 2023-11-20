def insertion_sort(arr):            #O(n^2), best O(n), avg O(n^2)  
    k=0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
            k+=1
        arr[j+1] = key 
    return k

with open("input.txt") as f:
    arr = list(map(int, f.readline().split()))
k=insertion_sort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print(arr[i])
with open("output.txt", "w") as o:
    o.write(str(arr))
    o.write(str(k))