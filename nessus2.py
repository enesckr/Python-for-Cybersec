import requests
import subprocess as subp
import sqlite3 as sql
import datetime as dt
import socket

header = {
    "X-ApiKeys": "accessKey=b96ae201964c42ece5f0b5bbb551a251f6eabfb56e689ebd85eef63f9cd22115; "
                 "secretKey=a3fae456dd289302f11ef9458e55dac5ecb44f44fc9c9fee8872eade342322d4;"}

output = subp.check_output("dir", shell=True)
if not "host_discovery.db" in str(output):
    print("No Database")
    conn = sql.connect("host_discovery.db")
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE hosts (ip text, time text)')
    cursor.close()
conn = sql.connect("host_discovery.db")
cursor = conn.cursor()
cursor.execute('SELECT ip FROM hosts')
ip = cursor.fetchall()
ip_list = []
for i in ip:
    ip_list.append(str(i[0]))
conn.close()
url = "https://localhost:8834/scans"
response = requests.get(headers=header, url=url, verify=False)
for i in response.json()["scans"]:
    if "HD" in i["name"] and "completed" in i["status"]:
        url = "https://localhost:8834/scans/" + str(i["id"])
        response = requests.get(headers=header, url=url, verify=False)
        for j in response.json()["hosts"]:
            if not j["hostname"] in ip_list:
                print("New IP : ", j["hostname"])
                conn = sql.connect("host_discovery.db")
                cursor = conn.cursor()
                cursor.execute("INSERT INTO hosts VALUES (?,?)", (str(j["hostname"]), str(dt.datetime.now())))
                conn.close()
                soc = socket.socket()
                soc.connect(("target_ip", 7777))  # "RHOST" , port_number
                log = "New IP founded|" + str(j["hostname"])
                soc.sendall(str(log).encode())
                soc.close()
