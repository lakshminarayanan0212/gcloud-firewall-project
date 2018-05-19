import requests
import json
from tabulate import tabulate
url = "https://www.googleapis.com/oauth2/v4/token"

payload = "client_id=1051695744365-vgu5crungnhuf7vjo4b4g0lbkmibnlom.apps.googleusercontent.com&client_secret=VM2gNMb8npPuZyf321EzvMo0&grant_type=refresh_token&refresh_token=1%2FDGjpWuhkieRzMHvGatf1-wZKEwpy0CVgagzTvAHQhEc"

headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'Accept': "application/json, text/javascript, */*",
    #'Cache-Control': "no-cache",
    #'Postman-Token': "24d10743-5923-47ef-967d-589f46832c47"
    }

response = requests.request("POST", url, data=payload, headers=headers)
resp=response.json()
print(response.text)

headers = {
    'Authorization': '{0} {1}'.format("Bearer",resp['access_token']) #ya29.Glu_BXGxTBJW7yemTQhnqkOoTV91MqxHgctua_iLsQfY4klVfp-VbBEvUQ-1cDWUabbXRJWJ_jpX1aPiC0zvY1cfMl4_1nd5Er_j8GiD_wC2tLOXpd63HrgdVwtq",
    #'Cache-Control': "no-cache",
    #'Postman-Token': "359d6249-38d4-4a6f-88ca-b25cb7a5817d"
    }

response = requests.request("GET","https://www.googleapis.com/compute/v1/projects/my-python-project-204116/global/firewalls", headers=headers)
resp=response.json()
list=[]
i=0
for item in resp['items']:
	list.append(item["name"]),list.append(item["direction"])


print(tabulate(list,headers=['name','direction'],tablefmt="rst"))
