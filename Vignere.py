""""
Inspired by Information security an as part of my study, I decided to play a bit and better understand Substitution encryption method
Here is a simple implementation example of Substitution cypher encoding and decoding methods
Ref: https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
"""


class Vignere:

    def charTable(self):
        #Ascii table generator / only printable characters
        characters = list(map(chr, range(32, 127)))
        return characters

    def keyToNumbers(self, keyText):
        """
        :param keyText: text  (one word preferably)
        :return: list of ascii number
        """
        return [ord(i) for i in keyText]

    def encrypt(self, text, encKey):
        result = ""
        key = self.keyToNumbers(encKey)
        keyIndex = 0
        for eachLetter in text:
            if keyIndex % len(key) == 0:
                keyIndex = 0
            for index in range(len(self.charTable())):
                if eachLetter == self.charTable()[index]:
                    result += self.charTable()[(index + key[keyIndex]) % len(self.charTable())]
            keyIndex += 1
        return result

    def decrypt(self, text, encKey):
        result = ""
        key = self.keyToNumbers(encKey)
        keyIndex = 0
        for eachLetter in text:
            if keyIndex % len(key) == 0:
                keyIndex = 0
            for index in range(len(self.charTable())):
                if eachLetter == self.charTable()[index]:
                    result += self.charTable()[(index - key[keyIndex]) % len(self.charTable())]
            keyIndex += 1
        return result


if __name__ == '__main__':
    import textwrap

    encKey = "I like information security"

    plainText = "Mike Capel (born October 13, 1961) is a former Major League Baseball right-handed " \
           "pitcher who played for the Chicago Cubs, Milwaukee Brewers, and Houston Astros. " \
           "In 49 career games, Capel pitched 62.1 innings, struck out 43 batters, and had a career win loss record of 34 with a 4.62 earned run average. " \
           "A starting pitcher in college and parts of his Minor League Baseball career, he converted to relief pitching while in Chicago's minor league system. " \
           "The Philadelphia Phillies chose Capel in the 24th round of the 1980 Major League Baseball draft, but instead of signing with the team, " \
           "he opted to attend the University of Texas. He played on the 1982 USA College AllStar Team, which placed third in the Amateur World Series in Seoul. " \
           "The next year, Capel and the Texas Longhorns won the College World Series. After he was drafted by the Cubs, " \
           "Capel left Texas and played in six seasons of the minor leagues before he made his major league debut in 1988. (Full article...)"

    obj = Vignere()
    encoded = obj.encrypt(plainText, encKey)
    print('\033[91m'+"Encoded text:\n", textwrap.fill(encoded, 200))
    print('\033[92m'+"Decoded text:\n", textwrap.fill(obj.decrypt(encoded, encKey), 200))
