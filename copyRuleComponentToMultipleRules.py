import requests
import json

ruleIDs = ['RL123','RL456','RL789','RL098','RL765','RL543']

for ruleID in ruleIDs:
    url = "https://reactor.adobe.io/properties/<propertyID>/rule_components"
    payload  = {"data": {
                    "attributes": {
                      "delegate_descriptor_id": "core::conditions::custom-code",
                      "name": "<ruleComponentName>",
                      "settings":"{"<body of the rule component>"}"
                    },
                    "relationships": {
                      "extension": {
                            "data": {
                                  "id": "EX123123",
                                  "type": "extensions"
                            }
                        },
                      "rules": {
                            "data": [{
                                    "id": ruleID,
                                    "type": "rules"
                            }]
                        }
                    },
                    "type": "rule_components"
                  }
    }
    
    payload = json.dumps(payload)
    
    headers = {
      'Accept': 'application/vnd.api+json;revision=1',
      'Content-Type': 'application/vnd.api+json',
      'Authorization': 'Bearer <token>',
      'X-Api-Key': '<key>',
      'X-Gw-Ims-Org-Id': '<orgID>@AdobeOrg'
    }
    response = requests.request("POST", url, headers=headers, data=payload)    
    print(response.text.encode('utf8'))
