from socket import *
import time
import os
import math
import json
socket = socket(AF_INET, SOCK_DGRAM)  # construct UDP
serverPort = 5001
socket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)  # setting UDP option to broadcast


content_name = input("Please enter which content you have: ")
address = input("Please enter ip you want to download from: ")



file_name = content_name + '.png'

c = os.path.getsize(file_name)
# print(c)
CHUNK_SIZE = math.ceil(math.ceil(c) / 5)
# print(CHUNK_SIZE)

index = 1
with open(file_name, 'rb') as infile:
    chunk = infile.read(int(CHUNK_SIZE))
    while chunk:
        chunkname = content_name +"_"+ str(index)
        print(chunkname)
        # print("chunk name is: " + chunkname + "\n")
        with open(chunkname, 'wb+') as chunk_file:
            chunk_file.write(chunk)
        index += 1
        chunk = infile.read(int(CHUNK_SIZE))
chunk_file.close()

# parsing file into 5 chunks

print(str(index - 1) + " Chunks created")
print("Starting to announce chunks...")
ip_address = gethostbyname(gethostname())

data = {
    'chunks': [content_name +"_1", content_name +"_2" , content_name +"_3", content_name +"_4" ,
                content_name +"_5"],
}

newData = json.dumps(data)

while True:
    socket.sendto(newData.encode('utf-8'), (address, serverPort))
    time.sleep(60)
