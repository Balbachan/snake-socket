"""
Universidade Prebisteriana Mackenzie
Faculdade de Computacao e Informatica (FCI)
Ciência da Computação
Redes de Computadores
Prof. Bruno Rodrigues

Batalha de Snakes
Turma 05G
Alunos:
    - Laura C. Balbachan dos Santos (32173008)
    - Matheus Farias de Oliveira Matsumoto (32138271)
"""
import socket

def main():

    host = 'localhost'
    port = 32138
    tamanho_buffer = 1024
    rodando = True

    # Criacao do socket.
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Aguardar conexao do host e porta.
    servidor.bind((host, port))

    # Definir limite de conexoes.
    servidor.listen(1)
    print(f"Server listening on port {port}.")

    # Aceitar conexao.
    cliente, addr = servidor.accept()
    print(f"Connection from {addr} has been established.")

    while rodando == True:

        # Receber dados do cliente.
        data = cliente.recv(tamanho_buffer).decode()
        print(f"Client: {data}")

        # Inserir mensagem.
        msg = input("msg >> ")
        
        # Checar comando para sair.
        if msg == "QUIT":
            rodando = False

        # Mandar mensagem.
        cliente.send(msg.encode())

    servidor.close()

main()
