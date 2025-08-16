def append_number_to_tuple(numbers_tuple, number_to_add) :
	if not isinstance(numbers_tuple,tuple) :
		raise TypeError("Input must be a tuple")
	
	if not isinstance(number_to_add, int) :
		raise ValueError("Only integers are allowed")

	if not numbers_tuple :
		raise ValueError("Tuple cannot be empty") 
	
	for digit in numbers_tuple :
		if not isinstance (digit, (int)) :
			raise ValueError("Only integers are allowed")

	if len(numbers_tuple) > 5 :
		raise ValueError
	
	new_tuple = numbers_tuple + (number_to_add,)
	return new_tuple


numbers = (3,4,2,4,5)
number_to_join = 88

#print(append_number_to_tuple(numbers, number_to_join))


original_tuple = (1, 2, [3, 4], 5)
original_tuple [2][0] = 99
#print(original_tuple)


#converting from tuple to list

my_fruits = "Apple", "Banana", "Cherry"
#print(my_fruits)
my_list = [my_fruits]
my_list.append("Mango")
my_new_tuple = (my_list)

#print(my_new_tuple)


#unpacking a tuple

my_tuple = (10,20,30,40)

first_packing, second_packing, *last_element = my_tuple
#print(first_packing)
#print(second_packing)
#print(last_element)


#sum up all element in a 2Dlist

def sum_inner(my_list) :
	if not isinstance(my_list, list) :
		raise ValueError("Input must be a 2D list")


	for rows in my_list :
		if not isinstance(rows, list) :
			raise ValueError("This must be a list too")
	for column in rows :
		if not isinstance(column, int) :
			raise ValueError

	if column <= 0 :
		raise ValueError("No negative or Zero Entry")
	if type(my_list) == str :
		raise ValueError("No string allowed")
	
	new_list = []

	for rows in my_list :
		count = 0
		for column in rows:
			count += column
		new_list.append(count)
	
	return new_list
















		