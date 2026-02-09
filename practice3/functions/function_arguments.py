#1
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#2
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
#3
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

#4
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)

#5
def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)