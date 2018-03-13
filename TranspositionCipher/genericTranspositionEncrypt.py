#Generic Transposition Cipher Encryption


def main():
    myMessage = input('Enter the plain text to be encrypted:\n')
    myKey = int(input('Enter your encryption key:\n'))

    ciphertext = encryptMessage(myKey, myMessage)

    print(ciphertext + '|')


def encryptMessage(key, message):

    ciphertext = [''] * key
    for col in range(key):
        pointer = col

        while pointer < len(message):
            ciphertext[col] += message[pointer]
            pointer += key

    return ''.join(ciphertext)

if __name__ == '__main__':
    main()
