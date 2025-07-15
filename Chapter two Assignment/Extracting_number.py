numberOne = int(input("Enter 5 digit  "))

sum1 = numberOne % 10
sum2 = numberOne / 100  
sum3 = sum2 % 10
sum4 = numberOne % 1000    
sum5 = sum4 / 100
sum6 = numberOne % 10000     
sum7 = sum6 / 1000
sum8 = numberOne / 10000

print(sum8,   sum7,   sum5,   sum3,   sum1)