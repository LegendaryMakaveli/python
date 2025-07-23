principal = int(input("Answer the principal amount   "))
rate = float(input("Enter annual rate  "))
number_of_years = int(input("Enter numbers of years  "))

rate = rate / 100

remaining_deposit = 1 + rate * number_of_years 
sum = principal * remaining_deposit

print("The total money you will have after" , number_of_years,  "years is",  sum)