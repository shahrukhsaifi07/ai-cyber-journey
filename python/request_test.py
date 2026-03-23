import requests

url="https://google.com"

response=requests.get(url)

print("Status Code:",response.status_code)