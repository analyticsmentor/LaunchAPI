import requests

url = "https://reactor.adobe.io/rules/<ruleID>/rule_components?filter[name]=CONTAINS%20<filter>"

payload  = {}
headers = {
  'Accept': 'application/vnd.api+json;revision=1',
  'Content-Type': 'application/vnd.api+json',
  'Authorization': 'Bearer <token>',
  'X-Api-Key': '<key>',
  'X-Gw-Ims-Org-Id': '<orgID>@AdobeOrg'
}

response2 = requests.request("GET", url, headers=headers, data = payload)
print(response2.text.encode('utf8'))
