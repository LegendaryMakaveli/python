palidome = input("Enter User input:  ")
revsed_num = ""
for num in reversed(palidome) :
	revsed_num += num	

if palidome == revsed_num :
	print("number is a palindrome")
else :
	print("number is not a palindrome")	