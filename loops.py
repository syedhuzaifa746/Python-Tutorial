# 1) While Loop

# name = ""
# while len(name) == 0:
#     name = input("Enter Your Good Name! ")
# print("Hello, {}".format(name))

# Or
# name = None
# while not name:
#     name = input("Enter Your Good Name! ")
# print("Hello, {}".format(name))

# count = 0
# while count < 5:
#     print(count)
#     count += 1

# start = 1
# end = 5
# while start <= end:
#     print(start)
#     start += 1

# Iterating over items in a list:
# my_list = [1, 2, 3, 4, 5]
# index = 0
# while index < len(my_list):
#     print(my_list[index])
#     index += 1

# user_input = ""
# while user_input.lower() != "quit":
#     user_input = input("Enter a word (type 'quit' to exit): ")
#     print("You entered:", user_input)

# start_number = 1
# user_number = int(input("Enter any number: "))

# print("Entered number:", user_number)
# print("------------------------")

# while start_number <= user_number:
#     print(start_number)
#     if start_number % 2 == 0:
#         print(start_number, "is even")
#     else:
#         print(start_number, "is odd")
#     start_number += 1

# 2) for loop
# for i in range(10):
#     print(i+1)

# Iterating over elements in a list:
# fruits = ["apple", "banana", "orange", "grape", "pineapple"]
# for fruit in fruits:
#     print(fruit)

# Iterating over characters in a string:
# word = "hello world"
# for char in word:
#     print(char)

# Iterating over key-value pairs in a dictionary:
# person = {"name": "John", "age": 30, "city": "New York"}
# for key, value in person.items():
#     print(key, ":", value)

# import time
# for seconds in range(10, 0, -1):
#     print(seconds)
#     time.sleep(1)
# print("Happy New Year!")

# rows = int(input("Enter the number of rows: "))
# columns = int(input("Enter the number of columns: "))
# symbol = input("Enter the symbol to print: ")

# print("Pattern:")
# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end=" ")
#     print()  # Move to the next line after printing all columns

