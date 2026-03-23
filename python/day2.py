correct_password="admin"
passwords=["1234","admin","password","letmein"]

for pwd in passwords:
    if pwd==correct_password:
        print("Access Granted",pwd)
        break
    else:
        print("Wrong Password",pwd)
