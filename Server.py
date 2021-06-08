from socket import *
import json
import datetime

port = 8000
serverSock = socket(AF_INET, SOCK_STREAM)

serverSock.bind(('', port))

serverSock.listen(5)

print("Server listening...")
while True:
    conn, address = serverSock.accept()
    received = conn.recv(1024)
    newData = json.loads(received)


    chunk = newData['requested_content']
    print(chunk)

    with open(chunk  , 'rb') as f:
        data = f.read(100240)
        conn.sendall(data)

    with open("downloadlog.txt", "a") as downloadLog:  # Writing download log into txt file.
        currDate = datetime.datetime.now()
        stringToWrite = f"{address} downloaded {chunk}" + " at " + currDate.strftime("%Y-%m-%d %H:%M:%S")
        downloadLog.write(stringToWrite)
    conn.close()

