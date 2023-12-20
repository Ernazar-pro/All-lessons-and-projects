import requests

api_url  = 'http://localhost:8000/api/products'
response = requests.get(api_url)
data = response.json()
print(data)
