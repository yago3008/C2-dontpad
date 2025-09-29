class Criptographer:
    @staticmethod
    def e(pt, k):
        if not pt:
            return ""
        p = pt.encode("utf-8")
        k = k.encode("utf-8")
        cb = bytes([p[i] ^ k[i % len(k)] for i in range(len(p))])
        return cb.hex()


    @staticmethod
    def d(ch, k):
        if not ch:
            return ""
        cb = bytes.fromhex(ch)
        k = k.encode("utf-8")
        plain_bytes = bytes([cb[i] ^ k[i % len(k)] for i in range(len(cb))])
        return plain_bytes.decode("utf-8")