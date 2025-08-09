for adjacent in range(1, 21) :
	for opposite in range(adjacent, 21):
		for hypotenuse in range (opposite, 21) :
			if adjacent ** 2 + opposite ** 2 == hypotenuse ** 2 :
				print(adjacent, opposite, hypotenuse)


					# formular

	# hytopenuse ** 2 = opposite ** 2 + adjacent ** 2


opposite = int(input("Enter the opposite side:  "))
adjacent = int(input("Enter the adjacent side:  "))

sum1 = opposite ** 2
sum2 = adjacent ** 2

hypotenuse = sum2 + sum1
print(f"The hypotenuse value is: {hypotenuse}")