"""
What is a List
- A list is an ordered collection of items.
- pic

"""

# Python uses the square brackets ([]) to indicate a list. The following shows an empty list:
empty_list = []


# Typically, a list contains one or more items. To separate two items, you use a comma (,). For example:
todo_list = ["Learn Python List", "How to manage List elements"]
# Since a list often contains many items, it’s a good practice to name it using plural nouns e.g., numbers, colors, and shopping_carts.


# The following example defines a list of six numbers:
numbers = [1, 3, 2, 7, 9, 4]


# If you print out the list, you’ll see its representation including the square brackets. For example:
print(numbers)  # [1, 3, 2, 7, 9, 4]


# The following shows how to define a list of strings:
colors = ["red", "green", "blue"]
print(colors)  # ['red', 'green', 'blue']


# A list can contain other lists. The following example defines a list of lists:
coordinates = [[0, 0], [100, 100], [200, 200]]
print(coordinates)  # [[0, 0], [100, 100], [200, 200]]
