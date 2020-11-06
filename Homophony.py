""""
Inspired by Information security an as part of my study, I decided to play a bit and better understand Homophony encryption method
Here is s simple implementation example of Homophony encoding and decoding method
"""

class homophony:
    @staticmethod
    def charTable():
        return [
            ["A", ["†", "„", "§", "É"]],
            [" ", ["Ú", "Ý", "Ü", "Þ"]],
            ["B", ["€", "¦", "È", "Ò"]],
            ["C", ["Š", "‡", "Ë", "Ï"]],
            ["D", ["ƒ", "‘", "¢", "Ê"]],
            ["E", ["Ž", ".", "£", "Ì"]],
            ["F", ["™", ":", "Ä", "Ö"]],
            ["G", [",", "^", "\"", "á"]],
            ["H", ["#", "!", "¤", "Å"]],
            ["I", ["@", "¥", "ã"]],
            ["J", ["A", "2", "À", "Ù"]],
            ["K", ["b", "1", "Á", "Õ"]],
            ["L", ["6", "8", "Â", "é"]],
            ["M", ["4", "0", "¿", "ù"]],
            ["N", ["5", "c", "»", "ç"]],
            ["O", ["z", "I", "º", "æ"]],
            ["P", ["š", "/", "¹", "à"]],
            ["Q", ["\\", "=", "¸", "û"]],
            ["R", ["+", "%", "µ", "Ø"]],
            ["S", ["*", ")", "³", "ê"]],
            ["T", ["]", "(", "²", "ì"]],
            ["U", ["}", "{", "ž", "Ð"]],
            ["V", ["_", "r", "¬", "Ñ"]],
            ["W", ["-", "&", "©", "×"]],
            ["X", ["~", "`", "«"]],
            ["Y", [">", "|", "®"]],
            ["Z", ["?", "<", "°"]],
            ["0", ["Æ", "Ç", "Ô"]],
            ["1", ["ä", "ø", "ï"]],
            ["2", ["ß", "õ", "ÿ"]],
            ["3", ["è", "ö", "ô"]],
            ["4", ["Ó", "þ", "ò"]],
            ["5", ["ë", "ü", "ó"]],
            ["6", ["í", "a", "ð"]],
            ["7", ["ñ", "ý", "î"]],
            ["8", ["÷", "n", "â"]],
            ["9", ["ú", "p", "å"]],
        ]

    @staticmethod
    def encode(plaintext):
        import random
        result = ""
        for each in plaintext.upper():
            for encodes in homophony.charTable():
                if encodes[0] == each:
                    result += str(random.choice(encodes[1]))
                    break
        return result

    @staticmethod
    def decode(encryptedText):
        result = ""
        for eachNumber in encryptedText:
            for encodes in homophony.charTable():
                if eachNumber in encodes[1]:
                    result += encodes[0]
                    break
        return result


if __name__ == '__main__':

    plainText = "Mike Capel (born October 13, 1961) is a former Major League Baseball right-handed " \
           "pitcher who played for the Chicago Cubs, Milwaukee Brewers, and Houston Astros. " \
           "In 49 career games, Capel pitched 62.1 innings, struck out 43 batters, and had a career win–loss record of 3–4 with a 4.62 earned run average. " \
           "A starting pitcher in college and parts of his Minor League Baseball career, he converted to relief pitching while in Chicago's minor league system. " \
           "The Philadelphia Phillies chose Capel in the 24th round of the 1980 Major League Baseball draft, but instead of signing with the team, " \
           "he opted to attend the University of Texas. He played on the 1982 USA College All-Star Team, which placed third in the Amateur World Series in Seoul. " \
           "The next year, Capel and the Texas Longhorns won the College World Series. After he was drafted by the Cubs, " \
           "Capel left Texas and played in six seasons of the minor leagues before he made his major league debut in 1988. (Full article...)"


    encoded = homophony.encode(plainText)
    print("Homophony Encoded Text: ", encoded)
    print("Homophony Decoded Text: ", homophony.decode(encoded))


