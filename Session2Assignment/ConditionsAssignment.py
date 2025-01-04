#!/usr/local/bin/python3
# command: python3 PythonTuples.py

conditionList = [{"Name": "John",
"Age": 0,
"Income": 75000,
"Region": "ABC"
}, {"Name": "Tom",
"Age": 22,
"Income": -1,
"Region": "NAN"
}, {"Name": "Pope",
"Age": 23,
"Income": 85000,
"Region": "North America"
}]

# Mark record as invalid if age or income is 0 or less
for dic in conditionList:
    if(dic["Age"]<=0 or dic["Income"]<0):
        dic["Valid"] = "N"
    else:
        dic["Valid"] = "Y"
    print(f"the updated dic {dic}")

# High, Medium and Low income
for dic in conditionList:
    if(dic["Income"] > 100000):
        dic["Income Level"] = "High-income"
    elif(dic["Income"] > 50000 and dic["Income"] <= 100000):
         dic["Income Level"] = "Medium-income"
    else:
        dic["Income Level"] = "Low-income"
    print(dic)

# region as "North America"
for dic in conditionList:
    if(dic["Region"] == "North America"):
        print(dic)

# make 3 list for invalid, valid and region wise customer
valid_customer = list()
invalid_customer = list()
region_customer = list()

for dic in conditionList:
    if(dic["Valid"]=="Y"):
        valid_customer.append(dic)
    else:
        invalid_customer.append(dic)
    if(dic["Region"] == "North America"):
        region_customer.append(dic)

print(f"valid customer {valid_customer}")
print(f"invalid customer {invalid_customer}")
print(f"region wise {region_customer}")



