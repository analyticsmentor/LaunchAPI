import requests

url = "https://reactor.adobe.io/properties/<propertyID>/rules?filter[name]=CONTAINS%20<anyfilter>"

payload  = {}
headers = {
  'Accept': 'application/vnd.api+json;revision=1',
  'Content-Type': 'application/vnd.api+json',
  'Authorization': 'Bearer <token>',
  'X-Api-Key': '<key>',
  'X-Gw-Ims-Org-Id': '<orgID>@AdobeOrg'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text.encode('utf8'))

ids = []
for d in response.json()["data"]:
    ids.append(d["id"])
