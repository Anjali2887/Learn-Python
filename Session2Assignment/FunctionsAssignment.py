#!/usr/local/bin/python3
# command: python3 PythonTuples.py

orders = [
    {"order_id": 1, "customer_id": 101, "order_amount": 500, "order_date": "2024-12-01", "order_status": "completed"},
    {"order_id": 2, "customer_id": 102, "order_amount": 1500, "order_date": "2024-12-02", "order_status": "completed"},
    {"order_id": 3, "customer_id": 103, "order_amount": 200, "order_date": "2024-12-03", "order_status": "cancelled"},
    {"order_id": 4, "customer_id": 104, "order_amount": 2000, "order_date": "2024-12-04", "order_status": "completed"},
    {"order_id": 5, "customer_id": 105, "order_amount": 750, "order_date": "2024-12-05", "order_status": "pending"}
]


# Write a function to filter out orders that have an order_amount greater than a given threshold.
filteredOrder = list()
def filter(order,threshold=600):
    if(order["order_amount"] > threshold):
        filteredOrder.append(order)
    
for order in orders:
    filter(order)

print(filteredOrder)

#Write a function to categorize orders based on their amount:
#.If order_amount > 1000, categorize as "High Value".
# .If order_amount ≤ 1000, categorize as "Standard Value".
categorizeOrdersList = list()
def categorizeOrders(order,threshold=1000):
    if(order["order_amount"] > threshold):
        order["category"] = "High Value"
        categorizeOrdersList.append(order)
    elif(order["order_amount"] <= threshold):
        order["category"] = "Standard Value"
        categorizeOrdersList.append(order)
    
for order in orders:
    categorizeOrders(order)

print(categorizeOrdersList)

#Write a function to return the total revenue from completed orders
i = 0

def getTotalRevenue(i):
    for order in orders:
        if(order["order_status"] == "completed"):
            i += order["order_amount"]
    print(f"total revenue is {i}")

getTotalRevenue(i)
