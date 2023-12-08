import random;
import math;
import time;

def power_exponentiation(base,power, m):
    #uses divide and conquer strategy:
    if power == 0: 
        return 1
    half_power = power_exponentiation(base, power // 2, m)
    
    if(power % 2 == 0):
        res = half_power * half_power
        return res % m
    else:
        res = base * half_power * half_power
        return res % m


def is_prime(number):
    if number <= 1:
        return False
    if number % 2 == 0:
        return number == 2
    max_div = math.floor(math.sqrt(number))
    for i in range(3, 1 + max_div,2):
        if number % i == 0:
            return False
    return True
    # if(number < 2):
    #     return False
    # for i in range(2,(number//2) + 1):
    #     if number % i == 0:
    #         return False
    # return True

def generate_prime(min_val,max_val):
    prime = random.randint(min_val,max_val)
    while not is_prime(prime):
        prime = generate_prime(min_val, max_val)
    return prime

def extendedGCD(a,b):
    if a == 0:
        return (b,0,1)
    g,y,x = extendedGCD(b % a, a)
    return (g,x - (b // a) * y, y)

def mod_inverse(e, phi):
    g, x, y = extendedGCD(e,phi)
    if g != 1:
        raise Exception("No modular inverse")
    return x % phi
    # for d in range(3, phi):
    #     if((d * e) % phi == 1):
    #         return d
    # raise ValueError("mod_inverse does not exist")




p, q = generate_prime(10000,50000), generate_prime(10000,50000)

while p == q:
    q = generate_prime(10000,50000)

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

def rsaBasic():
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


def rsaImprove():
    # ord returns unicode for each character c in message
    message = "Hello World"
    message_encoded = [ord(c) for c in message]
    cipherText = [power_exponentiation(c,e,n) for c in message_encoded]
    print("CipherText:",cipherText)
    message_encoded = [power_exponentiation(c,d,n) for c in cipherText]
    message = "".join(chr(c) for c in message_encoded)
    print(message)


rsaBasicStartTime = time.perf_counter()
rsaBasic()
rsaBasicEndTime = time.perf_counter()
rsaBasicTime = rsaBasicEndTime - rsaBasicStartTime

rsaImproveStartTime = time.perf_counter()
rsaImprove()
rsaImproveEndTime = time.perf_counter()
rsaImproveTime = rsaImproveEndTime - rsaImproveStartTime



print(f"rsaImproveTime: {rsaImproveTime:.6f} vs rsaBasic: {rsaBasicTime:.6f}")




