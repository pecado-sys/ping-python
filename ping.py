import socket, time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

bytesToSend = bytes(64)
countBytes = 0

host = input("Host: ")

try:
    HostIP = socket.gethostbyname(host)
    rsp = sock.connect_ex((host, 80))



    print("[*] Connect successfully")

    while True:
        try:
            sock.send(bytesToSend)
            print(f"Send 64 bytes to{host} ({HostIP})")
            
            countBytes +=64
            time.sleep(0.6)
        except KeyboardInterrupt:
            break

    sock.close()
    print("[-] Socket close")
except:
    host = "NOTFOUND"
    HostIP = "IP NOT FOUND"
    print('[x] Cant connect')

print(f"----------- Info ------------\n-> were sent {countBytes} bytes to {host} ({HostIP})")