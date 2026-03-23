with open("logs.txt","r") as file:
    logs=file.readlines()

for log in logs:
    if "Success" in log:
        print("Successful login found:",log.strip())
        