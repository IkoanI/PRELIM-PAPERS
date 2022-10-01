from socket import socket
import sqlite3
server = socket()
server.bind(("localhost",8888))
server.listen()
newSocket, addr = server.accept()

newSocket.sendall(b"1. Highest high tide with one corresponding date and time it happened\n" +
                  b"2. Lowest low tide with one corresponding date and time it happened\n" +
                  b"3. Largest tidal range\n" +
                  b"4. Smallest tidal range")

option = newSocket.recv(1024).decode()
conn = sqlite3.connect("tide.db")
if option == '1':
    result = conn.execute("SELECT MAX(Height), Date, Time " +
                          "From Tide " +
                          "Where isHigh = 1").fetchone()
    
    message = f"{result[0]}, {result[1]}, {result[2]}"

elif option == '2':
    result = conn.execute("SELECT MIN(Height), Date, Time " +
                          "From Tide " +
                          "Where isHigh = 0").fetchone()
    
    message = f"{result[0]}, {result[1]}, {result[2]}"

else:
    tides = conn.execute("SELECT Height " +
                         "From Tide").fetchall()

    largestRange = 0
    smallestRange = 999
    for i in range(len(tides) - 1):
        range = abs(tides[i + 1][0] - tides[i][0])
        if range > largestRange:
            largestRange = round(range, 1)

        if range < smallestRange:
            smallestRange = round(range, 1)


    if option == '3':
        message = f"{largestRange}"

    else:
        message = f"{smallestRange}"

conn.close()
newSocket.sendall(message.encode())
newSocket.close()
server.close()
