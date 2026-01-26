#1
a = 5
b = 2
if a > b: print("a is greater than b")
#2
a = 2
b = 330
print("A") if a > b else print("B")

#3
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#4
x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)

#5
username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)