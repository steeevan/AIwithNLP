import requests

url = "https://ntrs.nasa.gov/api/citations/search"

payload={}
headers = {
  'Cookie': 'connect.sid=s%3A-ILqguJI3nqvrUm9KJXwwDcZT77Uc_yR.JfZZYXB%2BOxkUj4gp4W06LZNf52IF1jaPiH9z4eMJKWc'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
