#!/usr/bin/env python3

# Compute a checksum for a packet (with the checksum field set to 0) or verify
# a packet (with the checksum field set to the CRC remainder).

import sys
import textwrap
import crcsolver # https://pypi.org/project/crcsolver/

# Group the bits 8 by 8 and perform integer conversion.
packet = textwrap.wrap(sys.argv[1], 8)
packet = [int(i, 2) for i in packet]

# Manual computation:

# Compute the checksum by XORing all fields of the frame. Since the checksum is
# on 4-bits, XOR each fields two times with a 4-bit right shift.
cks = 0
for i in range(len(packet)):
    cks = cks ^ packet[i] ^ (packet[i] >> 4)
cks = cks & 0xF
# Format the checksum into binary and print it.
cks = "{0:04b}".format(cks)
print(cks)

# Using CRCSolver:

# The width=4 set the x^4 factor and the poly=0x1 set the x^0 factor. Hence, the polynome is: x^4 + 1
cks = "{0:04b}".format(crcsolver.compute(packet, {'width':4, 'poly':0x1, 'init':0x0, 'refin':False, 'refout':False, 'xorout':0x0}))
print(cks)
