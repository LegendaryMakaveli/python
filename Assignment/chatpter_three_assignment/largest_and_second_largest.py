number = int(input("Enter number:  "))

largest = number
smallest = number

for number in range(1, 5) :
	number = int(input("Enter number:  "))
	if number < largest > smallest :
		print(number, "is the second largest")