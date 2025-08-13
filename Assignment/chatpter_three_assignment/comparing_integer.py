print("Enter two integers, and i will tell you,", "the relationships they satisfy. ")

numberOne = int(input("Enter first integer:  "))
numberTwo = int(input("Enter second integer:  "))

if numberOne == numberTwo :
	print(numberOne, "is equal to", numberTwo)
else:
	print(numberOne, "is not equal to", numberTwo)
if numberOne > numberTwo :
	print(numberOne, "is greater than", numberTwo)
else :
	print(numberOne, "is less than", numberTwo)
if numberOne <= numberTwo :
	print(numberOne, "is less or equal to", numberTwo)
else :
	print(numberOne, "is greater or equal to", numberTwo)