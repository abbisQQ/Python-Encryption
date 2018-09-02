from Crypto.Cipher import AES



messageClear= input("test me: ")
#print the messages length
print(len(messageClear))
#we need a message that is multiplier of 16
while(len(messageClear)%16!=0):
    messageClear = messageClear +" "
messageClear =  messageClear.encode()

#secret_key = os.urandom(BLOCK_SIZE) i generated once and i will use that always
secret_key=b'b\x90\xf7\x1d\\KY\xc3\xd7\x13\xf1\x90\xba\xe4HS\xe3\xce\x1cd\x8f\xdf\xda\xc8u\xa9B\x85-&<\xb7'
Initialization_vector = b'This is a testIV'#IV must be 16 bytes long

def encryption(messageToEncrypt):
    obj = AES.new(secret_key, AES.MODE_CBC,Initialization_vector)
    return obj.encrypt(messageToEncrypt)



def decryption(ciphertext):
    obj2 = AES.new(secret_key, AES.MODE_CBC,Initialization_vector)
    return obj2.decrypt(ciphertext).decode()

if __name__=="__main__":
    message = encryption(messageClear)#The message must be a  be a multiple of 16 bytes
    print(message)
    message = decryption(message)
    message = message.replace("~","")
print("Decrypted successful:" + message)
