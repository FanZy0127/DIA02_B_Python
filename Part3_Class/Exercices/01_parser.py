
class Parse:
    def __init__(self, separator, message):
        self.separator = separator
        self.message = message

    def __str__(self):
        return self.get_parsed_sentence()

    def get_parsed_sentence(self):
        values = self.message.strip().split(self.separator)
        return ' '.join([value.strip() for value in values if value.strip().isdigit()])


sentence_to_parse = '8790: bonjour le monde:8987:7777:Hello World:    9007'

parsed_sentence = Parse(':', sentence_to_parse)
print(parsed_sentence)


"""
    OU BIEN
"""


class Parser:

    def __init__(self, separator, sentence):
        self.separator = separator
        self.parsed_line = list
        self.sentence = sentence

    def __parse(self):
        """
            '9007'.isdigit() renvoie False
            '9007'.isdigit() renvoie True
        """
        self.parsed_line = [
            i.strip() for i in self.sentence.split(self.separator) if i.strip().isdigit()
        ]

    """
        Le type de votre fonction spéciale __str__ doit être de type str
    """
    def __str__(self):
        self.__parse()

        return ' '.join(self.parsed_line)


parser_2 = Parser(':', sentence_to_parse)
print(parser_2)
