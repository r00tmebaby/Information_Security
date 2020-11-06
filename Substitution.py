""""
Inspired by Information security an as part of my study, I decided to play a bit and better understand Substitution encryption method
Here is a simple implementation example of Substitution cypher encoding and decoding methods
Ref: https://en.wikipedia.org/wiki/Substitution_cipher
"""

class Substitution:

    def charTable(self):
        return [
                    "A", "B", "C", "D", "E",
                    "F", "G", "H", "I", "J",
                    "K", "L", "M", "N", "O",
                    "P", "Q", "R", "S", "T",
                    "U", "V", "W", "X", "Y",
                    "Z", "9", "8", "7", "6",
                    "5", "4", "3", "2", "1",
                    "0", " ", "(", ")", ".",
                    "a", "b", "c", "d", "e",
                    "f", "g", "h", "i", "j",
                    "k", "l", "m", "n", "o",
                    "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y",
                    "z",
        ]

    def encode(self, text):
        result = ""
        for eachLetter in text:
            for index in range(len(self.charTable())):
                if eachLetter == self.charTable()[index]:
                     result += self.charTable()[index-1]
                     break
        return result


    def decode(self, text):
        result = ""
        for eachLetter in text:
            for index in range(len(self.charTable())):
                if eachLetter == self.charTable()[index]:
                    newIndex= index + 1
                    if index + 1 == len(self.charTable()):
                        newIndex = 0
                    result += self.charTable()[newIndex]
        return result

if __name__ == '__main__':

    import textwrap
    plainText = "Mike Capel (born October 13, 1961) is a former Major League Baseball right-handed " \
           "pitcher who played for the Chicago Cubs, Milwaukee Brewers, and Houston Astros. " \
           "In 49 career games, Capel pitched 62.1 innings, struck out 43 batters, and had a career win–loss record of 3–4 with a 4.62 earned run average. " \
           "A starting pitcher in college and parts of his Minor League Baseball career, he converted to relief pitching while in Chicago's minor league system. " \
           "The Philadelphia Phillies chose Capel in the 24th round of the 1980 Major League Baseball draft, but instead of signing with the team, " \
           "he opted to attend the University of Texas. He played on the 1982 USA College All-Star Team, which placed third in the Amateur World Series in Seoul. " \
           "The next year, Capel and the Texas Longhorns won the College World Series. After he was drafted by the Cubs, " \
           "Capel left Texas and played in six seasons of the minor leagues before he made his major league debut in 1988. (Full article...)"

    obj = Substitution()
    encodedText = obj.encode(plainText)

    print('\033[91m'+"Encoded text:\n", textwrap.fill(encodedText, 200))
    print("\n")
    decodedText = obj.decode(encodedText)
    print('\033[92m'+"Encoded text:\n", textwrap.fill(decodedText, 200))

