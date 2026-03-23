import requests

url="https://httpbin.org/post"
passwords=["1234","12345","123456"]
correct_password="12345"
for pwd in passwords:
    print("Trying : ",pwd)

    data={
            "username":"admin",
            "password":pwd
    }
    if pwd==correct_password:
        print("Login Success:",pwd)
        break
    else:
        print("Login FAILED")
    response=requests.post(url,data=data)
    # print(response.text)
    # if "success" in response.text.lower():
    #     print("Password found:",pwd)
    #     break

# print("Tried:",pwd)
# print("Status:",response.status_code)
# print("response lenght:",len(response.text))
# print("-------")

    


# print(response.text)
