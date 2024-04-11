# How to convert Int to Bytes in Python

num = 2048

my_bytes = num.to_bytes(2, byteorder='big')
print(my_bytes)  # 👉️ b'\x08\x00'