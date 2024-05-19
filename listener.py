import sys
import socket
import time

from pex.arch.types import *
from pex.platform.types import *

from pwny.session import PwnySession


def main():
    print('Waiting for connection ...', end=' ')

    s = socket.socket()
    s.bind((sys.argv[1], int(sys.argv[2])))
    s.listen()
    c, a = s.accept()

    print(f'Connection from {a[0]}:{str(a[1])}\n')

    p = PwnySession()
    p.details['Platform'] = sys.argv[3]
    p.details['Arch'] = sys.argv[4]
    p.open(c)
    p.set_prompt('pwny %red%bold% %end')
    p.interact()


if __name__ == '__main__':
    if len(sys.argv) < 5:
        print(f'Usage: {sys.argv[0]} <host> <port> <platform> <arch>')
        sys.exit(1)

    main()
    sys.exit(0)
