from hashlib import md5

class MD5:
    def __init__(self, data: str):
        self.data = data

    def encrypt(self):
        self.data = md5(self.data.encode()).hexdigest()
        return self.data
    
def check(data: str, hash_string: str) -> bool:
    if md5(data.encode()).hexdigest() == hash_string:
        return True
    else:
        return False