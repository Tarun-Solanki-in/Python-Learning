import os

# Print the contents of the current directory
directory_path = '/'
contents = os.listdir()

print("Contents of the directory are:")

for item in contents:
    print(item)