import socket

# Configurações do cliente
HOST = ' ' #Inserir no espaço entre aspas simples o ip do computador de quem está rodando o servidor
PORT = 65432

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        data = s.recv(1024).decode()
        print(data)
        
        # Envia respostas (substitua pelos inputs dos jogadores)
        respostas = input("Digite suas respostas separadas por vírgula: ")
        s.sendall(respostas.encode())
        
        feedback = s.recv(1024).decode()
        print(feedback)

if __name__ == "__main__":
    start_client()
