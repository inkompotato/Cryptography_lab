from Crypto.Util import number
from Crypto.Cipher import AES


class Client:

    def __init__(self):
        self.p = 99233
        self.g = 99132
        self.host = '127.0.0.1'
        self.port = 65432
        self.private_key = number.getRandomInteger(self.p - 1)
        self.common_secret = ""

    def incoming_data(self, data, conn):
        if self.common_secret == "":
            # incoming data is the key of Bob
            self.common_secret = self.calculate_common_secret(int(data.decode('ascii')))
            self.send_data(conn)
        else:
            # we have received encrypted data
            plain_text = self.decrypt_data(data)
            print(f"< {plain_text}")
            # reply
            self.send_data(conn)

    def send_data(self, conn):
        plain_text = input(">")
        while len(plain_text) % 16 != 0:
            plain_text += " "

        conn.sendall(self.encrypt_data(plain_text))

    def calculate_common_secret(self, other_key):
        k = str(pow(other_key, self.private_key, self.p))
        print(f"{self.__class__.__name__} calculated the common secret as : {k}")
        while len(k) % 16 != 0:
            k += " "
        return k.encode("ascii").hex()

    def get_key(self):
        key = pow(self.g, self.private_key, self.p)
        print(f"{self.__class__.__name__}'s key: {key}")
        return bytearray(str(key), "ascii")

    def encrypt_data(self, data: str):
        cipher = AES.new(bytearray.fromhex(self.common_secret), AES.MODE_ECB)

        message_string_hex = data.encode("ascii").hex()
        cipher_text = cipher.encrypt(bytearray.fromhex(message_string_hex))

        return bytearray(cipher_text)

    def decrypt_data(self, data: bytes):
        cipher = AES.new(bytearray.fromhex(self.common_secret), AES.MODE_ECB)

        cipher_text_bytearray = bytearray(data)
        return str(cipher.decrypt(cipher_text_bytearray), "ascii")
