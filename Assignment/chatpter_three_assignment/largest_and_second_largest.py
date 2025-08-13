number = int(input("Enter number:  "))

largest = number
smallest = number
secondLargest = 0

for number in range(1, 5) :
	number = int(input("Enter number:  "))
	if number < largest > smallest :
		secondLargest = number
	print(secondLargest, "is the second largest")