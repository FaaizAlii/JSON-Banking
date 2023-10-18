import json
import random
import time


def id_generator():
    try:
        s = True
        while s:
            s = False
            id = random.randint(1000,9999)
            with open('a.json','r') as f:
                existing_data = json.load(f)
                for i in existing_data:
                    if id == i["id"]:
                        s = True
                        break
                    else:
                        s = False
                        return id
    except:
        id = random.randint(1000,9999)
        return id


def write_data(data,filename= 'a.json'):
    with open (filename,'w') as f:
        json.dump(data,f,indent=4)

def set_data(data1):
    try:
        with open('a.json','r') as f:
            existing = json.load(f)
            existing.append(data1)
            write_data(existing)
    except:
        data_type = [data1]
        write_data(data_type)

def view_details(data):
    name = data["name"]
    fname = data["fname"]
    age = data["age"]
    id = data["id"]
    pwd = data["pwd"]
    cash = data["cash"]
    print(f"\n\nName    : {name}")
    print(f"dad name: {fname}")
    print(f"Age     : {age}")
    print(f"ID      : {id}")
    print(f"Password: {pwd}")
    print(f"cash    : {cash}")


def get_data():
    name = input("Enter Your Name: ")
    fname = input("Enter Your Father Name: ")
    age = input("Enter Your age: ")
    pwd = input("Enter new Password: ")
    cash = int(input("Enter initial cash to deposit: "))
    id = id_generator()
    all_data = {"name":name,"fname":fname,"age":age,"id":id,"pwd":pwd,"cash":cash}
    return all_data

def show_data_all():
    try:
        with open('a.json','r') as f:
            exist = json.load(f)
            for i in exist:    
                name = i["name"]
                fname = i["fname"]
                age = i["age"]
                id = i["id"]
                pwd = i["pwd"]
                cash = i["cash"]

                print(f"\nname: {name}")
                print(f"Father's name: {fname}")
                print(f"age: {age}")
                print(f"id: {id}")
                print(f"password: {pwd}")
                print(f"cash: {cash}\n\n")
                time.sleep(2)
    except:
        print("Error Happend! Try Again!")

def check_single():
    try:
        e = False
        s = True
        while s:
            id = int(input("Enter your ID: "))
            pwd = input("Enter Password: ")
            with open('a.json','r') as f:
                temp = json.load(f)
                for i in temp:
                    if id == i['id'] and pwd == i["pwd"]:
                        name = i["name"]
                        fname = i["fname"]
                        age = i["age"]
                        id = i["id"]
                        pwd = i["pwd"]
                        cash = i["cash"]

                        print("\n")
                        print(f"name         : {name}")
                        print(f"Father's name: {fname}")
                        print(f"age          : {age}")
                        print(f"id           : {id}")
                        print(f"password     : {pwd}")
                        print(f"cash         : {cash}\n\n")
                        time.sleep(5)
                        s = False
                        e = False
                        break
                    else:
                        e = True
                if e:
                    print("\nIncorrect Info! Try Again\n\n")
    except:
        print("Error happend!")

def Del_acc():
    try:
        e = False
        c = False
        s = True
        while s:
            id = int(input('enter ID: '))
            pwd = input("Enter Password: ")
            with open('a.json','r+') as f:
                temp = json.load(f)
                for i in temp:
                    if id == i["id"] and pwd == i["pwd"]:
                        temp.remove(i)
                        e = False
                        c = True
                        s = False
                        break
                    else:
                        e = True
                if e:
                    print("Wrong Info! Try Again")
                    break
                if c:
                    f.seek(0)
                    json.dump(temp,f,indent=4)
                    f.truncate()
                    print("\nAccount Deleted Successfully :)\n\n")
                    time.sleep(2)
                    
    except:
        pass
            
        
        
def Deposit():
    try:
        e = False
        c = False
        s = True
        while s:
            id = int(input("Enter your ID: "))
            pwd = input("Enter Password: ")
            amount = int(input("Enter amount to deposit: "))
            with open('a.json','r+') as f:
                temp = json.load(f)
                for i in temp:
                    if id == i['id'] and pwd == i["pwd"]:
                        
                        i["cash"] = i["cash"]+ amount
                        s = False
                        c = True
                        e = False
                        break
                    else:
                        e = True
                if e:
                    print("\nIncorrect Info. Please recheck it!\n")
                    break
                if c:
                    f.seek(0)
                    json.dump(temp,f,indent=4)
                    f.truncate()
                    print("\nDeposit Successfull ;)\n\n")
                    time.sleep(2)
    except:
        print("Error happend!")


def Withdraw():
    try:
        e = False
        c = False
        s = True
        while s:
            id = int(input("Enter your ID: "))
            pwd = input("Enter Password: ")
            amount = int(input("Enter amount to Withdraw: "))
            with open('a.json','r+') as f:
                temp = json.load(f)
                for i in temp:
                    if id == i['id'] and pwd == i["pwd"] and  amount <= i["cash"]:
                        
                        i["cash"] = i["cash"] - amount
                        s = False
                        c = True
                        e = False
                        break
                    else:
                        e = True
                if e:
                    print("\nIncorrect Info. Please recheck it!\n")
                    break
                if c:
                    f.seek(0)
                    json.dump(temp,f,indent=4)
                    f.truncate()
                    print("\nWithdraw Successfull ;)\n\n")
                    time.sleep(2)
    except:
        print("Error happend!")


def Transfer():
    try:
        e = False
        c = False
        s = True
        while s:
            id = int(input("\nEnter your ID: "))
            pwd = input("Enter Password: ")
            amount = int(input("Enter amount to To Transfer: "))
            rec_id = int(input("enter Receiver ID: "))
            with open('a.json','r+') as f:
                temp = json.load(f)
                for i in temp:
                    if id == i['id'] and pwd == i["pwd"] and amount <= i["cash"]:
                        
                        i["cash"] = i["cash"] - amount
                        e = False
                        break
                    else:
                        e = True
                if e:
                    print("\nIncorrect Info. Please recheck it!\n")
                    break
                f.seek(0)
                for i in temp:
                    if rec_id == i["id"]:
                        i["cash"] = i["cash"] + amount
                        s = False
                        c = True
                        e = False
                        break
                if c:
                    f.seek(0)
                    json.dump(temp,f,indent=4)
                    f.truncate()
                    print("\nTransfer  Successfull ;)\n\n")
                    f.seek(0)
                    time.sleep(2)
                    f.close()
    except:
        print("Error happend!")


def menu():
    print("***BANKING SYSTEM USING JSON***")
    print("1 - create Account")
    print("2 - Delete Account")
    print("3 - Deposit Cash")
    print("4 - Withdraw Cash")
    print("5 - Transfer Money")
    print("6 - view all users data")
    print("7 - view single user data")
    print("0 - Exit!")

def choice():
    ch = input("Choose: ")
    return ch

if __name__ == '__main__':
    while True:
        menu()
        inp = choice()
        if inp == '1':
            #Create Account
            data = get_data()
            set_data(data)
            view_details(data)
            print("\nAccount Created Successfully!\n\n")
            time.sleep(5)
        elif inp == '2':
            #delete account
            Del_acc()
        elif inp == '3':
            #Deposit
            Deposit()
        elif inp == '4':
            # Withdraw
            Withdraw()
        elif inp == '5':
            # Transfer
            Transfer()
        elif inp == '6':
            # check all users data
            show_data_all()
        elif inp == '7':
            # check single user data
            check_single()
        elif inp == '0':
            break
        else:
            print("wrong Choice!! Please Choose carefully!!")