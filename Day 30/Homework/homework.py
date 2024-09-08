#1)

def evenOrOdd():
    num = int(input("Enter number: "))
    if num / 2 == 0.0:
        print("Your number is even.")
    else:
        print("Your number is odd.")

#2)

def posOrNeg():
    num = int(input("Enter number: "))
    if num > 0:
        print("Your number is positive.")
    elif num == 0:
        print("Your number is 0.")
    else:
        print("Your number is negative.")

#3)

def m5():
    num = int(input("Enter number: "))
    if num % 5 == 0.0:
        print("Your number is multiple of 5.")

#4)

def age():
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You are adult.")

#5)

def square():
    num = int(input("Enter number: "))
    print("Square of", num, "is: ", num * num)

#6)

def security():
    pas = input("Enter password: ")

    while len(pas) < 8:
        pas = input("Password length should e at least 8 symbols, enter again: ")
    print("You have registered.")

#7)

def squares():
    nums = []

    for i in range(10):
        num = int(input("Enter number: "))
        nums.append(num)

    for i in range(10):
        print(nums[i] ** 2)




