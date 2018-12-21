from pwn import *

BANDIT = 0

server = "bandit.labs.overthewire.org"
server_port = 2220
user = "bandit" + str(BANDIT)
pw = "bandit" + str(BANDIT)

conn = ssh(user, server, password=pw, port=server_port)

password = conn.process("cat readme", shell=True).recvall()

with open("password", "w") as pass_file:
    pass_file.write(password)

print password.replace("\n", "")

#conn.interactive()
