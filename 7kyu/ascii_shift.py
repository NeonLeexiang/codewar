# ASCII Shift Encryption/Decryption
def ascii_encrypt(plaintext):
    count = 0
    rl = []
    for c in plaintext:
        rl.append(chr(ord(c)+count))
        count += 1
    return ''.join(rl)
    
def ascii_decrypt(plaintext):
    count = 0
    rl = []
    for c in plaintext:
        rl.append(chr(ord(c)-count))
        count += 1
    return ''.join(rl)
    
    
"""
def ascii_encrypt(s):    
    return ''.join(chr(ord(c)+i) for i, c in enumerate(s))
    
def ascii_decrypt(s):
    return ''.join(chr(ord(c)-i) for i, c in enumerate(s))
"""
