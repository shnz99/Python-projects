import requests
from datetime import datetime
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

########################## making new data in the graphs ###########################################################
add_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHNAME}"

today = datetime.now()

add_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "11.5",
}
# response_add = requests.post(url=add_endpoint, json=add_config, headers=headers)
# print(response_add.text)

########################## making updates to the graphs ###########################################################
date_to_update = "20221208"
update_endpoint = f"{add_endpoint}/{date_to_update}"

update_config = {
    "quantity": "7",
}
# response_update = requests.post(
#     url=update_endpoint, json=update_config, headers=headers
# )
# print(response_update.text)
########################## making deletes to the graphs ###########################################################
delete_endpoint = f"{add_endpoint}/{date_to_update}"
response_delete = requests.delete(url=delete_endpoint, headers=headers)
print(response_delete.text)
