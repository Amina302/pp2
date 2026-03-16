import os

if not os.path.exists("test_folder"):
    os.mkdir("test_folder")

os.makedirs("test_folder/sub_folder", exist_ok=True)

print("Current directory:", os.getcwd())

print("\nDirectory contents:")
for item in os.listdir():
    print(item)

os.chdir("test_folder")
print("\nChanged directory:", os.getcwd())