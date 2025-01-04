#!/usr/local/bin/python3
# command: python3 PythonTuples.py

eComTuple = ("T001", "Alice Smith", "Laptop", 1, 1500.00)

# Access transaction id and total price
print(f"Transaction Id is {eComTuple[0]} and total price is {eComTuple[4]}")

# Extract customer name and product purchased
print(f"Customer name and product purchased are {eComTuple[1:3]}")

# iterate through all the fields
for a in eComTuple:
    print(a)

# discount price
tupleList = list(eComTuple)
tupleList[4] = tupleList[4] - (tupleList[4]* 0.1)
eComTuple = tuple(tupleList)
print(eComTuple)


