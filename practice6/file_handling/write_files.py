#1
with open("demofile.txt", "a") as f:
    f.write("\nNow the file has more content!")

with open("demofile.txt", "r") as f:
    print("After append:")
    print(f.read())
#2
with open("demofile.txt", "w") as f:
    f.write("Woops! I have overwritten the file content!")

with open("demofile.txt", "r") as f:
    print("\nAfter overwrite:")
    print(f.read())

