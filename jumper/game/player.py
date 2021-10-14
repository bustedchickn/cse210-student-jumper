

class Player:


    def __init__(self):
        #the player is able to have a memory
        self.memory = []

        pass


    def letter_pick(self):
        #picks a letter
        letter_choice = input()
        
        return letter_choice



    def letter_memory(self):
        """
        The player thinks of all the letters it has guessed because 
        they do not want to say the same letter twice and ruin their guess
        """
     
        choice = self.letter_pick()

        #if the letter has already been picked run into a conditional statement
        if choice in self.memory:

            #dont break while loop until new letter has been picked
            while choice in self.memory:

                print("wait I have already guessed that")
                print("Let me think of a new guess")
                choice = input()

                if choice not in self.memory:

                    self.memory.append(choice)
                    break

        else:

            self.memory.append(choice)
        #we only want to return the new value

        return choice

  



player = Player()
keep_play = input("Want to keep playing?")
while keep_play == 'y':
    print('pick a letter')
    print( player.letter_memory())
    



