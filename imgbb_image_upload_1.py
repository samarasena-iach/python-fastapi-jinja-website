import base64
import requests
import os

os.environ['REQUESTS_CA_BUNDLE'] = 'C:/Users/AU256UR/Downloads/Zscaler Root CA.crt'
apiKey = 'e601a932b245c10cc0ecf3db7b177bdf'

print("imgBB API Uploader")
print("API Key: " + apiKey)
fileLocation = input("Enter file location: ")

with open(fileLocation, "rb") as file:
    url = "https://api.imgbb.com/1/upload"
    payload = {
        "key": apiKey,
        "image": base64.b64encode(file.read()),
    }
    res = requests.post(url, payload)

if res.status_code == 200:
    print("Server Response: " + str(res.status_code))
    print("Image Successfully Uploaded")
else:
    print("ERROR")
    print("Server Response: " + str(res.status_code))