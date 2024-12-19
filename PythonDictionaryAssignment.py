#!/usr/local/bin/python3
# command: python3 PythonDictionary.py

employeeList = [{"name": "John", "age": 21, "empId": 11 },
            {"name": "Mira", "age": 24, "empId": 22 },
            {"name": "Nora", "age": 25, "empId": 33 }]

# add a new field in the dictionary 
for dic in employeeList:
    dic["Active"] = "A"
    print(f"updated Dictionary is {dic}")

# print the name and their employee Ids using iteration
for dic in employeeList:
    print(f"the employee name is {dic["name"]} and respective employee id is {dic["empId"]}")

# get the max age from employeeList
max = employeeList[0]["age"]
for dic in employeeList:
    if(dic["age"] > max):
        max = dic["age"]

print(f"The maximum of an employee is {max}")

        