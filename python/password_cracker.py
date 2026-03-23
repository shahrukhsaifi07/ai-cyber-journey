correct_password="admin"

with open("password.txt","r") as file:
    passwords=file.readlines()

attempts = 0

for pwd in passwords:
    pwd=pwd.strip()
    attempts+=1

    print("Trying:",pwd)
    if pwd==correct_password:
        print("Password Found",pwd)
        print("Total Attempts:",attempts)
        break
    else:
        print("Failed")

print("Finished Checking")