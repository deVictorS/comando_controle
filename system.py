import socket
import threading
import time

SERVER_IP = "10.20.10.179"
SERVER_PORT = 4444

def connect(ip, port):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip, port))
        print("Conectado ao servidor.")
        return client
    except Exception as e:
        print("Erro ao conectar:", e)
        return None

def receive_messages(client):
    """Thread que recebe mensagens do servidor."""
    try:
        while True:
            data = client.recv(1024)
            if not data:
                print("Conexão encerrada pelo servidor.")
                break
            print("\n[Servidor]:", data.decode())
    except:
        pass
    finally:
        client.close()

def main_loop(client):
    """Loop principal de envio."""
    while True:
        try:
            msg = input("> ")
            if msg.lower() in ("exit", "quit"):
                client.close()
                break

            client.send(msg.encode())
        except:
            break

if __name__ == "__main__":
    while True:
        client = connect(SERVER_IP, SERVER_PORT)
        if client:
            threading.Thread(target=receive_messages, args=(client,), daemon=True).start()
            main_loop(client)
        else:
            print("Tentando novamente em 3 segundos...")
            time.sleep(3)