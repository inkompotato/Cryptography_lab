from random import randint


# def read_file():
#     f = open("files/words.txt", "r")
#     return f.readlines()
#
#
# def random_word():
#     words = read_file()
#     random = randint(0, len(words))
#     return words[random].replace("\n", "").lower()


# random_word()

class Dictionary:
    wordarray = []

    def __init__(self):
        self.wordarray = self.read_file()

    def read_file(self):
        f = open("files/words.txt", "r")
        array = f.readlines()
        for i in range(0, len(array)):
            array[i] = array[i].replace("\n", "").lower()
        return array

    def random_word(self):
        random = randint(0, len(self.wordarray))
        return self.wordarray[random]

    def contains_word(self, word: str):
        return word.lower() in self.wordarray


