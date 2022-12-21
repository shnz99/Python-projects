import requests
import os

USERNAME = "shnz99"
GRAPHNAME = "graph1"
pixela_token = os.environ.get("PIXELA_TOKEN")
headers = {"X-USER-TOKEN": pixela_token}

####################### Making account in pixela #################################################################
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": pixela_token,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params) wystarczy jedno uruchomienie do stworzenia nowego usera w systemie pixela dane zawarte w user params
# print(response.text)

########################### making graphs ########################################################################
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPHNAME,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}
# response_graph = requests.post(url=graph_endpoint, json=graph_config, headers=headers) wystarczy jeden raz uruchomić utworzenie nowego graphu
# print(response_graph.text)

########################## making updates to the graphs ###########################################################
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHNAME}"
update_config = {
    "date": "20221214",
    "quantity": "11.5",
}
response_update = requests.post(
    url=update_endpoint, json=update_config, headers=headers
)
print(response_update.text)
