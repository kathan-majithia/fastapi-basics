from passlib.context import CryptContext

cc = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password: str):
        return cc.hash(password)
    
    def verify(cipher_text, plain_text):
        return cc.verify(plain_text,cipher_text)