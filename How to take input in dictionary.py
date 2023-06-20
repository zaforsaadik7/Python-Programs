my_dict = {}  # Create an empty dictionary

n = int(input("Enter the number of key-value pairs: "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    my_dict[key] = value

print("Dictionary:", my_dict)
