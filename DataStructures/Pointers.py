dict1 = {
    'value': 1
}

dict2 = {
    'value': 2
}

dict3 = {
    'value': 3
}

dict2 = dict3


if id(dict1) == id(dict2) == id(dict3):
    print("All pointing to the same address")
else:
    print('All not pointing to the same address')


print(id(dict1))
print(id(dict2))
print(id(dict3))

