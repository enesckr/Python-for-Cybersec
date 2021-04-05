from tkinter import *
import datetime


def check():
    file = open("usom.txt", "r")
    content = file.read()
    file.close()
    ip = entry1.get()
    now = datetime.datetime.now()
    if str(ip) in content:
        file = open("log.txt", "a")
        text = str(ip) + " zararli\nTarih: " + str(now) + "\n"
        file.write(text)
        file.close()
        v.set("IP zararli")
    else:
        file = open("log.txt", "a")
        text = str(ip) + " zararli değil\nTarih: " + str(now) + "\n"
        file.write(text)
        file.close()
        v.set("IP zararli değil")


app = Tk()
app.title("USOM ZARARLI IP CONTROL")
B = Button(app, text="Control", command=check)
B.place(x=50, y=50)
B.pack()
labelIP = Label(app, text="Enter IP Address:")
labelIP.place(x=50, y=80)
labelIP.pack()
entry1 = Entry(app)
entry1.place(x=50, y=90)
entry1.pack()
v = StringVar()
entry2 = Entry(app, textvariable=v)
entry2.place(x=50, y=100)
entry2.pack()
app.mainloop()
