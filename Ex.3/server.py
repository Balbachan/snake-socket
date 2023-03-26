import socket
from thread import *
import sys

def threaded_client(conn, player):
    
    conn.send(str.encode("Conectado."))
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

# Ler a posicao da cobrinha.
def read_pos(array):


# Definir a posicao da cobrinha.
def make_pos(array):


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

    # Posicao das cobrinhas.
    posCobras = [[160, 210][200, 210]]

    currentPlayer = 0  # Contar quantos jogadores estao conectados.

    while True:
        conn, addr = s.accept()
        print(f"Conectado com {addr}.")

        start_new_thread(threaded_client, (conn, currentPlayer))
        currentPlayer += 1
