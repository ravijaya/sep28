import requests


url = 'http://127.0.0.1:5000/todo/tasks'
data = {'title': 'learn go lang'}

response = requests.post(url, json=data)
print(response.status_code)
print()
print(response.json())