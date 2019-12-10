from src.diffie_hellman.client import Client
import socket


class Bob (Client):

    def __init__(self):
        super().__init__()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
            conn.connect((self.host, self.port+1))
            conn.sendall(self.get_key())
            while True:
                data_received = conn.recv(1024)
                if not data_received:
                    break
                else:
                    # received data
                    self.incoming_data(data_received, conn)


Bob()
