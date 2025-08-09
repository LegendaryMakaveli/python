import random

def random_number(numbers) :
	my_list = []

	for number in range(10) :
		Numbers = random.randint(1, 50)
		my_list.append(Numbers)

	return my_list

print ((1), "Random number in list: ", random_number(100))


def get_the_length(numbers) :
	count = 0
	for digit in numbers :
		count+= 1

	return count

print((2), "The length of the list is : ", get_the_length([2,3,4,5,6,7,8]))

def sum_at_even_position