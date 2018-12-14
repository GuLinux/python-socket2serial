#!/usr/bin/env python3

import os
import pty
import socket
import select
import argparse

parser = argparse.ArgumentParser(description='Creates a virtual pty for a remote tcp/udp socket')
parser.add_argument('host', type=str)
parser.add_argument('port', type=int)
parser.add_argument('-u', '--udp', action='store_true')
args = parser.parse_args()

lhost = args.host
lport = args.port

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if args.udp else socket.SOCK_STREAM)
    s.connect((lhost, lport))
    master, slave = pty.openpty()
#    tty.setraw(master, termios.TCSANOW)
    print('PTY: Opened {} for {}:{}'.format(os.ttyname(slave), lhost, lport))
    mypoll = select.poll()
    mypoll.register(s, select.POLLIN)
    mypoll.register(master, select.POLLIN)

    try:
        while True:
            fdlist = mypoll.poll(1000)
            for fd,event in fdlist:
                data = os.read(fd, 4096)
                write_fd = s.fileno() if fd == master else master
                os.write(write_fd, data)
    finally:
        s.close()
        os.close(master)
        os.close(slave)
    
if __name__ == "__main__":
    main()
