import requests

def extract_keys():
    url = "https://jsonplaceholder.typicode.com/users/1"

    response = requests.get(url)
    data = response.json()

    # Extract keys
    user_id = data.get("id")
    user_name = data.get("name")
    user_email = data.get("email")

    print("User ID:", user_id)
    print("User Name:", user_name)
    print("Email:", user_email)

extract_keys()
