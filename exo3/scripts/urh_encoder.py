#!/usr/bin/python2

import sys
import textwrap

# get stream from urh
in_packet = sys.argv[1]

# sync packet
if len(in_packet) == 16:
    print in_packet
    sys.exit()

# normal message packet
in_packet = textwrap.wrap(in_packet, 8)
in_packet = [int(i, 2) for i in in_packet]

for i in range(1, len(in_packet)):
    in_packet[i] = in_packet[i] ^ in_packet[i - 1]

in_packet = ["{0:{fill}8b}".format(i, fill='0') for i in in_packet]

in_packet = ''.join(in_packet)

# Manchester-I encoding
in_packet = ''.join(['01' if x == '1' else '10' for x in in_packet])

# add sync bits removed by the encoder
in_packet = '111100001111000011111110' + in_packet

print in_packet
 
