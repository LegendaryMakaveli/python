count = 1
number = int(input("Enter a number:  "))
largest = number
smallest = number
total = number
average = number
product = 1
while count < 4 :
	count = count + 1
	number =int(input("Enter a number:   "))
	if number > largest : largest = number
	if number < smallest : smallest = number
	total += number
	average = total / 4
	product *= number
	

print("The largest is", largest)
print("The smallest is ", smallest)
print("The sum is ", total)
print("The average is ", average)
print("The product is ", product)

