#for loop
# 1) Write a program that calculates and prints the sum of numbers from 1 to 10 using a for loop.
# შექმენით პროგრამა რომელიც გამოთვლის და დაპრინტავს რიცხვების ჯამს 1-დან 10-მდე for ციკლის გამოყენებით.

sum = 0

for i in range(10):
    i += 1
    sum += i
print(sum)

# 2) Print the squares of numbers from 1 to 15.
# დაპრინტე 1-დან 15-მდე ციფრების კვადრატები.

for i in range(15):
    print(i ** 2)

# 3) Write a program that calculates and prints the sum of squares of numbers from 1 to 5 using a for loop.
# დაწერე პროგრამა რომელიც ითვლის და პრინტავს 1-დან 5-მდე ციფრების კვადრატების ჯამს for ციკლის გამოყენებით.

sum = 0

for i in range(6):

    squ = i * i

    sum += squ 

print(sum)

# 4) Print numbers divisible by both 3 and 5 from 1 to 100 inclusive.
# დაპრინტეთ 1-დან 100-ის ჩათვლით რიცხვები რომლებიც იყოფა 3-ზე და 5-ზე.

for i in range(1,100):
    if (i % 3) + (i % 5) == 0.0:
        print(i)


# 5) Write a program that prints numbers from 10 to 1 in reverse order using a for loop.
# დაწერეთ პროგრამა რომელიც ბეჭდავს ციფრებს 10-დან 1-მდე საპირისპირო თანმიმდევრობით for loop-ის გამოყენებით.

var = 11

for i in range(1,11):
    var -= 1
    print(var)


# while loop
# 1) Calculate the sum of digits of a number entered by the user.
# გამოთვალეთ მომხმარებლის მიერ შეყვანილი რიცხვების ჯამი.

input1 = int(input("Enter first number:"))

input2 = int(input("Enter second number:"))

while True:
    print('Sum of numbers:', input1 + input2)
    break


# 2) Write a program that uses a while loop to print numbers from 10 down to 1.
# დაწერეთ პროგრამა რომელიც იყენებს while ციკლს 10-დან 1-მდე რიცხვების დასაპრინტად.

var = 10

while var != 0:
    print(var)
    var -= 1


# 3) Write a program that calculates and prints the sum of all integers from 1 to 100 using a while loop.
# დაწერეთ პროგრამა რომელიც გამოთვლის და ბეჭდავს ყველა მთელი რიცხვის ჯამს 1-დან 100-მდე while ციკლის გამოყენებით.

sum = 0
var = 0

while True:

    var += 1
    sum += var
    if var == 100:
        break
print(sum)


# 4) Write a program that calculates and prints the square of numbers from 1 to 10 using a while loop.
# დაწერეთ პროგრამა რომელიც გამოთვლის და ბეჭდავს რიცხვების კვადრატს 1-დან 10-მდე while ციკლის გამოყენებით.

var = 1

while var != 10:
    print(var ** 2)
    var += 1


# if-else
# 1) Write an if-else statement to determine if a year entered by the user is a leap year.
# დაწერეთ if-else განცხადება იმის დასადგენად არის თუ არა მომხმარებლის მიერ შეყვანილი წელი ნაკიანი.

input1 = int(input("Enter year:"))

if (input1 % 4) == 0.0:
    print("You entered a leap year.")
else:
    print("You entered a normal year.")


# 2) Check if a given string entered by the user is a palindrome.
# შეამოწმეთ არის თუ არა მომხმარებლის მიერ შეყვანილი მოცემული სტრიქონი პალინდრომი.

input1 = str(input("Enter something:"))

reversed_input1 = input1[::-1]

if reversed_input1 == input1:
    print("Your word is a palindrome.")
else:
    print("you entered a normal word.")


# 3) termine if a number entered by the user is positive, negative, or zero.
# გაარკვიე მომხმარებლის მიერ შეყვანილი რიცხვი არის დადებითი, უარყოფითი თუ ნული.

input1 = int(input("Enter a number:"))

if input1 > 0:
    print("Number is positive.")
elif input1 < 0:
    print("Number is negative.")
else:
    print("Number is zero.")


# 4) calculate the BMI of a person based on their height and weight entered by the user and classify their BMI category using if-else.
# გამოთვალეთ პირის BMI მომხმარებლის მიერ შეყვანილი სიმაღლისა და წონის მიხედვით და დაალაგეთ მათი BMI კატეგორია if-else-ის გამოყენებით.

weight = int(input("Enter your weight:"))

height = int(input("Enter your height:"))

BMI = weight / (height ** 2)

if BMI >= 25.0:
    print("You are overweight.")
elif BMI >= 18.5 and BMI <= 24.9:
    print("You are healthy.")
else:
    print("You are underweight.")

