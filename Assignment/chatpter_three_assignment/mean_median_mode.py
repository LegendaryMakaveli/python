my_list = [9,11,22,34,17,22,34,22,40];

total = 0
mean = 0

for number in my_list :
	total = total + number

mean = total / 9
median = my_list[4]
mode = my_list[2]

print(my_list)
print(f"The mean is {mean: .2f}")
print("The median is: ", median)
print("The mode is: ", mode)

my_list_with_outlier = [9,11,22,34,17,22,34,22,40,34];

total = 0
mean = 0
median = 0

for number in my_list_with_outlier :
	total = total + number
mean = total / 10
median = (my_list_with_outlier[4] + my_list_with_outlier[5]) / 2
mode = my_list_with_outlier[2]

print(my_list_with_outlier)
print(f"The mean after an outlier was added is: {mean: .2f}")
print(f"The median after an outlier was added is: {median: .2f}")
print("The mode is: ", mode)