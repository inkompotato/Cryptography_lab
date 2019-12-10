from src.diffie_hellman.client import Client
from Crypto.Cipher import AES
import socket
import threading


class Eve (Client):

    def __init__(self):
        super().__init__()

        t1 = threading.Thread(target=self.connect_alice)
        t1.start()

        t2 = threading.Thread(target=self.connect_bob)
        t2.start()

        self.common_secret = []
        self.connections = []

    def connect_alice(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn_alice:
            conn_alice.connect((self.host, self.port))
            conn_alice.sendall(self.get_key())

            while True:
                data_received = conn_alice.recv(1024)
                if not data_received:
                    break
                else:
                    # received data
                    self.incoming_data(data_received, conn_alice)

    def connect_bob(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port+1))
            s.listen()
            conn_bob, addr = s.accept()

            with conn_bob:
                while True:
                    data_received = conn_bob.recv(1024)
                    if not data_received:
                        break
                    else:
                        self.incoming_data(data_received, conn_bob)

    def incoming_data(self, data, conn):
        if len(self.common_secret) == 0:
            # incoming data is the key of Bob
            self.common_secret.append(self.calculate_common_secret(int(data.decode('utf-8'))))
            self.connections.append(conn)
        elif len(self.common_secret) == 1:
            self.common_secret.append(self.calculate_common_secret(int(data.decode('utf-8'))))
            self.connections.append(conn)
            conn.sendall(self.get_key())
        else:
            # we have received encrypted data
            plain_text = self.decrypt_data_mim(data, conn)
            print(plain_text)
            # reply
            if self.connections[0] == conn:
                self.send_data_mim(plain_text, self.connections[1])
            else:
                self.send_data_mim(plain_text, self.connections[0])

    def send_data_mim(self, plain_text, conn):
        while len(plain_text) % 16 != 0:
            plain_text += " "
        conn.sendall(self.encrypt_data_mim(plain_text, conn))

    def encrypt_data_mim(self, data: str, destination):
        if destination == self.connections[0]:
            cipher = AES.new(bytearray.fromhex(self.common_secret[0]), AES.MODE_ECB)

            message_string_hex = data.encode("ascii").hex()
            cipher_text = cipher.encrypt(bytearray.fromhex(message_string_hex))

            return bytearray(cipher_text)
        else:
            cipher = AES.new(bytearray.fromhex(self.common_secret[1]), AES.MODE_ECB)

            message_string_hex = data.encode("ascii").hex()
            cipher_text = cipher.encrypt(bytearray.fromhex(message_string_hex))

            return bytearray(cipher_text)

    def decrypt_data_mim(self, data: bytes, source):
        if source == self.connections[0]:
            cipher = AES.new(bytearray.fromhex(self.common_secret[0]), AES.MODE_ECB)

            cipher_text_bytearray = bytearray(data)
            return str(cipher.decrypt(cipher_text_bytearray), "ascii")
        else:
            cipher = AES.new(bytearray.fromhex(self.common_secret[1]), AES.MODE_ECB)

            cipher_text_bytearray = bytearray(data)
            return str(cipher.decrypt(cipher_text_bytearray), "ascii")


Eve()
