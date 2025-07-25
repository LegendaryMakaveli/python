space = 11
count = 1
while count < 11 :
	space = 11
	while(space > count) :                                                 
		print("  ", end='' )
		space -= 1
	star = 0
	while star < count :
		print("*", end = ' ')
		star  += 1
	count  +=  1
	
	print()
