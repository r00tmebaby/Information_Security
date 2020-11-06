""""
Inspired by Information security an as part of my study, I decided to play a bit and better understand RSA encryption method
Here is s simple implementation example of RSA encoding and decoding

Reference: https://www.youtube.com/watch?v=oOcTVTpUsPQ
Referebce: https://crypto.stackexchange.com/questions/5889/calculating-rsa-private-exponent-when-given-public-exponent-and-the-modulus-fact

"""

import random


class RSA:
    """

    Class RSA Generates public and private keys that can be used for
    RSA encryption and decryption

    #####-RSA- ### -parameters-#######
    ##################################
    # p= prime number
    # q= prime number
    # n = p * q
    # fn = (p-1) * (q-1)
    # e = 1 * (e / GCD)  *Important:  E -> {1 < E < fn , prime with N an FN}
    # d = ((1/e) % n) equal 1
    # public key (e, n)
    # private key (d, n)
    ###################################


    """


    rsaKeySize = 4
    minBytes = 1024

    def __init__(self, RSALength):
        if RSALength <= self.rsaKeySize:
            self.rsaKeySize = RSALength

    def is_prime(self, n):
        """ Test if a number is prime
            Args:
                n -- int -- the number to test
                k -- int -- the number of tests to do
            return True if n is prime
        """
        # Test if n is not even.
        # But care, 2 is prime !
        if n == 2 or n == 3:
            return True
        if n <= 1 or n % 2 == 0:
            return False
        # find r and s
        s = 0
        r = n - 1
        while r & 1 == 0:
            s += 1
            r //= 2
        # do k tests
        for _ in range(self.rsaKeySize):
            a = random.randrange(2, n - 1)
            x = pow(a, r, n)
            if x != 1 and x != n - 1:
                j = 1
                while j < s and x != n - 1:
                    x = pow(x, 2, n)
                    if x == 1:
                        return False
                    j += 1
                if x != n - 1:
                    return False
        return True

    def test_prime(self):
        p = random.getrandbits(self.rsaKeySize)
        p |= (1 << self.rsaKeySize - 1) | 1
        return p

    def prime_number(self):
        p = 4
        while not RSA.is_prime(self, p):
            p = RSA.test_prime(self)
        return p

    def modinv(self, e, phi):
        """"
            Euclidean algorithm implementation
            Ref: https://crypto.stackexchange.com/questions/5889/calculating-rsa-private-exponent-when-given-public-exponent-and-the-modulus-fact
        """
        d_old = 0
        r_old = phi
        d_new = 1
        r_new = e
        while r_new > 0:
            a = r_old // r_new
            (d_old, d_new) = (d_new, d_old - a * d_new)
            (r_old, r_new) = (r_new, r_old - a * r_new)
        return d_old % phi if r_old == 1 else None

    def generateKeys(self):
        """
        Generate and display the keys
        """
        p = self.prime_number()
        q = self.prime_number()
        fn = (p - 1) * (q - 1)
        e = random.randint(1, fn)
        n = p * q
        d = self.modinv(e, fn)
        if d is not None and d > e:
            publicKey = [e, n]
            privateKey = [d, n]

            print("Public Key: (%s, %s)\nPrivate Key: (%s, %s)" % (
                publicKey[0], publicKey[1], privateKey[0], privateKey[1]))
        else:
            self.generateKeys()


def RSAtest(text, key):
    """
    Encrypt or decrypt function
    formula (text ** key[0]) % key[1]

    :param text: plain text type: string
    :param key: type array of exactly two integers[5,6]
    :return: encrypted or decrypted text
    """
    sequence = []
    result = ""
    if len(key) == 2 and type(key) == list:
        for each in text:
            sequence.append(pow(ord(each), key[0]) % key[1])
    else:
        print("The key must be a list")
    for each in sequence:
        result += chr(each)
    return result


if __name__ == '__main__':
    # Generate new keys
    obj = RSA(4)
    obj.generateKeys()

    # Set a plain text
    import textwrap

    plainText = "Mike Capel (born October 13, 1961) is a former Major League Baseball right-handed " \
                "pitcher who played for the Chicago Cubs, Milwaukee Brewers, and Houston Astros. " \
                "In 49 career games, Capel pitched 62.1 innings, struck out 43 batters, and had a career win–loss record of 3–4 with a 4.62 earned run average. " \
                "A starting pitcher in college and parts of his Minor League Baseball career, he converted to relief pitching while in Chicago's minor league system. " \
                "The Philadelphia Phillies chose Capel in the 24th round of the 1980 Major League Baseball draft, but instead of signing with the team, " \
                "he opted to attend the University of Texas. He played on the 1982 USA College All-Star Team, which placed third in the Amateur World Series in Seoul. " \
                "The next year, Capel and the Texas Longhorns won the College World Series. After he was drafted by the Cubs, " \
                "Capel left Texas and played in six seasons of the minor leagues before he made his major league debut in 1988. (Full article...)"

    # Use the public key to encrypt the text
    print('\033[91m'+"Encoded text:\n", textwrap.fill(RSAtest(plainText, [17, 143]), 200))

    cypherText = RSAtest(plainText, [17, 143])

    # Use the private key to decrypt the text
    print('\033[92m'+"Decoded text:\n", textwrap.fill(RSAtest(cypherText, [113, 143]), 200))
