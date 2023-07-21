# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, word_list):
        match_list = []
        sorted_self_word = sorted(self.word)
        for word in word_list:
            if sorted_self_word == sorted(word):
                match_list.append(word)
        print(match_list)
        return match_list