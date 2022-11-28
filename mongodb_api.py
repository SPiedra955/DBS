import requests
import json
url = "https://data.mongodb-api.com/app/data-nxnpm/endpoint/data/v1/action/find"
payload = json.dumps({
    "collection": "bikes",
    "database": "rental_bikes",
    "dataSource": "SANDBOXX",
})
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': "taIj5LjbfEgsNcnWAtCfctE9wGgPZzub4XCT9bex1nbLA9VHMhKhrsRGvbd7iE51",
}
response = requests.request("POST", url, headers=headers, data=payload)
 
print(response.text)
