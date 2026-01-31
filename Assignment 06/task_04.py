try:
    filename = input("Enter file name: ")
    file = open(filename, "r")
    for i in range(3):
        print(file.readline().strip())
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
finally:
    print("File operation attempted.")
