current_world_population = float(input("Enter the current world population:  "))
current_world_growing_rate = float(input("Enter the current rate:  "))
year = int(input("Enter the year:  "))




CURRENT_POPULATION = 8_100_000_000
GROWING_RATE =0.009

total = CURRENT_POPULATION * GROWING_RATE

calculate_world_growth = year * total

print(f"{calculate_world_growth: .4f}")
