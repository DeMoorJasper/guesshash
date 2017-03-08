import hashlib
from itertools import combinations

WithoutBase64 = 'caed6a36e83ecc9399453dd7ff4144972db6a80dfda0b35807d352a3f7ba379d312dc45806b26f30570537e205d034782a53af93b195ee687092a7bb52336081'
salt = '7049548a11ca1d08d017d2429bb04a3b'

# SHA512 * 512( SHA256 * 256(SHA1(MD5 * 5( plaintext + salt ))))


letters = 'abcdefghijklmnopqrstuvwxyz'

char = 1
while char < 6:
    print(char)
    for subset in combinations(letters, char):
        strPass = ''.join(subset)
        saltyPass = strPass + salt
        # print(strPass)
        res = saltyPass

        counter = 0

        while counter < 5:
            res = hashlib.md5(res.encode('utf-8')).hexdigest()
            # print(res)
            counter += 1

        res = hashlib.sha1(res.encode('utf-8')).hexdigest()
        counter = 0

        while counter < 256:
            res = hashlib.sha256(res.encode('utf-8')).hexdigest()
            # print(res)
            counter += 1

        counter = 0

        while counter < 512:
            res = hashlib.sha512(res.encode('utf-8')).hexdigest().lower()
            # print(res)
            counter += 1

        if res == WithoutBase64:
            print('==== SUCCESS ====')
            print(strPass)

    char += 1

print("NO PASSWORD FOUND")