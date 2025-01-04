#!/usr/local/bin/python3
# command: python3 PythonSet.py

customer_ids = [101, 102, 103, 101, 104, 105, 102, 106]

#remove duplicate values
uniqueSet = set()
for c in customer_ids:
    uniqueSet.add(c)
print(f"the unique set is {uniqueSet}")

product_a_customers = {101, 102, 103, 104}
product_b_customers = {103, 104, 105, 106}

# intersaction
intersectionSet = product_a_customers & product_b_customers
print(f"New set is {intersectionSet}")

# symmetric difference
diffSet = product_a_customers ^ product_b_customers
print(f"New Sym set {diffSet}")

# union set
unionSet = product_a_customers | product_b_customers
print(f"New union set {unionSet}")

# remove invalid customer ids
transaction_logs = {101, 107, 103, 108, 102, 109}
valid_customers = {101, 102, 103, 104, 105, 106}

# Function to check if its valid customer
def valid(n):
    for a in valid_customers:
        if(a == n):
            return n
    
b = filter(valid, transaction_logs)
print(list(b))

region_a = {101, 102, 103, 104}
region_b = {104, 105, 106, 107}

# present in both the region
inBoth = region_a & region_b
print(f"in both {inBoth}")






