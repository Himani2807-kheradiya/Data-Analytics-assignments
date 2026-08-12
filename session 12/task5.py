from functools import reduce

numbers = [40, 60, 80, 120]
doubled_numbers = list(map(lambda x: x * 2, numbers))
filtered_numbers = list(filter(lambda x: x > 100, doubled_numbers))
total = reduce(lambda x, y: x + y, filtered_numbers)

print("Doubled Numbers:", doubled_numbers)
print("Numbers greater than 100:", filtered_numbers)
print("Final Sum:", total)