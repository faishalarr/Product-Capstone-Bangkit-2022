import requests

url = "https://finaltesting-bv3hqm2s3a-et.a.run.app/"
# url = "http://localhost:5000/"

resp = requests.post(url, data ={"chat": "jokes"})

print(resp.json())