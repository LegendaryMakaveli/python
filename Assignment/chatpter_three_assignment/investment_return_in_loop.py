principal = int(input("Enter the principal Amount:   "))
rate = int(input("Enter the rate:  "))

YEARLY_RATE = 100

rate_sum = rate / YEARLY_RATE

for year in range(1, 31) :
	amount = principal *(1 + rate_sum)**year
	print(f"{year}{amount: .2f}")