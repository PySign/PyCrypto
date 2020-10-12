import rsa


class Crypto:
    def __init__(self, size=1024*3):
        self.size = size

    def encrypt(self, plain_text:str):
        pass

    def decrypt(self, cypher_text:str):
        pass

    def get_key(self):
        self.public, self.private = rsa.newkeys(self.size)
        return self.public, self.private