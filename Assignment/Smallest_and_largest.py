numberOne = int(input("Enter first number  "))
numberTwo = int(input("Enter second number  "))
numberThree = int(input("Enter third number  "))

sum =numberOne + numberTwo + numberThree
print("The sum is  ", sum)

average = sum / 3
print("The average is ", average)

product = numberOne * numberTwo * numberThree
print("The product is ", product)

largest = numberOne
smallest = numberOne

if (numberTwo > largest) : largest = numberTwo
if (numberThree > largest) : largest = numberThree
print("The largest is", largest)

if (numberTwo < smallest) : smallest = numberTwo
if (numberThree < smallest) : smallest = numberThree
print("The smallest is " , smallest)