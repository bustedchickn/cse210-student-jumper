from faker import Faker



class Word:

    def __init__(self):
        
        fake = Faker()
        #the two attributes for word is the name and the length of that word
        self.guess_word = fake.name().split()[0]
        self.word_length = len(self.guess_word)

        
    def space_length(self):
        #create a string that will show how many letters are in the name
        tab_list = ''
        tab = '_'
        for _ in range(self.word_length):
            tab_list = tab_list +' '+ tab
            
        return tab_list

    def the_word(self):
        #returns the generated word

        return self.guess_word



word = Word()

print(word.space_length())
print(word.the_word())