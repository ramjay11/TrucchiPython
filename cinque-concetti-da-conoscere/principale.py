'''
Immutable
str
float
bool
byte
tuple

Mutable
list
set
dictionary
'''
# x = (1, 2) # tuple
x = [1, 2] # list, a mutable type
y = x
# x = (1, 2, 3) # reassigning
x[0] = 100
print(x, y) # y will make a copy of the immutable tuple(x)
# x[0] = 1 # tuple object doesn't support item assignment
print("--------------------------------")
# defines a function named get_largest_numbers that takes two parameters: numbers, 
# which is a list of numbers, and n, which is the number of largest numbers to return
def get_largest_numbers(numbers, n):
    # sorts the list numbers in ascending order. This is important because the function
    # aims to return the n largest numbers, so sorting the list makes it easier to pick the largest ones
    numbers.sort()
    # returns the last n elements of the sorted list numbers. Since the list has been sorted in ascending order, 
    # the last n elements will be the largest ones.
    return numbers[-n:]
#  initializes a list named nums containing some unsorted numbers
nums = [2, 3, 4, 1, 34, 123, 234, 1]
# calls the get_largest_numbers function with nums as the list of numbers and 2 as the number of
# largest numbers to return. It stores the result in a variable named largest
print(nums) # unsorted numbers
largest = get_largest_numbers(nums, 2)
print(nums) # sorted numbers
print("-------------")
# List Comprehensions
'''
List comprehensions provide a concise way to create lists in Python. They allow you to generate a new list by 
applying an expression to each item in an existing iterable (such as a list, tuple, or range) and optionally filtering the items based on a condition
basic syntax
new_list = [expression for item in iterable if condition]
'''
# Traditional approach using a loop to square numbers in a list
numbers1 = [1, 2, 3, 4, 5]
squared_numbers1 = []
for num1 in numbers1:
    squared_numbers1.append(num1 ** 2)
print(squared_numbers1) 
# Equivalent list comprehension
squared_numbers1 = [num1 for num1 in numbers1]
print(squared_numbers1)   
