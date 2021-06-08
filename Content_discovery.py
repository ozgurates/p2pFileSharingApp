from socket import *
import json
import time

udpSocket = socket(AF_INET, SOCK_DGRAM)
socketPort = 5001

udpSocket.bind(('', socketPort))

new_dict = {}
x = {}

print("Listening...")

while True:
    dict, address = udpSocket.recvfrom(100240)
    data = json.loads(dict)
    for i in data["chunks"]:
        chunk_name = i
        new_dict[(chunk_name) ] = address[0]


        a = new_dict.copy()
        a.update(x)

        file = open('dict.txt', 'w')

        conDict = file.write(json.dumps(a))
        file.close()

        ip_addr = address #its equal to ip
    print(a)
    time.sleep(5)