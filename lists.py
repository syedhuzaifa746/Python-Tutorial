my_list = [1, 2, 3]

# Methods that modify the list in place
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

my_list.remove(2)
print(my_list)  # Output: [1, 3, 4]

my_list.sort()
print(my_list)  # Output: [1, 3, 4]

# Methods that return a new list or other values
new_list = my_list.copy()

print(new_list)  # Output: [1, 3, 4]

count_of_ones = my_list.count(1)
print(count_of_ones)  # Output: 1



# list used to store multiple values in a single variable

# food = ["Pizza", "Biryani", "Pasta", "Cold Drink"]
# print(food)

# food.append("Burger")
# food.insert(2, "New Dish")
# food.remove("New Dish")
# food.pop()  # remove the last item from the list

# # Print the updated list after removing the last item
# for x in food:
#     print(x)

# food = ["Pizza", "Biryani", "Pasta", "Cold Drink"]
# last_item = food.pop()  # Removes and returns "Cold Drink" from the list
# print("Removed item:", last_item)  # Output: Removed item: Cold Drink
# print("Updated list:", food)  # Output: Updated list: ['Pizza', 'Biryani', 'Pasta']









# food[0] = "Palao" #Pizza replace by Palao
# # print("The first food is: ", food[0])

# # list methods
# food.append("Fried Rice")  # add item at the end of the list
# print("Added Fried Rice: ", food)

# food.insert(1, "Chicken Biryani")   # insert item at a specific position
# print("Inserted Chicken Biryani at index 1: ", food)

# del food[3]    # delete an item using its index
# print("Deleted Cold Drink: ", food)

# # check if an item exists in the list
# print("Does 'Pizza' exist in the list? ", 'Pizza' in food)
# print("Does 'Sandwich' exist in the list? ", 'Sandwich' in food)

# # access items from the list (index starts from 0)
# print("\nAccessing Items From The List: ")
# for i in range(len(food)):
#     print("Item at index", i, "is: ", food[i])

"""
Output:

The first food is:  Palette
Added Fried Rice:  ['Palao', 'Biryani', 'Pasta', 'Cold Drink']
Inserted Chicken Biryani at index 1:  ['Palao', 'Chicken Biryani', 'Pasta', 'Cold Drink']
Deleted Cold Drink:  ['Palao', 'Chicken Biryani', 'Pasta']
Does 'Pizza' exist in the list?  True
Does 'Sandwich' exist in the list?  False

Accessing Items From The List:  
Item at index 0 is:  Palao
Item at index 1 is:  Chicken Biryani
Item at index 2 is:  Pasta
"""
# print(len(food))