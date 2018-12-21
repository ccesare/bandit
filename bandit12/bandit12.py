from pwn import * # pylint: disable=unused-import
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--interactive",
                    help="open an interactive shell on host",
                    action="store_true")
args = parser.parse_args()

BANDIT = 12

with open("../bandit" + str(BANDIT - 1) + "/password", "r") as old_pass:
    pw = old_pass.read().replace("\n", "")

server = "bandit.labs.overthewire.org"
server_port = 2220
user = "bandit" + str(BANDIT)

conn = ssh(user, server, password=pw, port=server_port)

if args.interactive:
    conn.interactive()
else:
    payload = "cd `mktemp -d` && \
               cp ~/data.txt . && \
               xxd -r data.txt > unhexed.gz && \
               gunzip unhexed.gz && \
               bunzip2 unhexed > /dev/null 2>&1  && \
               mv unhexed.out unhexed.gz && \
               gunzip unhexed.gz && \
               tar -xf unhexed && \
               tar -xf data5.bin && \
               bunzip2 data6.bin > /dev/null 2>&1 && \
               tar -xf data6.bin.out && \
               mv data8.bin data8.gz && \
               gunzip data8.gz && \
               cat data8 | sed \"s/The password is //\""
    password = conn.process(payload, shell=True).recvall()

    with open("password", "w") as pass_file:
        pass_file.write(password)

    print password.replace("\n", "")
