from functools import reduce

numbers = [1, 2, 3, 4, 5]
#1
squared = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared)
#2
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)
#3
total = reduce(lambda a, b: a + b, numbers)
print("Sum of numbers:", total)