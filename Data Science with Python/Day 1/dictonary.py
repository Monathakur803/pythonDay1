### **DICTONARY:**

dictonary = {
    'name':'Python',
    'Class':'Day1',
    'task': 1
}
print(dictonary)

## Adding element in dictonary

dictonary = {
    'name':'Python',
    'Class':'Day1',
    'task': 1
}
dictonary['id'] = 123
print(dictonary)


dictonary = {
    'name':'Python',
    'Class':'Day1',
    'task': 1
}
dictonary.pop('task')
print(dictonary)

dictonary = {
    'name':'Python',
    'Class':'Day1',
    'task': 1
}
dictonary.popitem() #it will delet last element
print(dictonary)

dictonary = {
    'name':'Python',
    'Class':'Day1',
    'task': 1
}
del dictonary['task']
print(dictonary)

dictonary = {
    'name':'Python',
    'Class':'Day1',
    'task': 1
}

dictonary.clear() #it will delet last element
print(dictonary)

