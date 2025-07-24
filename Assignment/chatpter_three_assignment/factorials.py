factorial = int(input("Enter a number:   "))

total = 1
for number in range (1, factorial + 1) :
	total *= number
print(total)