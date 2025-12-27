# Input variable
n = 1337671203

# Reverse 32 bits
result = 0
for _ in range(32):
    result = (result << 1) | (n & 1)
    n >>= 1

print(result)
