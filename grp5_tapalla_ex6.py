#Write a Python function to find the maximum of three numbers.

def find_maximum(a, b, c):
    return max(a, b, c)
    
#Example usage:
num1 = 40
num2 = 60
num3 = 90
print("Maximum of", num1, ",", num2, "and", num3, "is:", find_maximum(num1, num2, num3))

#Write a Python function to sum all the numbers in a list.

def sum_list_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Example usage:
num_list = [21, 34, 45, 56, 24]
print("Sum of numbers in the list is:", sum_list_numbers(num_list))

#Write a Python program to reverse a string.

def reverse_string(input_string):
    return input_string[::-1]

# Example usage:
original_string = "Good Morning"
reversed_string = reverse_string(original_string)
print("Original string:", original_string)
print("Reversed string:", reversed_string)

#Write a Python function that accepts a string and counts the number of upper and lower case letters.

def count_upper_lower(input_str):
    upper_count = 0
    lower_count = 0

    for char in input_str:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

# Example usage:
input_string = "Hi Hello! Nice to meet you."
upper_count, lower_count = count_upper_lower(input_string)
print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)

# Write a Python function that takes a list and returns a new list with distinct elements from the first list.

def get_distinct_elements(input_lst):
    distinct_lst = []
    for item in input_lst:
        if item not in distinct_lst:
            distinct_lst.append(item)
    return distinct_lst

# Example usage:
original_lst = [1, 2, 3, 4, 2, 3, 5]
distinct_elements = get_distinct_elements(original_lst)
print("Original list:", original_lst)
print("Distinct elements:", distinct_elements)
