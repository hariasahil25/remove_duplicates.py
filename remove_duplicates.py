# Program to remove duplicate elements from a list

def remove_duplicates(numbers):
    unique_list = []

    for item in numbers:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list

# Original list
numbers = [1, 2, 3, 2, 4, 1, 5, 3]

# Removing duplicates
result = remove_duplicates(numbers)

# Printing result
print("Original List:", numbers)
print("List after removing duplicates:", result)
