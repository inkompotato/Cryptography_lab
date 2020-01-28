from src.dictionary import Dictionary
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

d = Dictionary()

message = "e18d1c933da3f3bf1517ec5033fff8f7998d8108d88d04688510f94dde36d5d69f3a3fb92e4515d72204fd420d079156e0434caeee957c9784390c85e4354acb"

for i in range(0, len(d.wordarray)):
    length = len(d.wordarray[i])
    key = bytearray.fromhex(d.wordarray[i].encode("utf-8").hex())
    if length < 16:
        key = pad(key, 16)
    elif 16 < length < 24:
        key = pad(key, 24)
    elif 24 < length < 32:
        key = pad(key, 32)

    if not len(key) % 8 == 0:
        continue

    cipher = AES.new(key, AES.MODE_ECB)

    plain_text = cipher.decrypt(pad(bytearray.fromhex(message), 16))
    try:
        print(plain_text.decode('utf-8'))
    except:
        continue
