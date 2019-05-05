import math,random

def getOTP(otp_len=10):
    global vocab
    otp=""
    for i in range(otp_len):
        idx = math.floor(random.random() * len(vocab))
        otp += vocab[idx]
    return otp

vocab="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz$@%#"
l = int(input("Enter length of OTP:"))
print("OTP:",getOTP(l))
