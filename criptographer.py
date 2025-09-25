
class Criptographer:
    @staticmethod
    def encrypt(plaintext: str, key: str) -> str:
        p = plaintext.encode("utf-8")
        k = key.encode("utf-8")
        cipher_bytes = bytes([p[i] ^ k[i % len(k)] for i in range(len(p))])
        return cipher_bytes.hex()


    @staticmethod
    def decrypt(cipher_hex: str, key: str) -> str:
        cipher_bytes = bytes.fromhex(cipher_hex)
        k = key.encode("utf-8")
        plain_bytes = bytes([cipher_bytes[i] ^ k[i % len(k)] for i in range(len(cipher_bytes))])
        return plain_bytes.decode("utf-8")


