import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect("192.168.1.5",username="msfadmin",password="msfadmin")
stdin, stdout, stderr = ssh.exec_command("cat /etc/passwd")
for i in (stdout.read().decode("ascii").split("\n")):
    try:
        if 0 == int((str(i)).split(":")[2]):
            print("user who uid equals 0 :",str(i).split(":")[0])
    except:
        pass