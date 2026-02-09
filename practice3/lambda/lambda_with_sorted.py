#1
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]

sorted_students = sorted(students, key=lambda x: x[1])

print("Students sorted by age:", sorted_students)

#2

words = ["apple", "pie", "banana", "cherry"]

sorted_words = sorted(words, key=lambda x: len(x))

print("Words sorted by length:", sorted_words)