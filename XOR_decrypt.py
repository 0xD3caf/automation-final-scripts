#XOR Decryption
#Mackenzie Summers
#Run from root Kali account

import base64

def XOR_decrypt():
    XOR_str = "xL/UirHHs5Pkl+SQsZfhkrSXsZOyw7OV5pXkxbSS5cW+k7fJ+g=="
    decoded_str = base64.b64decode(XOR_str)
    possible_key = []
    for num in range(4):
        for num2 in range(256):
            result = decoded_str[num] ^ num2
            if result == 67 and num == 0:
                possible_key.append(num2)
                break
            elif result == 78 and num == 1:
                possible_key.append(num2)
                break
            elif result == 83 and num == 2:
                possible_key.append(num2)
                break
            elif result == 123 and num == 3:
                possible_key.append(num2)
                break
    key = [possible_key[0], possible_key[1]]
    print(xorcrypt(decoded_str, key))
    #we know that it starts with CNS{
def xorcrypt(plain,key):
    c = ""
    #Loop to perform xor on each character of plaintext
    for i in range(len(plain)):
        #Get current iteration character of plaintext
        c1 = plain[i]
        #Get current iteration character of key
        c2 = key[i%len(key)]
        #XOR unicode verion of plaintext to int (ord) and return string representation (chr)
        c += chr(c1 ^ c2)
    return c
XOR_decrypt()


