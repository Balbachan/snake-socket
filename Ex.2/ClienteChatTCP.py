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
    port = 32173
    tamanho_buffer = 1024
    rodando = True

    # Criar o socket do cliente.
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conectar com o servidor.
    socket_cliente.connect((host, port))

    while rodando == True:

        # Escrever a mensagem.
        mensagem = input("msg >> ")

        # Checar se quer sair do programa.
        if mensagem == "QUIT":
            rodando = False
        
        # Enviar a mensagem para o servidor.
        socket_cliente.send(mensagem.encode())

        # Receber mensagem do servidor.
        msg_serv = socket_cliente.recv(tamanho_buffer).decode()
        print(f"Server: {msg_serv}")

    # Fechar a conexao.
    socket_cliente.close()

main()
