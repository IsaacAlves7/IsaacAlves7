import requests
import datetime
import os

TOKEN = os.environ['TOKEN']
USERNAME = "prajjwal"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response= requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Test Graph",
    "unit": "Minutes",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_response.text)
date = f"{datetime.datetime.today().strftime('%Y%m%d')}"

pixel_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_post_pram = {
    "date": date,
    "quantity": input("How many minutes did you code today? ")
}
#
response = requests.post(url=pixel_post_endpoint, json=pixel_post_pram, headers=headers)
print(response.text)

# print(date)
# pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
# pixel_update_pram = {
#     "quantity": "122"
# }
# response = requests.put(url=pixel_update_endpoint, json=pixel_update_pram, headers=headers)
# print(response.text)


# pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
#
# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)