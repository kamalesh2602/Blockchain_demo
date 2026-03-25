import rsa

class Wallet:
    def __init__(self):
        self.public_key, self.private_key = rsa.newkeys(512)

    def sign(self, data):
        return rsa.sign(data.encode(), self.private_key, 'SHA-256')