arr=[2,4]
target=6
'''
This code - is to find combination of sum repeating the elements 
I tried to optimize this code and do comment if you find some better solutions 
'''

def func(arr,target):
    result=[]
    def addfun(arr,target,temp):
        for i in arr:
            if i>target:
                break
            temp.append(i)
            if i==target:
                result.append(temp.copy())
                temp.pop()
                break
            else:
                addfun(arr[arr.index(i):], target-i, temp)
                temp.pop()

    addfun(arr,target,[])
    return result

print(func(arr,target))




