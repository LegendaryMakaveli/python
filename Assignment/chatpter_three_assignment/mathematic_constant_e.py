factorial = 1
total = 1
for number in range (1, 11 ) :
	factorial = factorial * number
	total = total + (1 / factorial)
print(f"{total: .1f}")