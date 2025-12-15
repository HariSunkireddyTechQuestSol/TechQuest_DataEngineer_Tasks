import requests

def get_public_ip():
    url = "https://api.ipify.org?format=json"
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        data = resp.json()
        print("Response JSON:", data)
    except requests.exceptions.RequestException as e:
        print("Error:", e)

get_public_ip()
