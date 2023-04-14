import ast

from pwn import *


def main():
    r = remote("software-17.challs.olicyber.it", 13000)
    data = r.recv(1024)
    r.sendline(b"c")
    r.recvline()
    data = r.recvline()
    data = data.decode()
    #data = data[1::1]
    #print(data)
    l1 = ast.literal_eval(data)
    i = 0
    for el in l1:
        i += el
    print(i)
    r.recvline()
    print(r.recvline())
    r.sendline(str(i).encode())
    print(r.recvline())
    print(r.recvline())


    r.close()


if __name__ == "__main__":
    main()
