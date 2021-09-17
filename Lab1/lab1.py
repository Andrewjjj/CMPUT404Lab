import requests
print(f"requests version: {requests.__version__}")
print()
req_google = requests.get("https://www.google.com")
print(req_google.content)