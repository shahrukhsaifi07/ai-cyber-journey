with open("password.txt","r") as file:
    passwords=file.readlines()

for pwd in passwords:
    print(pwd.strip())