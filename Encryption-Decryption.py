from Crypto.Cipher import AES



#secret_key = os.urandom(BLOCK_SIZE) i generated once and i will use that always
secret_key=b'b\x90\xf7\x1d\\KY\xc3\xd7\x13\xf1\x90\xba\xe4HS\xe3\xce\x1cd\x8f\xdf\xda\xc8u\xa9B\x85-&<\xb7'
Initialization_vector = 'This is a testIV'#IV must be 16 bytes long

def encryption(messageToEncrypt):
    obj = AES.new(secret_key, AES.MODE_CBC,Initialization_vector)
    return obj.encrypt(messageToEncrypt)



def decryption(ciphertext):
    obj2 = AES.new(secret_key, AES.MODE_CBC,Initialization_vector)
    return obj2.decrypt(ciphertext).decode()

if __name__=="__main__":
    message = encryption("The answer is no")#The message must be a  be a multiple of 16 bytes
    print(message)
    message = decryption(message)
    print("Decrypted successful:" + message)
