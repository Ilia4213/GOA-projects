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


