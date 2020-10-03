import hashlib

target = '8e7c9e'  
candidate = 0
while True:
    plaintext = str(candidate)
    hash = hashlib.md5(plaintext.encode('ascii')).hexdigest() #ascii encoding then md5 encoding
    if hash[:6] == target:
        print('plaintext:"' + plaintext + '", md5:' + hash)  # md5 pattern found
        break
    candidate = candidate + 1
