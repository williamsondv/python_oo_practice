import random
"""Word Finder: finds random words from a dictionary."""



class WordFinder:
    """Class to create a randomly generated word from a text file of words."""
    def __init__(self, file_path):
       self.word_lst =  []
       self.read_file(file_path)

    def read_file(self,file_path):
        words = 0
        file = open(file_path)
        self.word_lst = file.read().splitlines()
        words = len(self.word_lst)
        print(f"{words} words read")

    def random(self):
        word_num = len(self.word_lst)
        random_num = random.randint(0, word_num-1)
        return self.word_lst[random_num]


class SpecialWordFinder(WordFinder):
    """Class to create a randomly generated word from a text file of words."""
    

    def random(self):
        """returns a random word that does not begin with "#" and is not an empty string"""
        modified_lst = [w for w in self.word_lst if not w.startswith("#") and not w == ""]
        word_num = len(modified_lst)
        random_num = random.randint(0, word_num-1)
        word = modified_lst[random_num]
        return word
        
                
        
