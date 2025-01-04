#!/usr/local/bin/python3
# command: python3 PythonDictionary.py

employeeDic = {"Employee ID": "E001",
"Name": "John Doe",
"Department": "Engineering",
"Salary": 75000,
"Skills": ["Python", "SQL", "Data Engineering"]
}

# add a new field in the dictionary 
employeeDic["Location"] = "New York"
print(f"updated Dictionary is {employeeDic}")

# update the Salary
employeeDic["Salary"] = 80000

# Print employee's skills
print(employeeDic["Skills"])

# Add new skill
skillList = employeeDic["Skills"]
skillList.append("AWS")
employeeDic["Skills"] = skillList
print(employeeDic["Skills"])

# Calculate total number of keys
keyList = employeeDic.keys()
print(f"Total number of keys are {len(keyList)}")

# remove the key from dict
employeeDic.pop("Location", None)
print(employeeDic)

# print all keys and values using loop
for keys, values in employeeDic.items():
    print(f"key {keys} and value  {values}") 

        