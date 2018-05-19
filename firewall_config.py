import requests
import json
from tabulate import tabulate
url = "https://www.googleapis.com/oauth2/v4/token"

payload = "client_id=1051695744365-vgu5crungnhuf7vjo4b4g0lbkmibnlom.apps.googleusercontent.com&client_secret=VM2gNMb8npPuZyf321EzvMo0&grant_type=refresh_token&refresh_token=1%2FDGjpWuhkieRzMHvGatf1-wZKEwpy0CVgagzTvAHQhEc"


def credential(url,payload):
	headers = {
    	'Content-Type': "application/x-www-form-urlencoded",
    	'Accept': "application/json, text/javascript, */*",
    #'Cache-Control': "no-cache",
    #'Postman-Token': "24d10743-5923-47ef-967d-589f46832c47"
    	}

	response = requests.request("POST", url, data=payload, headers=headers)
	resp=response.json()
	#print(response.text)
	token=resp['access_token']
	return token
def listFirewall(token):
	headers = {
    	'Authorization': '{0} {1}'.format("Bearer",token) #ya29.Glu_BXGxTBJW7yemTQhnqkOoTV91MqxHgctua_iLsQfY4klVfp-VbBEvUQ-1cDWUabbXRJWJ_jpX1aPiC0zvY1cfMl4_1nd5Er_j8GiD_wC2tLOXpd63HrgdVwtq",
    #'Cache-Control': "no-cache",
    #'Postman-Token': "359d6249-38d4-4a6f-88ca-b25cb7a5817d"
    	}

	response = requests.request("GET","https://www.googleapis.com/compute/v1/projects/my-python-project-204116/global/firewalls", headers=headers)	
	resp=response.json()
	for item in resp['items']:
		print('{0}  {1}  {2}  {3}'.format(item['name'],item['direction'],item.get('allowed'),item.get('denied')))

def getFirewall(token):
	name=input("Enter the Firewall_Rule_Name:")
	headers = {
        'Authorization': '{0} {1}'.format("Bearer",token) #ya29.Glu_BXGxTBJW7yemTQhnqkOoTV91MqxHgctua_iLsQfY4klVfp-VbBEvUQ-1cDWUabbXRJWJ_jpX1a$
    #'Cache-Control': "no-cache",
    #'Postman-Token': "359d6249-38d4-4a6f-88ca-b25cb7a5817d"
        }
	response= requests.request("GET","https://www.googleapis.com/compute/v1/projects/my-python-project-204116/global/firewalls/"+name,headers=headers)
	resp=response.json()
	print('{0} {1} {2} {3}'.format(resp["name"],resp["direction"],resp.get("allowed"),resp.get("denied")))


def patchFirewall(token):
	name=input("Enter the Firewall_Rule_Name to patched:")
	headers = {
        'Authorization': '{0} {1}'.format("Bearer",token) #ya29.Glu_BXGxTBJW7yemTQhnqkOoTV91MqxHgctua_iLsQfY4klVfp-VbBEvUQ-1cDWUabbXRJWJ_jpX1a$
    #'Cache-Control': "no-cache",
    #'Postman-Token': "359d6249-38d4-4a6f-88ca-b25cb7a5817d"
        }
        response= requests.request("PATCH","https://www.googleapis.com/compute/v1/projects/my-python-project-204116/global/firewalls/"+name,headers=headers)
        resp=response.json()
        print('{0} {1} {2} {3}'.format(resp["kind"],resp["operationType"],resp["status"],resp["user"]))


Access_token=credential(url,payload)
#listFirewall(Access_token)
#getFirewall(Access_token)
patchFirewall(Access_token)
