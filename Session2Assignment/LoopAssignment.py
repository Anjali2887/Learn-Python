#!/usr/local/bin/python3
# command: python3 PythonTuples.py

transactions = [1200, 450, 1800, -50, 300, 2200, 1000, 500, 750]

#Calculate the total number of transactions and the total amount of transactions
totalNumberOfTransaction = len(transactions)
print(f"Total number of transactions are {totalNumberOfTransaction}")

i=1
totalAmountOfTransaction = transactions[0]
while i<totalNumberOfTransaction:
    totalAmountOfTransaction += transactions[i]
    i += 1

print(f"total Amount is {totalAmountOfTransaction}")

#Identify and print the transactions that are above $500. If a transaction is above $2000, stop processing further transactions (use break).
for tran in transactions:
    if(tran > 500):
        if(tran > 2000):
            break
        print(f"Transactions::::: {tran}")

#Skip any invalid transaction values (negative amounts) and continue processing the rest (use continue).
for tran in transactions:
    if(tran < 0):
        continue
    print(f"Positive Transactions::::{tran}")

#Use a while loop to track the number of transactions processed until a transaction greater than $1000 is found.

i = 0
transactions.sort(reverse=True)

while transactions[i]>1000 :
    i += 1

print(f"Total count is {i}") 


