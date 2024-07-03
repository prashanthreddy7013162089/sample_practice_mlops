arr=[1,2,3,4,5,6,7,8]
left=0 
target=3
right=arr[len(arr)-1]
while(left<=right):
    if (target==arr[(left+right)//2]):
        print((left+right)//2)
        break
    elif (target>arr[(left+right)//2]):
        left=(left+right)//2+1 
    elif (target<arr[(left+right)//2]):
        right=(left+right)//2-1 
    else:
        print("please enter correct number")