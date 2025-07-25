count = 0
while count < 11 :
	star = 0
	while(star < count) :                                                 
		print("*", end = " ")
		star  += 1
	count  +=  1
	print()




count = 11
while count > 0 :
	star = 0
	while(star < count) :
		print("*", end = " ")
		star  += 1
	count  -=  1
	print()



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




space = 11
count = 1
while count < 11 :
	space = 11
	while(space > count) :                                                 
		print(" ", end='' )
		space -= 1
	star = 0
	while star < count :
		print("*", end = ' ')
		star  += 1
	count  +=  1
	
	print()
