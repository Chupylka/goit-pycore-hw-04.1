# json -> jsnotation object
from mock import get_mocked_user
import json


print(f"Name from main.py {__name__}")


filename = input("Enter filename >>>")
amount = int(input("How many fake users you want >>>"))


with open(filename, "w") as file:
    moced_users = list()
    for i in range(amount):
        moced_users.append(json.dump(get_mocked_user()))
    file.writelines(mocked_users)