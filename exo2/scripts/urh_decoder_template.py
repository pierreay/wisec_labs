#!/usr/bin/env python3

# IMPORTANT
# - Each TODO line must be replaced by the adequate one to decode the
#   packet. Note that you can break a TODO line in multiple lines if you
#   prefer.
# - Start to read and replace the TODO statements at the code 'decode()'
#   function.

# For exit and argv.
import sys
# For text-based manipulations (This is actually a hint about the 'wrap'
# function).
import textwrap

def decode_xor(in_packet, out_packet):
    # Copy the first byte of the packet (0xA + Ctr) which is untouched by the
    # encryption process.
    # TODO: out_packet[0] = ???

    # XOR each byte of the encrypted packet with the previous one (starting
    # from the second one). Each XOR is our unencrypted byte.
    # TODO: for x in ???:
        # TODO: out_packet[x] = ???

def decode_bit_to_int(packet):
    # Group bits 8 by 8.
    # TODO: packet = ???

    # Perform integer conversion and return it.
    # TODO: return [??? for i in ???]

def decode_manchester(packet):
    # Group bits two by two (Manchester-I decode low/high transition).
    # TODO: packet = ???


    # Perform the decoding and return it.
    # TODO: return ''.join([??? if ??? else ??? for x in ???])

# Take an entire packet just after demodulation (with its synchronization
# field) and return the decoded packet.
def decode(in_packet):
    # Delete the first 24-bit sync field.
    # TODO: in_packet = ???

    # Manchester-I decoding.
    in_packet = decode_manchester(in_packet)

    # Convert decoded bit stream to integers.
    in_packet = decode_bit_to_int(in_packet)

    # Create the final packet.
    out_packet = [0] * len(in_packet)

    # De-XOR the incoming packet.
    decode_xor(in_packet, out_packet)

    # Format each integer in a 8-bit value.
    # TODO: out_packet = ["???".format(i) for i in ???]
    # TODO: return ???

decode(sys.argv[1])
