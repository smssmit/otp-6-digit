# Write a python program to generate 6-digit alphanumeric OTP.

import random, math


def otpgen():
    string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" #you can also add special symbols is you need
    otp = ""
    length = len(string)
    for i in range(6): #by changing the range you can change the otp length
        otp += string[math.floor(random.random() * length)]
    print("Your OTP is", otp)


otpgen()
