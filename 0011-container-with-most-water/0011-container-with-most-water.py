import array
new_array=array.array('i',[1,8,6,2,5,4,8,3,7])
max = 0
for z in range(len(new_array)-1):
    x= z
    hight = new_array[x]
    if (new_array[z + 1] - new_array[z]) > 0:
        y= (new_array[z + 1] - new_array[z]) * hight
        if max < y:
            max=y
    else:
        y= (new_array[z ] - new_array[z + 1]) * hight
        if max < y:
            max=y
print(max)



        
