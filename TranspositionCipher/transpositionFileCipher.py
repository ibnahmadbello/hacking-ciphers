# Transposition Cipher Encrypt/Decrypt File

import time, os, sys, TranspositionCipher.transpositionDecrypt, TranspositionCipher.transpositionEncrypt

def main():
    inputFileName = 'frankenstein.txt'
    # Be careful! If a file with the outputFileName name already exists,
    # this program will overwrite that file.
