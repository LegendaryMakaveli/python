from functools import reduce

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
	
	total = list(map(sum, my_list))
	return total

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
	
	if not new_list :
		raise TypeError("list cannot be empty")

	return list(filter(is_remove, new_list))


def is_range(number) :
	if (number) ==  0 or number == -1 :
		raise ValueError	
	return number % 3 == 0 and number % 5 == 0	

def filter_numbers(number) :
	if not isinstance(number, list) :
		raise TypeError("Accept only list")
	
	if not number :
		raise TypeError("Cannot be empty")

	return list(filter(is_range, number))


# Filter all palindromes

def is_palindrome(word) :
	if isinstance(word, int) :
		raise ValueError("Integers is not allowed")
	
	if not word :
		raise TypeError("Can't leave this open")

	new_word = word.lower()
	return new_word == new_word[: : -1]

def check_for_palindrome(words) :
	if not isinstance(words, list) :
		raise TypeError("Only accept list")
	
	if not words :
		raise TypeError("List cannot be empty")

	for rows in words :
		if isinstance(rows, int) :
			raise ValueError("No integers allowed")

	return list(filter(is_palindrome, words))


def convert_to_upper(words) :
	if not isinstance(words, list) :
		raise TypeError("Only list is accepted")
	
	if not words :
		raise TypeError("Cannot be empty")	

	for rows in words :
		if isinstance(rows, int) :
			raise ValueError("No integers")
		elif isinstance(rows, float) :
			raise ValueError("No float too")

	return list(map(str.upper, words))

#Square all number in a list/range

def square_number(numbers) :
	if not isinstance(numbers, list) :
		raise TypeError("Only list is accepted")

	if not numbers :	
		raise TypeError("cannot be empty")

	for digit in numbers :
		if isinstance(digit, str) :
			raise ValueError("NO string allowed")
		elif isinstance(digit, float) :
			raise ValueError("No float too")

	return list(map(lambda number: number ** 2, numbers))


#Capitalizes the first letter

def capitalize_first_letter(words) :
	if not isinstance(words, list) :
		raise TypeError("Must be a list")

	if not words :	
		raise TypeError("Cannot be empty")

	for rows in words :
		if isinstance(rows, int) :
			raise ValueError("No integers pls")
		elif isinstance(rows, float) :
			raise ValueError("And no float too")

	return list(map(str.capitalize, words))

#Add 10% tax

def add_tax(numbers) :
	if not isinstance(numbers, list) :
		raise TypeError("Must be a list")
	
	if not numbers :
		raise TypeError("cannot be empty")
	
	for digit in numbers :
		if isinstance(digit, str) :
			raise ValueError("String is not welcome")

	return list(map(lambda number: number * 1.1, numbers ))

def sum_all_numbers(numbers) :
	if not isinstance(numbers, list) :
		raise TypeError("Must be a list")
	
	for digits in numbers :
		if isinstance(digits, str) :
			raise ValueError("No string allowed")
		elif isinstance(digits, float) :
			raise ValueError("No float too")

	return reduce(lambda valueOne, valueTwo : valueOne + valueTwo, numbers)


def find_the_largest(numbers) :
	if not isinstance(numbers, list) :
		raise TypeError("List is expected")

	if not numbers :
		raise TypeError("Cannot be empty")

	for digits in numbers :
		if isinstance(digits, str) :
			raise ValueError("No string allowed")
		elif isinstance(digits, float) :
			raise ValueError("No float as well")

	return reduce(lambda valueOne, valueTwo :  valueOne if valueOne > valueTwo else valueTwo, numbers)


#concetenate string into single string

def concatenate_string(words) :
	if not isinstance(words, list) :
		raise TypeError("list is expected")
		
	if not words :
		raise TypeError("cannot be empty")

	for rows in words :	
		if isinstance(rows, int) :
			raise ValueError("No integers allowed")
		elif isinstance(rows, float) :
			raise ValueError("No float as well")
		
		return reduce(lambda valueOne, valueTwo : valueOne + " " + valueTwo, words)


#find the product

def find_product(numbers) :
	if not isinstance(numbers, list) :
		raise TypeError("Only string is accepted")
	
	if not numbers :
		raise TypeError("Cannot be empty")

	for digits in numbers :
		if isinstance(digits, str) :
			raise ValueError("No string allowed")
		elif isinstance(digits, float) :
			raise ValueError("No float as well")

	result = map(lambda digit : digit * 2, numbers)
	return reduce(lambda valueOne, valueTwo : valueOne * valueTwo, result)


#sum all element and use filter to keep the largest

def sum_all_elements(numbers) :
	if not isinstance(numbers, list) :
		raise TypeError("Only list is allowed")

	if not numbers :
		raise TypeError("Cannot be empty")

	for row in numbers  :
		for column in row :
			if isinstance(column, str) :
				raise ValueError("No string allow")
			elif isinstance(column, float) :
				raise ValueError("And no float")

	total = list(map(sum, numbers))
	return total

def is_greater(number) :
	if not isinstance(number, list) :
		raise TypeError("Only list")

	if not number :
		raise TypeError("Cannot be empty")

	for rows in number :
		if isinstance(rows, str) :
			raise ValueError("No string")
		elif isinstance(rows, float) :
			raise ValueError("And no float")

	return max(number)
	

def remove_non_numeric(number) :
	if not isinstance(number, list) :
		raise TypeError("Only list is allowed")

	for row in number :
		if isinstance(row, float) :
			raise ValueError("No float")

	number_only = [digit for digit in number if digit.isdigit()]
	numbers = [int(digit) for digit in number_only]
	return sum(numbers)



























	







		