
### **SET**

myset = {1,2,3,4,"python", "data science"}
print(myset)

# Adding elements to set

myset = {1,2,3,4,"python", "data science"}
myset.add('task1')
print(myset)

myset = {1,2,3,4,"python", "data science"}
thisset = {'a','b','c','d'}
myset.update(thisset)
print(myset)

#Removing element from set

myset = {1,2,3,4,"python", "data science"}
myset.remove("python")
print(myset)