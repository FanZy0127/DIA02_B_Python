class Message:

    def __init__(self, message):
        self.message = message

    def __contains__(self, word):

        assert len(self.message) > 0

        return word in self.message


class FormatedMessage(Message):
  
    def __contains__(self, word):

        assert len(self.message) > 0

        return word.lower() in self.message.lower()


m = Message("Bonjour tout le monde")

print("Bonjour" in m)
print("bonjour" in m)

f_m = FormatedMessage("Bonjour tout le monde")

print("Bonjour" in f_m)
print("bonjour" in f_m)
