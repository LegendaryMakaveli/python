palindrome = int(input("Enter 5 digits:  "))

numberOne = (palindrome // 10000) % 10
numberTwo = (palindrome // 1000) % 10
numberThree = (palindrome // 100) % 10
numberFour = (palindrome // 10) % 10
numberFive = palindrome % 10

if numberOne == numberFive and numberTwo == numberFour :
	print(palindrome, "is a palindrome")
else :
	print(palindrome,"is not a palindrome")