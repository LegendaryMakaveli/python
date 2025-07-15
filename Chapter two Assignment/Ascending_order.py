numberOne = float(input("Enter the first float number  "))
numberTwo = float(input("Enter the second float number  "))
numberThree = float(input("Enter the third float number  "))


largest = 0
second_largest = 0
smallest = 0


if (numberOne > numberTwo and numberOne > numberThree) : largest = numberOne
if (numberTwo > numberOne and numberTwo > numberThree) : largest = numberTwo
if (numberThree > numberTwo and numberThree > numberOne) : largest = numberThree

print("The largest is  ", largest)



if (numberOne > numberTwo and numberOne < numberThree) : second_largest = numberOne
if (numberOne < numberTwo and numberOne > numberThree) : second_largest = numberOne

if (numberTwo > numberOne and numberTwo < numberThree) : second_largest = numberTwo
if (numberTwo < numberOne and numberTwo > numberThree) : second_largest = numberTwo

if (numberThree > numberOne and numberThree < numberTwo) : second_largest = numberThree
if (numberThree < numberOne and numberThree > numberTwo) : second_largest = numberThree

print("The second largest is  ", second_largest)


if (numberOne < numberTwo and numberOne < numberThree) : smallest = numberOne
if (numberTwo < numberOne and numberTwo < numberThree) : smallest = numberTwo
if (numberThree < numberOne and numberThree < numberTwo) : smallest = numberThree

print("The smallest is  ", smallest)