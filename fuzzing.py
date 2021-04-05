import requests

file = open("fuzzing.txt", "r")
content = file.read()
file.close()
# header of searching site
PHPSESSID = ""  # Type the PHPSESSID
targetURL = ""  # Type the target url
header = {"Cookie": "PHPSESSID={}".format(PHPSESSID)}
for i in content.split("\n"):
    print(i)
    # url of searching site
    url = "{}".format(targetURL) + str(i)
    response = requests.get(url=url, headers=header)
    if "200" in str(response.status_code):
        print("There is a File or Directory:", i)
    else:
        print("There is not File or Directory:", i)
