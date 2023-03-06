import requests

url = 'https://userhashcodeserver.uk.r.appspot.com/hashCodeServer?'

payload = {
    "nome": "FulanodeTal",
    "email": "FulanodeTal@gmail.com",
    "cpf": "264.258.660-04"
}

response = requests.post(url, params=payload)

print(response.json())
