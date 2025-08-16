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



#using filter to get all even number

def is_even(number) :
	return number % 2 == 0


def return_even(number) :
	if not isinstance(number, list) :
		raise TypeError("Only list is allowed")
	
	for row in number :
		if not isinstance(row, int) :
			raise TypeError("Only integers is allowed")

	if not number :
		raise ValueError("List cannot be empty")

	return list(filter(is_even, number))

# Extract only the words longer than 5

def is_longer(animals) :
	return isinstance(animals, str) and animals != " " and len(animals) > 5

def return_letter_longer_than_five(words) :
	if not isinstance(words, list) :
		raise TypeError("Only list is allowed")

	if  any(not isinstance(word, str) or word == " " for word in words) :
		raise ValueError("No integer allowed and no empty string")
	if not words : 
		raise TypeError("List cannot open")
	
	return list(filter(is_longer, words))

#Keep the first value that is greater than 2


def is_remove(my_list) :
	if isinstance(my_list, list) :
		raise TypeError("Only list is allowed")

	return [value for value in my_list if isinstance(my_list, tuple) and len(my_list) > 0 and my_list[0] > 2]


def filter_first_value_greater_than_2(new_list) :
	if not isinstance(new_list, list) :
		raise TypeError("Only accept list")

	return list(filter(is_remove, new_list))


def is_range(number) :
	if (number) ==  0  :
		raise ValueError
	elif(number) == -1 :
		raise ValueError
	
	for digit in range(1,16) :
		if digit % 3 == 0 and digit % 5 == 0 :
			return digit


















	







		