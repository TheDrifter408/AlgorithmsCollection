import rsa;

def generate_keys():
    (pub_key, priv_key) = rsa.newkeys(1024)
    with open('keys/pub_key.pem',"wb") as f:
        f.write(pub_key.save_pkcs1('PEM'))

    with open('keys/priv_key.pem',"wb") as f:
        f.write(priv_key.save_pkcs1('PEM'))

def load_keys():
    with open("keys/pub_key.pem","rb") as f:
        pub_key = rsa.PublicKey.load_pkcs1(f.read())

    with open("keys/priv_key.pem","rb") as f:
        priv_key = rsa.PrivateKey.load_pkcs1(f.read())

    return pub_key,priv_key
    
def encrypt(msg,key):
    return rsa.encrypt(msg.encode('ascii'),key);

def decrypt(cipheredText,key):
    try:
        return rsa.decrypt(cipheredText,key).decode('ascii')
    except:
        return False

def sign_sha1(msg,key):
    return rsa.sign(msg.encode("ascii"),key,'SHA-1')

def verify_sha1(msg,signature,key):
    try:
        return rsa.verify(msg.encode('ascii'),signature,key) == "SHA-1"
    except:
        return False
    

generate_keys()
pub_key, priv_key = load_keys()

message = input("Enter a Message: ")

cipherText = encrypt(message,pub_key)

signature = sign_sha1(message,priv_key)

plainText = decrypt(cipherText,priv_key)

print(f"Cipher Text: {cipherText}")
print(f"Signature: {signature}")

if plainText:
    print(f"Plain text: {plainText}")
else:
    print("Could not decrypt.")

if verify_sha1(plainText,signature,pub_key):
    print("Signature verified");
else:
    print('Could not verify.')
