response = input("What is your problem?:   ")
response2 = input("Have you had this problem before:   ")
if response2 == 'Yes' or response2 == 'yes' or response2 == 'YES':
	print("well, you will have it again")
elif response2 == 'No' or response2 == 'no' or response2 == 'NO':
	print("well, You have it now")
else:
	print("invalid input")