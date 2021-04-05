import requests
import subprocess as subp

# header --> Nessus API Key Generator
header = {
    "X-ApiKeys": "accessKey=b96ae201964c42ece5f0b5bbb551a251f6eabfb56e689ebd85eef63f9cd22115; "
                 "secretKey=a3fae456dd289302f11ef9458e55dac5ecb44f44fc9c9fee8872eade342322d4;"}
url = "https://localhost:8834/scans"
response = requests.get(headers=header, url=url, verify=False)

# We'll list Hostname,Host ID,Plugin Output in hosts from scans
for i in response.json()["scans"]:
    scan_id = i["id"]
    url = "https://localhost:8834/scans/" + str(i["id"])
    response = requests.get(headers=header, url=url, verify=False)
    print(response.json())
    for i in response.json()["hosts"]:
        try:
            IP = i["hostname"]
            host_id = i["host_id"]
            print("********----**********----**********----*********")
            print("Ip Address : "+str(IP))
            print("Host ID : "+str(host_id))
            url = "https://localhost:8834/scans/" + str(scan_id) + "/hosts/" + str(host_id) + "/plugins/11936"
            vuln = requests.get(headers=header, url=url, verify=False)
            plugin_output = vuln.json()["outputs"][0]["plugin_output"]
            print(plugin_output)
            if "Windows" in plugin_output:
                dir = subp.check_output("dir", shell=True)
                if not "windows.txt" in str(dir):
                    data = str(IP) + "\n"
                    file = open("windows.txt", "w")
                    file.write(data)
                    file.close()
                file = open("windows.txt", "r")
                IP_control = file.read()
                file.close()
                if not str(IP) in IP_control:
                    data = str(IP) + "\n"
                    file = open("windows.txt", "a")
                    file.write(data)
                    file.close()
        except:
            pass
