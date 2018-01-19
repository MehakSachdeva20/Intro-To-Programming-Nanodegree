#Global Declaration is done in order to ensure that the code works properly
blanks = ["___1___", "___2___", "___3___", "___4___", "___5___"]

#Declaration of the paragraphs is done.User will select this in order to start the level.
level1_paragraph = '''Hello Friend . Welcome to the QUIZ SHOW .\nGreat !! You Have choosen the beginner level."\n"Your First Quiz is on Golden Temple.\n Here I begin.\nGolden Temple is situated in ___1___ in ___2___ in India.\nIt is popularly known as ___3___.\nIt is a place of ___4___ for everyone.\nIt is world's largest kitchen as food is served to thousands of people in form of ___5___'''
level2_paragraph = '''Hello Friend . Welcome to the QUIZ SHOW .\nGreat !! You Have choosen the MEDIUM level.\nYour SECOND  Quiz is on NEXUS 5X.\n Here I begin.\n Nexus 5x is an ___1___ smartphone which is approximately ___2___ (130mm)in height.\nIt supports the latest android version called ___3___.\nCurrently google is rolling out the android version ___4___ on nexus 5x.\nIts storage capacity is 16GB of ___5___'''
level3_paragraph = '''Hello Friend . Welcome to the QUIZ SHOW .\nGreat !! You Have choosen the HARD level.\nYour LAST  Quiz is on FACEBOOK.\n Here I begin.\nFacebook was launched on ___1___ February 2004 by ___2___.He is american ___3___ and the ___4___richest person in the world and is marrried to ___5___ Cha'''

#Answers are stored here in different lists as diiferent level exists.
level1_answer=["punjab", "amritsar", "harmindar sahab", "worship", "langar"]#using proper function names
level2_answer=["android", "5.2", "nougat", "7.1.2", "32"]
level3_answer=["4", "mark zukerberg", "programmer", "5", "priscilla"]

#Function is declared here so that user is asked to enter the name and the game may proceed.
def WELCOME_USER(player_name):
    print "WELCOME "+ player_name + ". Lets BEGIn here"

#User is asked to choose the level and in response to this corresponding level is displayed.
def get_choosing_difficulty(level):
    if level=="EASY" or level=="1":
        print "You choose the easy level\n"
 #returning is done here
        return level1_paragraph,level1_answer

    elif level=="MEDIUM" or level=="2": #if the user choose medium level then results corresponding to medium levels are displayed
        print "You choose the itermediate level\n"
        return level2_paragraph,level2_answer

    else:
        print "You Choose the Hard level\n"#if the user choose hard level then results corresponding to hard levels are displayed
        return level3_paragraph,level3_answer

#for every blank in blank array ,it is checked and if it is answer then it is replaced else none is returned 
def part1_QUIZ(word, blanks):
    for blank in blanks: 
           if blank in word: 
                return blank
    return None

#Functionality :-user input is check with the already stored answers
#input :- Asking the answer from the user
#Output :-if it is correct then it is replaced by the blank
def changing_the_answer(word, blanks, user_input, index):
    
    word=word.replace(blanks[index],user_input)#replacing is done here  . Replacing takes only place if the user enters correct answer.
    return word


#Funtionality:-here checking is done whether the user enters correct answer or not
#Input :- Name of the user is entered and the answer is enterd
#Output:- User name along with question and user answer is displayed.If ti is correct replaced by blank else it the user is asked to enter it again
def checking_answer(level, subdivision, answer):
    index=0
    for blank in blanks: 
        question="Enter your answer for "+blank+" "
        print question
        user_input=raw_input("Enter the answer ").lower() #if the user enter the answer in caps it is converted to lover case using lower()
        while user_input != answer[index]:#if the user enters wrong answer he is prompted to enter it again and if it is correct it is replaced
            print "YOU GOT IT WRONG"
            user_input = raw_input("Enter Once Again ").lower() 
        print "Corret"
        
        subdivision = subdivision.replace(blanks[index],user_input)#paragraph is replaced with the user input
        print subdivision
        index+=1;#index is incremented so that it can switch to next blank


#Functionality :-defining the game function so that the game could begin
#Input :- user name,level choosing is done here
#Output :- If the user enter correct answer it is replaced else user is prompted to enter the answer again
def play_game():
    
    player_name=raw_input("Enter your name ")#aking the name of the user
    WELCOME_USER(player_name)#Function is called here so that it can take input from the user
    level=raw_input("EASY - 1\nMEDIUM - 2\nHARD - 3\n")#inputting the level
    if level in ['1', '2', '3', 'EASY', 'MEDIUM', 'HARD']:
        paragraph, answer1 = get_choosing_difficulty(level)
        print paragraph
        checking_answer(level,paragraph,answer1)
        #user choice is asked here whether he wants to contine or quit the name
        choice = raw_input("You DID IT \nDo you want to play again? Yes/No").lower()
        if(choice=="yes"):#if the user wants to cintinue the game the starts again else the user comes out of the game
            play_game()#function call to start the game
        else:
            exit(0)#in order to end the game exit is used
        
    else:
        print "Chose appropriate level\n"
        play_game()

#Funtionality:-Game begins
play_game()
