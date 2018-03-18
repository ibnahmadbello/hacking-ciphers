# Transposition Cipher Encrypt/Decrypt File

import time, os, sys, TranspositionCipher.transpositionDecrypt, TranspositionCipher.transpositionEncrypt

def main():
    inputFileName = 'frankenstein.txt'
    # Be careful! If a file with the outputFileName name already exists,
    # this program will overwrite that file.
    outputFileName = 'frankenstein.encrypted.txt'
    myKey = 10
    myMode = 'encrypt' # set to 'encrypt' or 'decrypt'

    # If the input file does not exist, then the program terminates early.
    if not os.path.exists(inputFileName):
        print('The file %s does not exist. Quitting...' % (inputFileName))
        sys.exit()

    # If the output file already exists, give the user a chance to quit.
    if os.path.exists(outputFileName):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFileName))


