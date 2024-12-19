#!/usr/local/bin/python3
# command: python3 PythonList.py

#simulate list for given user Ids
print("Welcome to the User Id List simulation.")
user_id1 = int(input("Please provide 1st user Id"))
user_id2 = int(input("Please provide 2nd user Id"))
user_id3 = int(input("Please provide 3rd user Id"))
userList = [user_id1, user_id2, user_id3]
print(f"The complete user id list is {userList}")
userChoice = int(input("Please choose option 1 - for adding data into list/n option 2 for removing data from list/n option 3 for sorting list"))
if userChoice == 1:
    userNumberAdd = input("Please provide new user id to add in the list")
    userList.append(userNumberAdd)
    print(f"The new updated list is {userList} and new length of the list is {len(userList)}")
elif userChoice == 2:
    userNumberRemove = input("Please provide a user id to remove from the list")
    if userNumberRemove in userList:
        userList.remove(userNumberRemove)
        print(f"The new updated list is {userList} and new length of the list is {len(userList)}")
    else:
        print("Given number is not present in the list")
else:
    print(f"The sorted list is {userList.sort()}")        
