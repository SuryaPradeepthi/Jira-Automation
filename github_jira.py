import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask

app=Flask(__name__)

@app.route("/createJIRA",methods=['POST'])
def createJIRA():
    
    url = "https://chakkasuryapradeepthi-1722992188917.atlassian.net/rest/api/3/issue"
    API_Token="ATATT3xFfGF0FpWqsJVy5vi6kW8yzooXPLL5FrDGuqvvE0KIXn_7KgkWgNGJUBAg44DRUKT-Wqt4nyUj_3YmzpPvVzto_u4kG7dNf82HOKKOLS3HS128WucwUNEtVgKu0cHtZRrv-Ix2YQ6uZWYeiQZ4-ekA2vxKnu17CrLlUEtmu9QabKmGWxc=074A22E8"

    auth = HTTPBasicAuth("chakkasuryapradeepthi@gmail.com",API_Token)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
    "description": {
        "content": [
            {
            "content": [
                {
                "text": "My first jira ticket",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },
        
       "issuetype": {
        "id": "10007"
        },
        
        "project": {
        "key": "DEEP"
        },
        
        
        "summary": "First Jira ticket",
        
        
    },
    "update": {}
    } )

    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))


app.run('0.0.0.0',port=5000)