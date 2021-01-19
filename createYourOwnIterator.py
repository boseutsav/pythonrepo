
#
# def Sentence(instr):
#     for item in instr.split():
#         yield item


class Sentence:

    def __init__(self,sentence):
        self.sentence = sentence
        self.words =self.sentence.split()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index +=1
        return self.words[index]

my_sentence = Sentence('This is a sentence')

for word in my_sentence:
    print(word)