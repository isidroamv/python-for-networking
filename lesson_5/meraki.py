import requests
import json

# Get organizations
url = "https://api.meraki.com/api/v0/organizations"
headers = { "X-Cisco-Meraki-API-Key": "9dbb33c7edc9072c0bd6b69de7edf5732d66778f", "Content-Type":"application/json"}
r = requests.get(url, headers=headers)
organizations = json.loads(r.text)
organization = organizations[0]
print("organization", organizations)

# Get operators
url = "https://api.meraki.com/api/v0/organizations/"+ str(organization["id"]) + "/admins"
headers = { "X-Cisco-Meraki-API-Key": "9dbb33c7edc9072c0bd6b69de7edf5732d66778f", "Content-Type":"application/json"}
r = requests.get(url, headers=headers)
admins = json.loads(r.text)
admin = admins[0]
print("admin", admin)

# Create Network
url = "https://api.meraki.com/api/v0/organizations/"+ str(organization["id"]) + "/admins"
headers = { "X-Cisco-Meraki-API-Key": "9dbb33c7edc9072c0bd6b69de7edf5732d66778f", "Content-Type":"application/json"}
payload = '{"name":"My etwork", "type":"wireless", "timeZone": "MX"}' 
r = requests.post(url, headers=headers, data=payload)
print("network", r.text)
