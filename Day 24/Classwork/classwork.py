#1)

array1 = [1,2,3,4,5,6,7,8,9,10,]
array1.append(1121)
array1.remove(3)

print(array1)

#2)

array2 = []
array2.append(array1)

#3)

array3 = [1,2,3,4,5,6,7,8]

for i in array3:
    if (i % 2) == 0.0:
        print(i, "ლუწია")
    else:
        print(i, "კენტია")
