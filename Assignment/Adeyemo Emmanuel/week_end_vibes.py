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


def sum_even_number(numbers) :
	count = 0
	for index, digit in enumerate(numbers) :
		if (index % 2 == 0) :
			count+= digit
		
	return count

print((3), "The sum of numbers at even position is: ", sum_even_number([2,1,2,4,2,5,2]))


def sum_odd_number(numbers) :
	count = 0
	for index, digit in enumerate(numbers) :
		if (index % 2 != 0) :
			count+= digit
		
	return count

print((4), "The sum of numbers at odd position is: ", sum_odd_number([2,1,2,4,2,5,2]))


def multiply_odd_number(numbers) :
	count = 1
	for digit in range(1, len(numbers), 3) :
		count = count * digit
		
	return count

print((5), "Multiply element at third position: ", multiply_odd_number([2,1,2,4]))


def calculate_average(numbers) :
	calculate_average = 0
	count = 0
	for digit in numbers :
		count += digit
	calculate_average = count / len(numbers)

	return calculate_average

print((6), "Average of all element:  ", calculate_average([2,1,2,4,4,5,6,7]))


def largest_and_smallest(numbers) :
	largest = 0
	smallest = numbers[1]
	for digit in numbers :
		if digit > largest :
			largest = digit
		if digit < smallest :
			smallest = digit

	return [largest,smallest]

print((7), "Largest and smallest: ",  largest_and_smallest([2,1,2,4,4,5,6,7,0,9]))


def count_string(sentence) :
	count = 0
	for word in sentence :
		count+= 1
	if count >= 2 and sentence[0] == sentence[-1] :
		return sentence

print((8), "Return Sentence : ",   count_string(["ikka", "makaveli", "trevor", "emma", "ikka"]))











