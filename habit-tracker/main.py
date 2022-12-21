import requests
import os

USERNAME = "shnz99"
pixela_token = os.environ.get("PIXELA_TOKEN")
headers = {"X-USER-TOKEN": pixela_token}

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": pixela_token,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params) wystarczy jedno uruchomienie do stworzenia nowego usera w systemie pixela dane zawarte w user params
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)
