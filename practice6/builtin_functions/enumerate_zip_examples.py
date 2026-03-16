names = ["Ali", "Amina", "Sara"]
scores = [85, 90, 78]

#1
print("Using enumerate:")
for index, name in enumerate(names):
    print(index, name)

#2
print("\nUsing zip:")
for name, score in zip(names, scores):
    print(name, score)

#3
numbers = [5, 2, 9, 1]
print("\nSorted numbers:", sorted(numbers))

#4
a = "10"
b = int(a)
print("Type after conversion:", type(b))