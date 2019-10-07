# Driver program to test above function

'''

Longest Incresing Sequence

'''

def lis(arr):
    n=len(arr)
    lis=[0]*n

    for i in range(1,n):
        for j in range(0,i):
            if arr[j]<arr[i] and lis[i]<lis[j]+1:
                lis[i]=lis[j]+1

    return max(0,max(lis))





arr = [10, 22, 9, 33, 21, 50, 41, 60]
print("Length of lis is", lis(arr))
