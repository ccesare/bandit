from pwn import *

user = "bandit0"
pw = "bandit0"
server = "bandit.labs.overthewire.org"
#port = 2220

conn = ssh(user, server, password=pw, port=2220)

password = conn.process("cat readme", shell=True).recvall()

with open("password", "w") as pass_file:
    pass_file.write(password)

print password.replace("\n", "")

#conn.interactive()
