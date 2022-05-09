arr = [45, 67, 87, 23, 5,  32, 60]

#your code below:
new_list=[]
contj=len(arr)-1
for i in range(0,len(arr)):
    
    new_list.append(arr[contj])
    contj=contj-1
  
print(new_list)