print('hello')# **LIST**

list1 = [1,2,3.34,'Python']
print(list1)

## Adding new elements in list

#Appending new element
list2 = [2,10,'data analysis',2.34,'python']
list2.append('adding') # using append we can only add one element at a time
print(list2)

list3 = [1,2,10,11,2.34,'python']
list3.insert(1,'index') # using function index() we can add element at specific index
print(list3)

list2.extend(list3) #using function extend() we can add two list
print(list2)

## removing elements from list

thislist = [1, 2, 3,'Python', 4,'Data science', 5] #deleting element from specific index
del thislist[2]
print(thislist)

thislist =  [1, 2, 3,'Python', 4,'Data science', 5]
thislist.remove('Data science') #deleting element by there value
print(thislist)

my_list = [1, 2, 3, 4, 5]
my_list.pop() #this will always delete element from last
print(my_list)


my_list = [1, 2, 3, 4, 5]
my_list.clear() #it will clear whole list at a time
print(my_list)

 
