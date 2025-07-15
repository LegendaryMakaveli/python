print ("Welcome to programming with python" +  " " + "silentfinders");

nameOne = input ("Enter you name:  ")
ageOne = int(input ("Enter your age:  "))
heightOne = float(input("Enter your height:  "))

nameTwo = input("Enter your name:  ")
ageTwo = int (input ("Enter your age:  "))
heightTwo = float(input("Enter your height:  "))

if (ageOne > ageTwo):
	print(nameOne + " " + "is older than" + " " + nameTwo)
else :
	print(nameTwo + " " + "is older than" + " " + nameOne)