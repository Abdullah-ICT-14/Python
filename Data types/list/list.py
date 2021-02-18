#List is a collection which is ordered and changeable. Allows duplicate members.

#In Python lists are written with square brackets.
this_is_list=['apple','orange','cucumber','hello','hello','how','are','you','i']
print(this_is_list)

#You access the list items by referring to the index number:
print(this_is_list[1])

#Negative indexing means beginning from the end, -1 refers to the last item, -2
#refers to the second last item etc.
print(this_is_list[-1])

#Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the
#range.

print(this_is_list[2:5])

#By leaving out the start value, the range will start at the first item:
print(this_is_list[:4])

#By leaving out the end value, the range will go on to the end of the list:
print(this_is_list[5:])

#Range of Negative Indexes
#Specify negative indexes if you want to start the search from the end of the list:

print(this_is_list[-4:-1])

#Change Item Value
#To change the value of a specific item, refer to the index number:
this_is_list[3]='ruma'
print(this_is_list)

#You can loop through the list items by using a for loop:

for x in this_is_list:
    print(x)


#Check if Item Exists
#To determine if a specified item is present in a list use the in keyword:

for apple in this_is_list:
    print('yes,apple present')

#List Length
#To determine how many items a list has, use the len() function:

print(len(this_is_list))

#Add Items
#To add an item to the end of the list, use the append() method:
this_is_list.append('lamia')
print(this_is_list)

#To add an item at the specified index, use the insert() method:
this_is_list.insert(4,'tayeba')
print(this_is_list)

this_is_list.insert(4,5)
print(this_is_list)


#Remove Item
#There are several methods to remove items from a list:

this_is_list=pop(5)
print(this_is_list)

