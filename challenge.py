import base64
import struct

with open('data.txt', 'r') as f:
    data = f.read().split(":")[1]

decoded = base64.b64decode(data)

arrayDecoded = [format(byte, "02x") for byte in decoded]

arrayBytes = ''.join(arrayDecoded).upper()
print("Array de Bytes:", arrayBytes)

numberBytes = []

for i in range(0, len(decoded), 4):
  numberBytes.append(struct.unpack('<i', decoded[i:i+4])[0])

print("Números Lidos:", numberBytes)

numberBytes.sort()
print("Números Ordenados:", numberBytes)
