import socket
from thread import *
import sys

def threaded_client(conn):
    
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Desconectado.")
                break
            else:
                print(f"Recebido: {reply}")
                print(f"Enviando: {reply}")

            conn.sendall(str.encode(reply))
        
        except:
            break

    print("Conexao perdida.")
    conn.close()


def main():
    
    server = "localhost"
    port = 24000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind((server, port))
    except socket.error as e:
        str(e)

    s.listen(2)
    print("Esperando por conexao. Servidor iniciado.")

    while True:
        conn, addr = s.accept()
        print(f"Conectado com {addr}.")

        start_new_thread(threaded_client, (conn, ))
