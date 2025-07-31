import math

def divide_or_square(number) :

	if (number) == float :
		raise ValueError("no float input")
	if int(number) <  0 :
		raise ValueError("no negatives")
	if int(number) == 'a' :
		raise ValueError("length error")
	if int(number) == str :
		raise ValueError("No String")
	if number % 5 == 0 :
		return  round (math.sqrt(number), 2)
	if number % 5 != 0 :
		return number % 5

def calculate_investment(amount, investment_rate, year) :
	if (amount , investment_rate, year) == 'a-z' or (amount , investment_rate, year) == 'A-Z' :
		raise ValueError("No Char allowed")
	elif (amount , investment_rate, year) == " " :
		raise ValurError("No String allow")

	if float(amount) < 0 :
		raise ValueError("No negative value pls!!")
	elif float(investment_rate) < 0 :
		raise ValueError("No negative value pls!!")
	elif int(year) < 0 :
		raise ValueError("No negative value pls!!")

	if float(investment_rate) == 1 :
		raise ValueError ("Rate is too low!!")
	elif float(amount) == 1 :
		raise ValueError("Amount is too low")
	elif int(year) == 2024 :
		raise ValueError("That cant be the year you want to check!!")

	if float(amount) > 2_000_000.000 :
		raise ValueError("Value too high!!")
	elif float(investment_rate) >= 13 :
		raise ValueError("rate too high")
	elif int(year) >= 3200 :
		raise ValueError("year too far")

	INTEREST_RATE = investment_rate / 100

	cal_rate = amount * (1 + INTEREST_RATE)

	future_return = cal_rate*year

	return future_return

#print("Your montly return is: ", calculate_investment(10_000, 5, 330))


def only_float(numberOne, numberTwo) :
	if (numberOne) == int :
		raise ValueError("Only float is allow")
	elif (numberTwo) == int :
		raise ValueError("Only float is allow")

	
	if float(numberOne) > 500.00 :
		raise ValueError("Number too large")
	elif float(numberTwo) >= 500.00 :
		raise ValueError("Number too large")
	

	if float(numberOne) == str :
		raise ValueError("No String allow")
	elif float(numberTwo) == str :
		raise ValueError("No String allow")
	elif numberOne < 0 :
		raise ValueError("No nagative input")
	elif numberTwo < 0 :
		raise ValueError("No nagative input")
	
	if (numberOne, numberTwo) == float :
		return 2
	elif (numberOne, numberTwo ) != float :
		return 0
	elif (numberOne) != float :
		return 1







