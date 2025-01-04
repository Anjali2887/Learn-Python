#!/usr/local/bin/python3
# command: python3 PythonList.py

#simulate list for given user Ids
inputList = [150, 200, 300, 400, 250]

# Adding a new item in the list
addList = lambda givenList, y : givenList.append(y)
addList(inputList, 500)
print(f"the updated list is {inputList}")

#removing the least item from the list
inputList.sort()
inputList.pop(0)
print(f"the updated list is {inputList}")

#sorting in descending order
inputList.sort(reverse=True)
print(f"the sorted list is {inputList}")

#Calculate total sales
print(sum(inputList))

#Find and calculate average sales
print(sum(inputList)/len(inputList))

#Slice and print the 1st 3 sales amount
print(inputList[0:3])

