#!/usr/local/bin/python3
# command: python3 PythonTuples.py

tuple1 = (1,2,3)
tuple2 = (4,5,6)

# adding two tuples
tuple3 = tuple1 + tuple2

print(f"new tuple is {tuple3}")

# comparision in tuples
print(tuple1 > tuple2)

print(tuple1 == tuple2)

print(tuple1 < tuple2)

#tuples used for configurations
dbConfig = ("db_URL", "username", "password")

for data in dbConfig:
    print(f"data config is {data}")




