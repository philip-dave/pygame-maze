from random import randint

def get_largest(arr,largest):
    if len(arr)==0:
        return largest
    if arr[len(arr)-1]>largest:
        largest = arr[len(arr)-1]
    arr.pop()
    return get_largest(arr,largest)
    
    

arr = []

for i in range(0,9):
    rand = randint(0,100)
    arr.append(rand)

print(get_largest(arr,0))