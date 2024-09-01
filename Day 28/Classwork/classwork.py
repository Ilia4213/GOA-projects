#1

for i in range(21):
    print(i)

#2

num1 = int(input('enter number: '))
num2 = int(input('enter second number:'))

for i in range(num1, num2):
    print(i)

#3

for i in range(50, 100):
    print(i)

#4

for i in range(50, 100):
    print(150-i)

#5

sum = 0
for i in range(51):
    print(i)
    sum += i
print(sum)

#6

numm = int(input("enter number: "))

for i in range(numm):
    print(i)

#7

age = int(input("Enter your age: "))

after = age + 10

for i in range(age, after):
    print(i)

#8

n1 = int(input("Enter number 1: ")) #number input
n2 = int(input("Enter number 2: ")) #number input
n3 = int(input("Enter number 3: ")) #number input
n4 = int(input("Enter number 4: ")) #number input
n5 = int(input("Enter number 5: ")) #number input

print(-n1 + n2 * n3 / n4 // n5) #printing result of calculation made with inputs

#9

age = int(input("Enter your age: "))

if age >= 18:
    print("You are adult")
else:
    print("You are kid")

#10

logic = 1 > 2
logic = 56 > 2
logic = 7 > 87
logic = 534 > 99
logic = 4 > 6777

logic = 9 < 4
logic = 5 < 2
logic = 7 < 8
logic = 5 < 9
logic = 0 < 6

logic = 59 <= 54
logic = 55 <= 25
logic = 57 <= 58
logic = 55 <= 95
logic = 50 <= 56

logic = 759 >= 547
logic = 557 >= 725
logic = 757 >= 587
logic = 557 >= 795
logic = 750 >= 567

logic = 4759 != 5474
logic = 5574 != 4725
logic = 4757 != 5874
logic = 5574 != 4795
logic = 4750 != 5674

logic = 14759 == 54741
logic = 55741 == 14725
logic = 14757 == 58741
logic = 55741 == 14795
logic = 14750 == 56741

#11

a = int(input('Enter integer: '))
b = int(input("Enter float: "))

print(a > b)

#12

c = "1"
d = False
e = 2
f = 3.4
g = {5,6}

print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))

#13

h = 0

while h != 10:
    h += 1
    if h % 2 == 0.0:
        print("even")
    else:
        print("odd")

#14

age = int(input("enter age: "))

if age >= 5 and age < 12:
    print("You are kid")
elif age >= 12 and age < 18:
    print("You are teen")
elif age >= 18:
    print("You are adult")

#15

budget = int(input("Enter your money: "))

price = int(input("Enter price of thing you want to buy: "))

if budget - price >= 0:
    print("You can buy")
else:
    print("You can't afford")



















