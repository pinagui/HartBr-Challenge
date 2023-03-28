import base64
import struct
# allow create package bytes to decode variables int, float, string, values

with open('data.txt', 'r') as f:
    data = f.read().split(":")[1]
print(data)

decoded = base64.b64decode(data)

print(decoded)
#b'2\x00\x00\x00\xfd\xff\xff\xff\x00\x00\x00\x00'

arrayDecoded = [format(byte, "02x") for byte in decoded]
# convert string to array
# format take off "x" from array with only 2 characters length
print(arrayDecoded)
# ['32', '00', '00', '00', 'fd', 'ff', 'ff', 'ff', '00', '00', '00', '00']
arrayBytes = ''.join(arrayDecoded).upper()
# join to concat 

print("Array de Bytes:", arrayBytes)

#LSB-First order bytes values are stored in memory or transmitted over a network
# least significant byte value comes first
# Least Significant Bit first
# This means that the least significant bit (on the right) contains the most important numerical information and the most significant bit (on the left) contains the sign information.
numberBytes = []

for i in range(0, len(decoded), 4):
  # range -> starts in 0, ends on length decoded and advance 4 by 4
  numberBytes.append(struct.unpack('<i', decoded[i:i+4])[0])
  # struct.unpack covert piece of byte array to signal lsb-first format
print("Números Lidos:", numberBytes)
  # < -> LSB First
  # i -> int number with 4 bytes
  # [i:i+4] -> advance 4 by 4
numberBytes.sort()
print("Números Ordenados:", numberBytes)

