from pwn import *

BANDIT = 1

with open("../bandit" + str(BANDIT - 1) + "/password", "r") as old_pass:
    pw = old_pass.read().replace("\n", "")

user = "bandit" + str(BANDIT)
server = "bandit.labs.overthewire.org"
#port = 2220

conn = ssh(user, server, password=pw, port=2220)

#conn.interactive()

password = conn.process("cat ./-", shell=True).recvall()

with open("password", "w") as pass_file:
    pass_file.write(password)

print password.replace("\n", "")
