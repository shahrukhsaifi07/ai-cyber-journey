with open("logs.txt","r") as file:
    logs=file.readlines()
failed_attempts=0
success_attempts=0


for log in logs:
    if "Success" in log:
        print("Successful login found:",log.strip())
        success_attempts +=1
    elif "Failed" in log:
        failed_attempts +=1

print("Failed Attempts",failed_attempts)
print("Success Attempts",success_attempts)