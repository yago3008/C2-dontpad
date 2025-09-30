
class Criptographer:
    @staticmethod
    def encrypt(plaintext: str, key: str) -> str:
        if not plaintext:
            return ""
        p = plaintext.encode("utf-8")
        k = key.encode("utf-8")
        cipher_bytes = bytes([p[i] ^ k[i % len(k)] for i in range(len(p))])
        return cipher_bytes.hex()


    @staticmethod
    def decrypt(cipher_hex: str, key: str) -> str:
        if not cipher_hex:
            return ""
        cipher_bytes = bytes.fromhex(cipher_hex)
        k = key.encode("utf-8")
        plain_bytes = bytes([cipher_bytes[i] ^ k[i % len(k)] for i in range(len(cipher_bytes))])
        return plain_bytes.decode("utf-8")


if __name__ == "__main__":
    key = "yago.martins"
    #rypted = Criptographer.encrypt('whoami', key)
    #print(f"{crypted}")
    decrypted = Criptographer.decrypt('0a0e0818721400151b4703120b150e015d67', key)
    print(f"{decrypted}")