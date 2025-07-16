principal = int(input("Enter the Principal amount  "))
annual_rate = float(input("Enter annual interest rate  "))
loan_duration = int(input("Enter loan duration  "))

PERCENTAGE = 100
MONTH_IN_YEARS = 12

annual_solve = annual_rate / MONTH_IN_YEARS

calculating_rate = annual_solve / PERCENTAGE

duration_solve = loan_duration * MONTH_IN_YEARS

solve_for_numerator = calculating_rate * (1 + calculating_rate) ** duration_solve

solve_for_denomerator = ((1 + calculating_rate) ** duration_solve) -1

solve_together = solve_for_numerator / solve_for_denomerator

montly_payment = principal * solve_together


print("Your Montly payment is ", montly_payment)