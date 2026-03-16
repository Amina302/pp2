import shutil
import os
#1
source_file = "demofile.txt"
backup_file = "backup_demofile.txt"

if os.path.exists(source_file):
    shutil.copy(source_file, backup_file)
    print("File copied successfully")
else:
    print("Source file does not exist")

#2
if os.path.exists(backup_file):
    os.remove(backup_file)
    print("Backup file deleted")
else:
    print("Backup file not found")