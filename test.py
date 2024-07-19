Money_Per_Month = 200
Interest_Per_Month = 0.003333333333333333333333333333333333333333
Month = 12 * 1
Money = 0

for i in range(Month):
    Money += Money_Per_Month
    Money += Money * Interest_Per_Month
print("After 1 year of working and saving money in bank, your interest made you:", int(Money - (Money_Per_Month * Month)),"Lari")
print("Thats only interest, and your whole money is:", int(Money),"Lari")
