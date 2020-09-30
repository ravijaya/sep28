import requests


url = 'http://127.0.0.1:5000/todo/tasks/4'

response = requests.delete(url)
print(response.json())
print()
print(response.status_code)