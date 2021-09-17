import requests
print(f"requests version: {requests.__version__}")
print()
req_google = requests.get("https://www.google.com")
req_myfile = requests.get("https://raw.githubusercontent.com/Andrewjjj/CMPUT404Lab/main/Lab1/lab1.py")
print(req_myfile.content)