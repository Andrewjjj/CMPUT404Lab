#!/usr/bin/env python3
import socket, time, sys
from multiprocessing import Process

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def get_remote_ip(host):
    print(f'Getting IP from {host}')
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()
    
    print(f"Ip address of {host} is {remote_ip}")
    return remote_ip

def handle_requests(proxy_end, conn):
    send_full_data = conn.recv(BUFFER_SIZE)
    print(f"Sending received data {send_full_data} to google")
    proxy_end.sendall(send_full_data)
    proxy_end.shutdown(socket.SHUT_WR)
    data = proxy_end.recv(BUFFER_SIZE)
    conn.sendall(data)
    conn.shutdown(socket.SHUT_RDWR)
    print(f"Sending received data {data} to client")

def main():
    extern_host = "www.google.com"
    port = 80
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:

        print("Starting Proxy Server")
        proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        proxy_start.bind((HOST, PORT))
        proxy_start.listen(2)

        while True:
            conn, addr = proxy_start.accept()
            print("Connected by", addr)

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                #TODO: get remote ip of google, connect proxy_end to it
                remote_ip = get_remote_ip(extern_host)
                proxy_end.connect((remote_ip, port))
                # multiprocessing:

                p = Process(target=handle_requests, args=(proxy_end, conn))
                p.daemon = True
                p.start()
                # allow multiple connection with daemon
                # target = handle_ request when creating the process

            # close the connection
            conn.close()

if __name__ == "__main__":
    main()