#!/usr/bin/python3

import sys
import binascii

if len(sys.argv) != 3:
    print("Error! Usage: number_station.py MESSAGE PAD")
    sys.exit()

secret_message = sys.argv[1]
secret_pad = sys.argv[2]

if len(secret_message) != len(secret_pad):
    print("Error! Message and pad should have the same length")
    sys.exit()

tx_message = [ord(m)^ord(p) for m,p in zip(secret_message, secret_pad)]

print(tx_message)
