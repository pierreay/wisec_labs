#!/usr/bin/env python3

# This decoder has two mode:
# - Batch : just feed a bitstream in argument, it will output a decoded bitstream (for URH).
# - Interactive : without argument, feed bitstream(s) in the prompt and type enter to decode it.

# For exit and argv.
import sys
# For text-based manipulations.
import textwrap

# Check the validity of the input packet. Return 1 if packet is correct.
def packet_check(packet):
    return 1 if len(packet) == 136 or len(packet) == 135 else 0 

def decode_xor(in_packet, out_packet):
    # Copy the first byte of the packet (0xA + Ctr) which is untouched by the
    # encryption process.
    out_packet[0] = in_packet[0]
    # XOR each byte of the encrypted packet with the previous one (starting
    # from the second one). Each XOR is our unencrypted byte.
    for x in range(1, len(in_packet)):
        out_packet[x] = in_packet[x] ^ in_packet[x-1]

def decode_bit_to_int(packet):
    # Group bits 8 by 8.
    packet = textwrap.wrap(packet, 8)
    # Perform integer conversion and return it.
    return [int(i, 2) for i in packet]

def decode_manchester(packet):
    # Group bits two by two (Manchester-I decode low/high transition).
    packet = textwrap.wrap(packet, 2)
    # Perform the decoding and return it.
    return ''.join(['1' if x == '01' else '0' for x in packet])

# Take an entire packet just after demodulation (with its synchronization
# field) and return the decoded packet.
def decode(in_packet):
    # Delete the first 24-bit sync field.
    in_packet = in_packet[24:]

    # Manchester-I decoding.
    in_packet = decode_manchester(in_packet)

    # Convert decoded bit stream to integers.
    in_packet = decode_bit_to_int(in_packet)

    # Create the final packet.
    out_packet = [0] * len(in_packet)

    # De-XOR the incoming packet.
    decode_xor(in_packet, out_packet)

    # Format each integer in a 8-bit value.
    out_packet = ["{0:08b}".format(i) for i in out_packet]
    return ''.join(out_packet)

# Batch mode (for URH).
if len(sys.argv) == 2:
    # Check the length of the packet. If length is not good, just output
    # nothing for URH.
    if packet_check(sys.argv[1]):
        print(decode(sys.argv[1]))
        
# Interactive mode.
else:
    # Information message.
    print("Press enter on an empty input to quit.")
    while True:
        # Prompt.
        in_packet = input(">>> ")
        # Quit on empty packet.
        if in_packet == "":
            sys.exit()
        # Check the length of the packet.
        if packet_check(in_packet):
            # Decode the packet and print fields.
            out_packet = decode(in_packet)
            print("Key   [00-08]:")
            print("  OxA [00-04]:" + out_packet[0:4])
            print("  Ctr [04-08]:" + out_packet[4:8])
            print("Ctrl  [08-12]:" + out_packet[8:12])
            print("Chk   [12-16]:" + out_packet[12:16])
            print("RC:   [16-32]:" + out_packet[16:32])
            print("Addr  [32-56]:" + out_packet[32:56])
        # Bad length, just inform the user and retry.
        else:
            print("Packet length error!")
