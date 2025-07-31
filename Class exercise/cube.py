def get_cube(number) :
	if type(number) == str :
		raise ValueError
	return number **3