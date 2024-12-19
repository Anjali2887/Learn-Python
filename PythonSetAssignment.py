#!/usr/local/bin/python3
# command: python3 PythonSet.py

my_list = [{"name":"a1", "product":"iPad", "price": 12345},
        {"name":"a2", "product":"iPad1", "price": 2345},
        {"name":"a1", "product":"iPad", "price": 12345}]

#cleaning data by removing duplicates with set 

new_set = set(my_list)

print(new_set)