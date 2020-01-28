from Crypto.Cipher import AES
from src.dictionary import Dictionary
from time import time

current_time_ms = lambda: int(round(time() * 1000))

d = Dictionary()
mode = input("select mode e (encrypt), r (encrypt with random key), d (decrypt) or c (crack)?: \n")

key_string = ""
if mode == "e" or mode == "d":
    key_string = input("enter key: \n")
elif mode == "r":
    key_string = d.random_word()
    print(f"{key_string} was chosen as the random key")
    numbers = input("salt key (y / n)?\n")
    if numbers == "y":
        key_string = key_string.replace("o", "0")
        key_string = key_string.replace("i", "1")
        key_string = key_string.replace("e", "3")
        key_string = key_string.replace("s", "5")
        print(f"key looks now like this: {key_string}")
    mode = "e"
elif mode == "c":
    print("craking mode selected, no key input is required")

while len(key_string) % 16 != 0:
    key_string += " "

message_string = ""

if mode == "e":  # r = e at this point
    message_string = input("enter plaintext message: \n")
elif mode == "d" or mode == "c":
    message_string = input("enter encrypted message: \n")
else:
    print("unrecognized input, exiting program")
    quit(1)

if mode == "e":
    key_string_hex = key_string.encode("ascii").hex()
    cipher = AES.new(bytearray.fromhex(key_string_hex), AES.MODE_ECB)

    while len(message_string) % 16 != 0:
        message_string += " "
    message_string_hex = message_string.encode("ascii").hex()
    cipher_text = cipher.encrypt(bytearray.fromhex(message_string_hex))
    print(f"message has been encrypted: \n {cipher_text.hex()}")

if mode == "c":
    start = current_time_ms()
    for i in range(0, len(d.wordarray)):
        length = len(d.wordarray[i])
        if length < 16:
            d.wordarray[i] += " "*(16-length)
            # d.wordarray[i] = (d.wordarray[i]*16)[0:16]
        elif 16 < length < 24:
            d.wordarray[i] += " "*(24-length)
            # d.wordarray[i] = (d.wordarray[i]*2)[0:24]
        elif 24 < length < 32:
            d.wordarray[i] += " "*(32-length)
            # d.wordarray[i] = (d.wordarray[i]*2)[0:32]

        try:
            new_key_string_hex = d.wordarray[i].encode("utf-8").hex()
            new_cipher = AES.new(bytearray.fromhex(new_key_string_hex), AES.MODE_ECB)
            plain_text = new_cipher.decrypt(bytearray.fromhex(message_string))
            print(f"message candidate: \n {plain_text.decode('utf-8')}, with key \"{d.wordarray[i]}\"")
        except (UnicodeDecodeError, ValueError):
            continue
    end = current_time_ms()
    print(f"finished cracking in {end-start}ms")


if mode == "d":
    key_string_hex = key_string.encode("ascii").hex()
    cipher = AES.new(bytearray.fromhex(key_string_hex), AES.MODE_ECB)

    plain_text = cipher.decrypt(bytearray.fromhex(message_string))
    print(f"message has been decrypted: \n {plain_text.decode('ascii')}")
