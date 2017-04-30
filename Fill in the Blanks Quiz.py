# Fill in the Blanks Quiz

# Blanks

blank = ["___1___", "___2___", "___3___", "___4___", "___5___"]

# Paragraphs

paragraph1 = '''There are seven continents on Earth. Do you know most 
of them? The continent that contains Canada is called ___1___. The 
continent that contains Brazil is ___2___. The continent that contains 
Egypt is called ___3___. The continent that contains Norway is called
___4___. The continent that contains Japan is called ___5___.'''

paragraph2 = '''There are four named oceans in the world. The one to
the immediate west of the United States is ___1___. The one to the east
is ___2___. The one south of India is called ___3___. The last ocean
that starts with the letter "A" and is really close to the North Pole 
is ___4___.'''

paragraph3 = '''Do you know the capitals of the world? The capital of 
the United Kingdom is ___1___. The capital of China is ___2___. The
capital of Australia is ___3___. Lastly, the capital of Russia is
___4___. Bonus question: what is the capital of Egypt is ___5___.'''

choosing_paragraph = [paragraph1, paragraph2, paragraph3]

# Answers

answers1 = ["North America", "South America", "Africa", "Europe", "Asia"]
answers2 = ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"]
answers3 = ["London", "Beijing", "Sydney", "Moscow", "Cairo"]

# Other texts

intro = '''Hello! Welcome to my quiz -- I will be giving you a few
paragraphs, and see if you are smart enough to fill in the answers 
correctly!'''

correct = "***Correct! Nice job!"
incorrect = "***Sorry... Try again!"

succeed = "Above is the complete paragraph! You got all of it correct! Amazing!"
quit_game = "Bye!"

#-------------------------------------------------------------------
# Functions

def choose_difficulty():
    ''' The inputs will be the difficulty; this function asks for the difficulty
    and then selects the right paragraph and answers to be the output to
    use in the play_game function.'''
    difficulty = raw_input("Choose difficulty (easy, medium, hard): ")
    '\n'
    if difficulty == "easy":
        return choosing_paragraph[0], answers1
    elif difficulty == "medium":
        return choosing_paragraph[1], answers2
    elif difficulty == "hard":
        return choosing_paragraph[2], answers3
    else:
        print quit_game

def play_game():
    ''' This uses the paragraph/answer (input) from the choose_difficulty
    function, and prints the corresponding paragraphs with the right answers.
    This asks what should go in blank as input, and if user input is correct,
    will go on the the next blank. Output is the paragraphs and correct/incorrect.'''
    paragraph, answer = choose_difficulty()
    i = 0 # counter
    n = 0 # blanks

    print "\n", paragraph, "\n"
    while n < len(answer): # depending on the amount of blanks, need to use length
        user_answer = raw_input("What should go in blank " + str(n+1) + "? ")
        if user_answer == answer[n]:
            i += 1
            if i == len(answer): # this happens when they filled all blanks correctly
                print correct
                paragraph = paragraph.replace(blank[n], user_answer)
                print "\n", paragraph, "\n"
                print succeed, "\n"
                break
            print correct
            paragraph = paragraph.replace(blank[n], user_answer)
            print "\n", paragraph, "\n"
            n += 1
        else:
            print incorrect #loops if user input is incorrect
    
def loop_game():
    ''' This is going to loop the game, input will be the the answer to
    if user wants to play again. Output is basically looping the game'''
    play_again = raw_input("Do you want to play again (yes or no)? ")
    "\n"
    if play_again == "yes":
        run_game()

def run_game():
    ''' This is the overall function, with just outputs the introduction and
    passes through the other functions for user to play the game.'''
    print "\n", intro, "\n"
    play_game()
    loop_game()

#-------------------------------------------------------------------
run_game()
    
