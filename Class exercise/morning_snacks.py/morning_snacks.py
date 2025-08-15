def square_of_a_list(number) :
	if number  ==  0 :
		raise ValueError
	elif type(number ) == str :
		raise ValueError
	
	return number**2
numbers = [1,2,3,4,5]
print(list(map(square_of_a_list, numbers)))


def length_of_a_list(number) :
	if number == [0,0,0,0,0] :
		raise ValueError

	return number
word = ["apple", "car"]
print(list(map(len,word)))


def even_number(number) :
	return number % 2 == 0

def is_even(number) :

	if (number) == 0 :
		raise ValueError
	if type(number) == str :
		raise TypeError
	return list(filter(even_number, number))

numbers = [2,3,4,2,34,5,6,4,7]
print (is_even(numbers))


def is_more_than_five(number) :
	name = str(number)
	highest_length = 5
	if len(name) <= highest_length :
		return number

def length_of_character(number) :
	if type(number) == int :
		raise TypeError
	elif type(number) == float :
		raise TypeError

	return list(filter(is_more_than_five, number))

words = ["apple", "banana", "kiwi", "Cherry", "grapes"]
print(length_of_character(words))


	



















