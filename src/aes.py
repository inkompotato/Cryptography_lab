from Crypto.Cipher import AES

mode = input("select mode e (encrypt) or d (decrypt): \n")
key_string = input("enter key: \n")
message_string = ""

if mode == "e":
    message_string = input("enter plaintext message: \n")
if mode == "d":
    message_string = input("enter encrypted message: \n")
else:
    print("unrecognized input, exiting program")
    quit(1)

key_string_hex = key_string.encode("ascii").hex()
cipher = AES.new(bytearray.fromhex(key_string_hex), AES.MODE_ECB)

if mode == "e":
    while len(message_string) % 16 != 0:
        message_string += " "
    message_string_hex = message_string.encode("ascii").hex()
    cipher_text = cipher.encrypt(bytearray.fromhex(message_string_hex))
    print(f"message has been encrypted: \n {cipher_text.hex()}")

if mode == "d":
    plain_text = cipher.decrypt(bytearray.fromhex(message_string))
    print(f"message has been decrypted: \n {plain_text.decode('ascii')}")
