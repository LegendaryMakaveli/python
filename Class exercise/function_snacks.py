import math

def divide_or_square(number) :
	if type (number) == float :
		raise ValueError

	if number % 5 == 0 :
		return round(math.sqrt(number), 2)
	elif number % 5 != 0 :
		return number % 5

	if type (number) == str :
		raise ValueError

	