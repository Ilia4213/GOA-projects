#1)
list = []
list = [1,2,3,4,5,6,7,8,9,10]

#2)

list1 = [2,4,6,8,10]
list2 = [1,3,5,7,9]

list1.extend(list2)

#3)

array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in array:
    print(i)

#4)

array1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
array2 = []
array3 = []
for i in array1:
    if i % 2 == 0:
        array2 += i
    else:
        array3 += i
print(array2)
print(array3)