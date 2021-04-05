import requests

res = requests.get("https://www.usom.gov.tr/url-list.txt", verify=False)
file = open("usom.txt", "w")
file.write(str(res.content))
file.close()
