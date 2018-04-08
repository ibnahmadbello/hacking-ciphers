# This program proves that the keyspace of the affine cipher is limited
# to len(SYMBOLS) ^ 2.

import AffineCiphers.affineCipher, AffineCiphers.cryptomath

message = 'Make things as simple as possible, but not simpler.'
for keyA in range(2, 100):
    key = keyA * len(AffineCiphers.affineCipher.SYMBOLS) + 1

    if AffineCiphers.cryptomath.gcd(keyA, len(AffineCiphers.affineCipher.SYMBOLS)) == 1:
        print(keyA, AffineCiphers.affineCipher.encryptMessage(key, message))