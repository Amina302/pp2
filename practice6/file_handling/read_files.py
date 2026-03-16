#1
with open("demofile.txt", "r") as f:
    content = f.read()
    print("Full file content:")
    print(content)


#2:
with open("demofile.txt", "r") as f:
    print("\nFirst 5 characters:")
    print(f.read(5))


#3
with open("demofile.txt", "r") as f:
    print("\nFirst line:")
    print(f.readline())


#4
with open("demofile.txt", "r") as f:
    print("\nReading line by line:")
    for line in f:
        print(line.strip())