import json
import random
import string
from pathlib import Path



class Bank:
    database = 'Bank Management System\data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database,'r') as fs:
                data = json.loads(fs.read())
        else:
            print("No such file Exists")
    except Exception as err:
        print(f"An exception occured as{err}")

    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountGenerate(cls):
        alpha = random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits,k=3)
        splchars = random.choices("!@#$%^&*",k=1)
        id = alpha + num + splchars
        random.shuffle(id)
        return "".join(id)



    def CreateAccount(self):
        info = {
            "name": input("Tell your Name :-"),
            "age" : int(input("Tell your age:-")),
            "email":input("What is your email:-"),
            "pin":int(input("Tell your 4 digit PIN:-")),
            "AccountNo.": Bank.__accountGenerate(),
            "Balance":0
        }
        if info['age'] <18 or len(str(info['pin'])) != 4:
            print("Sorry You cannot Create your account")
        else:
            print("Account has been Created Successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note down your Account Number")

            Bank.data.append(info)
            Bank.__update()

    def DepositMoney(self):
        accnumber = input("Please tell your Account Number:-")
        pin = int(input("Please tell your PIN aswell:-"))

        userdata = [i for i in Bank.data if i['AccountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("Sorry No DATA FOUND")
        else:
            amount = int(input("How much you want to deposit:-"))
            if amount > 10000 or amount < 0:
                print("Sorry the amount is too much you can deposite below 10000")
            else:
                userdata[0]['Balance'] += amount
                Bank.__update()
                print("Amount Deposited Successfully !")
    
    def WithdrawMoney(self):
        accnumber = input("Please tell your Account Number:-")
        pin = int(input("Please tell your PIN aswell:-"))

        userdata = [i for i in Bank.data if i['AccountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("Sorry No DATA FOUND")
        else:
            amount = int(input("How much you want to Withdraw:-"))
            if userdata[0]['Balance'] < amount:
                print("Sorry you don't have that much money")
                
            else:
                userdata[0]['Balance'] -= amount
                Bank.__update()
                print("Amount Withdrew Successfully !")

    def ShowDetails(self):
        accnumber = input("Please tell your Account Number:-")
        pin = int(input("Please tell your PIN aswell:-"))

        userdata = [i for i in Bank.data if i['AccountNo.'] == accnumber and i['pin'] == pin]
        print("Your information are \n\n")

        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")


    def UpdateDetails(self):
        accnumber = input("please tell your account number ")
        pin = int(input("please tell your pin aswell "))

        userdata = [i for i in Bank.data if i['AccountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("no such user found ")
        
        else:
            print("you cannot change the age, account number, balance")

            print("Fill the details for change or leave it empty if no change")

            newdata = {
                "name": input("please tell new name or press enter : "),
                "email":input("please tell your new Email or press enter to skip :"),
                "pin": input("enter new Pin or press enter to skip: ")
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]['name']
            if newdata["email"] == "":
                newdata["email"] = userdata[0]['email']
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]['pin']
            
            newdata['age'] = userdata[0]['age']

            newdata['AccountNo.'] = userdata[0]['AccountNo.']
            newdata['Balance'] = userdata[0]['Balance']
            
            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])
            

            for i in newdata:
                 if newdata[i] == userdata[0][i]:
                     continue
                 else:
                     userdata[0][i] = newdata[i]

            Bank.__update()
            print("details updated successfully")

            
    def Delete(self):
        accnumber = input("please tell your account number ")
        pin = int(input("please tell your pin aswell "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("sorry no such data exist ")
        else:
            check = input("press y if you actually want to delete the account or press n")
            if check == 'n' or check == "N":
                print("bypassed")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("account deleted successfully ")
                Bank.__update()


user = Bank()
print("Press 1 to creating an Account")
print("Press 2 for Depositing the Money")
print("Press 3 for Withdrawing the Money")
print("Press 4 for Details")
print("Press 5 for Updating the Details")
print("Press 6 for Deleting your Account")


check = int(input("Tell your Response :-"))

if check == 1:
    user.CreateAccount()

if check == 2:
    user.DepositMoney()

if check == 3:
    user.WithdrawMoney()

if check == 4:
    user.ShowDetails()

if check == 5:
    user.UpdateDetails()

if check == 6:
    user.Delete()
