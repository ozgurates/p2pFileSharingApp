import time
from socket import *
import json

port = 8000

contentDict = {}
file_name = input("Enter file name to download: ")
chunknames = [file_name + '_1', file_name + '_2', file_name + '_3', file_name + '_4', file_name + '_5']

for index in range(1, 6):
    f = open('dict.txt', 'r')
    contentDict = json.loads(f.read())

    fileToSend = file_name + str(1)
    # IP = contentDict['address']
    IP = contentDict[file_name +'_' + str(index)]
    print(IP)
    fileToSend = file_name +'_'+ str(index)
    print(fileToSend)
    data = {
        "requested_content" : fileToSend
     }
    newData = json.dumps(data)
    try:
        tcpSock = socket(AF_INET, SOCK_STREAM)
        tcpSock.connect((IP, port))
        tcpSock.send(newData.encode())

        file = open(fileToSend , 'ab')

        received = tcpSock.recv(1024)

        while received:
            file.write(received)
            received = tcpSock.recv(1024)


        file.close()
        tcpSock.close()

        print(fileToSend+" is successfully downloaded.")
    except:
        for i in range (1,6):
            try:
                time.sleep(2)
                print('Trying to download ' + file_name + str(i) + ' from another peer')
                IP = contentDict[file_name + str(index)][i]
                tcpSock.connect((IP, port))
                tcpSock.send(newData.encode())
                print(data)

                file = open(fileToSend , 'ab')
                received = tcpSock.recv(100240)
                with open(chunknames[index - 1] , 'wb') as outfile:
                    outfile.write(received)

                outfile.close()
                tcpSock.close()
                time.sleep(1)
                print(fileToSend + " is successfully downloaded.")
            except:
                print('Can not be downloaded')
        break


        print(fileToSend + " cannot be downloaded")


# with open(content_name+'.png', 'w') as outfile:
try:
   with open(file_name + '.png', 'wb') as outfile:  # in your code change 'ece.png' to content_name+'.png'
    for chunk in chunknames:
        with open(chunk , 'rb') as infile:
            outfile.write(infile.read())
except:
   print("Can not be create")

