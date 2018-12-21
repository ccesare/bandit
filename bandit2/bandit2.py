from pwn import *

BANDIT = 2

with open("../bandit" + str(BANDIT - 1) + "/password", "r") as old_pass:
    pw = old_pass.read().replace("\n", "")

server = "bandit.labs.overthewire.org"
server_port = 2220
user = "bandit" + str(BANDIT)

conn = ssh(user, server, password=pw, port=server_port)

#conn.interactive()

#password = ""
password = conn.process("cat ./spaces\ in\ this\ filename", shell=True).recvall()

with open("password", "w") as pass_file:
    pass_file.write(password)

print password.replace("\n", "")