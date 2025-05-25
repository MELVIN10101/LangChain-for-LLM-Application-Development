from binascii import unhexlify

# Messages
m3_hex = "3c6e09bc4ba9953d08f9ebca80a12154175720885a9532d6"
m3 = unhexlify(m3_hex)

# Partial key known bytes
key = [None]*32
key[:8] = list(unhexlify("42e56dfb42ab0b70"))
key[16:24] = list(unhexlify("65d065cafd586697"))

# Known plaintext start for message 3:
plaintext_known = b"null.chennai{"

offset_m3 = 14

# Recover key bytes from known plaintext of message 3
for i, pt_byte in enumerate(plaintext_known):
    c_byte = m3[i]
    key_pos = (offset_m3 + i) % 32
    key[key_pos] = c_byte ^ pt_byte

# Decrypt message 3 with known key bytes
decrypted = []
for i in range(len(m3)):
    k_pos = (offset_m3 + i) % 32
    if key[k_pos] is None:
        decrypted.append(ord('?'))
    else:
        decrypted.append(m3[i] ^ key[k_pos])

print("Decrypted message 3:", bytes(decrypted).decode('ascii', errors='replace'))
