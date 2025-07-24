total_gas_used = 0
total_mile_driven = 0
count = 1

while(count) :
	count= count + 1
	gas_used = float(input("Enter the gallons used:   "))
	
	miles_driven = float(input("Enter the mile driven:   "))

	sum = miles_driven / gas_used
	print(f"The miles/gallon for this tank was: {sum:10.4f} ")

total_gas_used += gas_used
total_mile_driven += miles_driven

sum2 = total_gas_used + total_mile_driven

average = sum2 / count

print("Total average miles/gallon was", average)