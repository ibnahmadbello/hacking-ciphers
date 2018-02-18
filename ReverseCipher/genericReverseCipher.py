# Reverse Cipher

message = input('Enter the message you want to encrypt: ')
translated = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1

print(translated)