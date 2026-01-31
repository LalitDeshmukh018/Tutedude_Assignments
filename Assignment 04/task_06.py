import os

filename = input()

if os.path.exists(filename):
    f = open(filename, "r")
    print(f.read())
    f.close()
else:
    print("File not found. Please check the filename.")
