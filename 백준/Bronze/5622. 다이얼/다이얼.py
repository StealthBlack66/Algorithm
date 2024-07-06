S=input()
result=0
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for letter in S:
    if letter in alphabet[0:3]:
        result+=3
    elif letter in alphabet[3:6]:
        result+=4
    elif letter in alphabet[6:9]:
        result+=5
    elif letter in alphabet[9:12]:
        result+=6
    elif letter in alphabet[12:15]:
        result+=7
    elif letter in alphabet[15:19]:
        result+=8
    elif letter in alphabet[19:22]:
        result+=9
    else:
        result+=10
print(result)