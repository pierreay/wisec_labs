#!/usr/bin/python3

import sys
import binascii

secret_message = [31, 12, 31, 9, 12]
secret_pad = "wisec"

if len(secret_message) != len(secret_pad):
    print("Error! Message and pad shoud have the same length.")
    sys.exit()

rx_message = [chr(m^ord(p)) for m,p in zip(secret_message, secret_pad)]

print(rx_message)
