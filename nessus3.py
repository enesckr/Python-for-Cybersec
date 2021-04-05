import requests
import subprocess
import datetime
import sqlite3 as sql

output = subprocess.check_output("dir", shell=True)
if not "port.db" in str(output):
    conn = sql.connect("port.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE ports (port text, ip text, time text)")
    cursor.close()

header = {
    "X-ApiKeys": "accessKey=b96ae201964c42ece5f0b5bbb551a251f6eabfb56e689ebd85eef63f9cd22115; "
                 "secretKey=a3fae456dd289302f11ef9458e55dac5ecb44f44fc9c9fee8872eade342322d4;"}
url = "https://localhost:8834/scans"
res = requests.get(headers=header, url=url, verify=False)
for i in res.json()["scans"]:
    scan_id = i["id"]
    url = "https://localhost:8834/scans/" + str(scan_id)
    scan = requests.get(headers=header, url=url, verify=False)
    for j in scan.json()["hosts"]:
        try:
            host_id = j["host_id"]
            # 11219 plugin shows open ports
            url = "https://localhost:8834/scans/" + str(scan_id) + "/hosts/" + str(host_id) + "/plugins/11219"
            IP = requests.get(headers=header, url=url, verify=False)
            for k in IP.json()["outputs"]:
                port = list(k["ports"].keys())[0]
                IP = j["hostname"]
                conn = sql.connect("port.db")
                cursor = conn.cursor()
                output = cursor.execute(" select * from ports where port=? and ip=?", (port, IP))
                port_count = len(output.fetchall())
                conn.close()
                if port_count < 1:
                    print("New port: ", port, " IP: ", IP)
                    conn = sql.connect("port.db")
                    cursor = conn.cursor()
                    cursor.execute("insert into ports values (?,?,?)", (port, IP, str(datetime.datetime.now())))
                    conn.commit()
                    conn.close()
        except:
            pass
