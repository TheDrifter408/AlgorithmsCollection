import random;
import math;

def is_prime(number):
    if(number < 2):
        return False
    for i in range(2,number//2 + 1):
        if number % i == 0:
            return False
    return True

def generate_prime(min_val,max_val):
    prime = random.randint(min_val,max_val)
    while not is_prime(prime):
        prime = generate_prime(min_val, max_val)
    return prime

def mod_inverse(e, phi):
    for d in range(3, phi):
        if((d * e) % phi == 1):
            return d
    raise ValueError("mod_inverse does not exist")

p, q = generate_prime(1000,5000), generate_prime(1000,5000)

while p == q:
    q = generate_prime(1000,5000)

n = p * q

phi = (p-1)*(q-1)

e = random.randint(3, phi - 1)

while math.gcd(e,phi) != 1:
    e = random.randint(e,phi - 1)

d = mod_inverse(e,phi)

print("Public Key: ",e)
print("Private Key: ",d)
print("n: ",n)
print("phi: ",phi)
print("p and q: ",p,q)

message = "Hello World"
# ord returns unicode for each character c in message
message_encoded = [ord(c) for c in message]
#pow(c,e,n) returns (c^e) mod n 
cipherText = [pow(c,e,n) for c in message_encoded]
# cipherText is now an unreadable text
print(cipherText)
message_encoded = [pow(c,d,n) for c in cipherText]
message = "".join(chr(c) for c in message_encoded)
print(message)

