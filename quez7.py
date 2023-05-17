# Q7. What do you understand about mutable and immutable data types? Give examples for both showing
# this property.

x = 5
print(x)  # Output: 5

x = x + 1
print(x)  # Output: 6

# The original value of x (5) is not modified, but a new object with the value 6 is created.

numbers = [1, 2, 3, 4]
print(numbers)  # Output: [1, 2, 3, 4]

numbers.append(5)
print(numbers)  # Output: [1, 2, 3, 4, 5]

# The original list is modified by adding a new element to it.
