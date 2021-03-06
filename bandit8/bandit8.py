from pwn import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--interactive",
                    help="open an interactive shell on host",
                    action="store_true")
args = parser.parse_args()

BANDIT = 8

with open("../bandit" + str(BANDIT - 1) + "/password", "r") as old_pass:
    pw = old_pass.read().replace("\n", "")

server = "bandit.labs.overthewire.org"
server_port = 2220
user = "bandit" + str(BANDIT)

conn = ssh(user, server, password=pw, port=server_port)

if args.interactive:
    conn.interactive()
else:
    payload = "cat data.txt | sort -n | uniq -c | sed \"s/.*1\ /IAMTHELINE /\" | grep IAMTHELINE | sed \"s/IAMTHELINE //\""
    password = conn.process(payload, shell=True).recvall()

    with open("password", "w") as pass_file:
        pass_file.write(password)

    print password.replace("\n", "")
