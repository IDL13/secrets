from hashlib import md5

class MD5:
    def __init__(self, data):
        self.data = data

    def encrypt(self):
        self.data = md5(self.data.encode()).hexdigest()
        return self.data