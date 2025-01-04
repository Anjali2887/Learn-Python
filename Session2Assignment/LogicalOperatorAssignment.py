#!/usr/local/bin/python3
# command: python3 PythonTuples.py

conditionList = [{"Order_Id": 1,
"customer_name": "AB",
"total_amount": 2000,
"Status": "Completed",
"is_priority": True
}, {"Order_Id": 2,
"customer_name": "AC",
"total_amount": 500,
"Status": "Cancelled",
"is_priority": True
}, {"Order_Id": 3,
"total_amount": 5000,
"Status": "Pending",
"is_priority": False
}]

# get the records which are of higher amount and either complete or marked priority
completedOrPriorList = list()
for dic in conditionList:
    if(dic["total_amount"] > 1000 and (dic["Status"] == "Completed" or dic["is_priority"])):
        completedOrPriorList.append(dic)

print(f"the filtered record {completedOrPriorList}")


# get incomplete or cancelled records
incompleteOrCancelledList = list()
for dic in conditionList:
    if(dic["Status"] == "Pending" or dic["Status"] == "Cancelled"):
        incompleteOrCancelledList.append(dic)

print(f"the filtered record {incompleteOrCancelledList}")


#get the record where customer_name is missing
for dic in conditionList:
    if("customer_name" not in dic):
        print(dic)

