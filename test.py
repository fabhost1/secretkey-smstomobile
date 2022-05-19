import requests

url = "https://www.fast2sms.com/dev/bulkV2"

querystring = {"authorization":"FRLiPdUNbjtIylOSgw1C3JHhDAGa4me6Vfo0TXz9uW2QZKscv79UCGdFZt54yswlxuSLI2Ab6jNXp1H7","sender_id":"FSTSMS","message":"YOUR_MESSAGE_ID","variables_values":"12345|asdaswdx","route":"p","numbers":"6383540837"}

headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)