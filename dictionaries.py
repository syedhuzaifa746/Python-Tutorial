# dictionary = A changeable, unordered collection of unique key: value pairs Fast becuase they use hashtaging
# allow us to access a vlaue quickly

capitals = {
    "Pakistan": "Islamabad",
    "India": "Delhi",
    "China": "Beijing",
    "Russia": "Moscow",
}

# print(capitals["Russia"]) # Output Moscow
# print(capitals["Germany"]) # Output will be KeyError bcz this key not exist in dict

# print(capitals.get("Russia")) # Output Moscow
# print(capitals.get("Germanhy")) # Output will be "None" which is one the datataype of python

# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

# for key, value in capitals.items():
#     print(key, value)

# capitals.update({"India": "Karachi"})
# print(capitals.get("India"))

# capitals.pop("India")
# print(capitals.get("India"))

capitals.clear()
print(capitals)