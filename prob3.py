
import os  # Import the os module

# Specify the directory path
path = r"C:\Users\User\Downloads\Python full course\Chapter 1"  

# Get the list of files and folders in the directory
contents = os.listdir(path)

# Print each file and folder name
for item in contents:
    print(item)
