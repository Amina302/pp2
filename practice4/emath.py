import math
#1
degree = float(input("Input degree: "))
radian = degree * math.pi / 180
print("Output radian:", radian)
print()

#2
height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))
area_trapezoid = 0.5 * (base1 + base2) * height
print("Expected Output:", area_trapezoid)
print()

#3
n_sides = int(input("Input number of sides: "))
side_length = float(input("Input the length of a side: "))
area_polygon = n_sides * side_length * side_length / (4 * math.tan(math.pi / n_sides))
print("The area of the polygon is:", area_polygon)
print()

#4
base = float(input("Length of base: "))
height_para = float(input("Height of parallelogram: "))
area_parallelogram = base * height_para
print("Expected Output:", area_parallelogram)
print()