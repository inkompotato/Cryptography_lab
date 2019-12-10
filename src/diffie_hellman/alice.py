from src.diffie_hellman.client import Client
import socket


class Alice (Client):

    def __init__(self):
        super().__init__()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            conn, addr = s.accept()

            with conn:
                while True:
                    data_received = conn.recv(1024)
                    if not data_received:
                        break
                    elif self.common_secret == "":
                        # received key
                        conn.sendall(self.get_key())
                        self.common_secret = self.calculate_common_secret(int(data_received.decode('utf-8')))
                    else:
                        self.incoming_data(data_received, conn)


Alice()
