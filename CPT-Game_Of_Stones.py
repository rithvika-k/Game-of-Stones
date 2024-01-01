# Rithvika Kathroju
# 1/19/2021

# In order to generate random numbers for the number of stones the game starts with, who goes first, and the number of stones withdrawn by the computer; we have to import the random class. 
# This will allow us to use the randint function. I will also be using the choice function for the prize feature.
import random


# I defined a function that contains the main functionality of the stone game. 
# By creating a function to do this, it will help make my code easier to understand(fewer indents) and more visually appealing 
def game_of_stones():
    
    # I created a counter to keep track of the total number of rounds played
    # As i defined this variable inside the function I have to make it global so that i can use it outside of the function/throughout my program. 
    global total_rounds
    
    """
    Intializing variable as a counter by setting it equal to zero.  
    The counter keeps track of the total number of rounds played
    A series of conditions are checked(if the user wants to play and if the game did not end(if stones != 0 - no loser/winner declared) then the number of rounds will increment by 1 
    """
    total_rounds = 0
    
    # Starting the game. Includes the randomly generated num of stones, and the player that will go first
    # Subheading
    print("======================================================================================================")
    print("💎                                              𝐏𝐋𝐀𝐘                                              💎")
    print("======================================================================================================")
    print("Ready? Set! Go! Let The Game Begin!")
    print("------------------------------------------------------------------------------------------------------")
    
    
    # Generates a random number from 15-30 inclusive which will be the number of stones the players are going to play with for that round 
    current_stones = random.randint(15,30)
    # Prints out the number of stones that will be in the game. Used concantenation and typecasting as the variable is an integer. 
    print("💎 Number of Stones in the Game: " + str(current_stones))
    
    """
    Generates which user will go first - Randomly selected. First a random number is generated, either 1 or 2.
    It informs the players which number was generated, then a series of conditions will be checked. If it equals
    1 then player 1 goes first, and then a new variable called current_player will be set to "Player 1". This 
    variable will help us ensure that the correct player goes first, and that the right winner of the game is 
    correctly outputted in the future. If the random number generated is not 1, but 2 given the range then 
    player 2 will go first, and the current_player will be set to "Player 2"
    """
    # Initializing variable called starting_player to the random number generated. Used concantenation and typecasting for printing.
    starting_player = random.randint(1,2)
    print("\nLet's see who goes first with our random number generator!\n")
    print("A " + str(starting_player) + " was generated! Meaning that...")
    # If the random number generated is equal to 1 then player 1 will go first
    if starting_player == 1:
        print(player_1 + " will go first")
        # Initializing current player variable and setting it equal to player 1 as they will go first 
        current_player = "Player 1"
    # If the random number generated is not equal to 1, but equal to 2 then player 2 will go first
    else: 
        print(player_2 + " will go first")
        # Initializing current player variable and setting it equal to player 2 as they will go first 
        current_player = "Player 2"
        
        
    """
    #Functionality 

    First, the while loop will always execute indefinitely as i set the expression to evalaute to True. More specific conditions will be checked later in the loop. 
    After that, the interpretor will go through the first nested if-else statments and then execute the one that results to True. 
    
    The first if branch will execute if the current number of stones equals to 0, that means that the game is finished and we can declare a winner/loser. A nested
    if branch will check if current_player is equal to Player 1, if true, then player 1 wins and player 2 loses. (The current_player variable is re-defined later 
    on in my code - when "Player 2" was the last one to take the stone, current_player is redefined to "Player 1" so that player 1 can be declared the winner and 
    player 2 as the loser, NOT vice versa). The results will be printed based on the player that was forced to take the last stone, and then the winner will be allowed
    to win a prize. A nested ELSE branch will execute if current_player is equal to Player 2, instead of Player 1, if true, then player 2 wins and player 1 loses. 
    (The current_player variable is re-defined later on in my code - when "Player 1" was the last one to take the stone, current_player is redefined to "Player 2"
    so that player 2 can be declared the winner and player 1 as the loser, NOT vice versa). The results will be printed based on the player that was forced to take
    the last stone, and then winner will be allowed to win a prize.
    
    The else branch will execute if the current number of stones is NOT equal to 0, meaning that the game is NOT finished, and we CANNOT declare a winner/loser. The
    game will continue by executing nested if-else statments based on the value of current player as well as keep score of the total number of rounds. 
    --- If current player is equal to player 1 then player 1 will go first. Users will be prompted to enter in a value first, and if the value of current stones is still greater than 0 
    then player 2 will take its turn. If player 2 is Coco the Computer, random numbers will be generated for it, if player 2 is a friend then they will be prompted to enter a value. 
    Values generated or inputted that are invalid (greater then number of stones avalible or out of range) it will be informed to the player in which a new number will be inputted or generated. 
    The number of stones will be decremented and the current stones remaining will be printed. 
    --- If current player is NOT equal to player 1, meaning that it equals to player 2, then player 2 will go first. If player 2 is Coco the Computer, random numbers will be generated for it, 
    if player 2 is a friend then they will be prompted to enter a value. After player 2 takes its turn and the value of current stones is still greater than 0, Player 1 will be prompted to
    enter in a value. Values generated or inputted that are invalid (greater then number of stones avalible or out of range) will be informed to the players in which a new number will be 
    inputted or generated. The number of stones will be decremented and the number of stones remaining will be displayed. 
    """
    while True: 
        """
        The if conditional branch is executed if current stones equals to 0, this means that the game is over and a winner/loser have to be declared. In this branch the correct
        players will be informed that they won or lost the game, and then the winner will be able to win a prize, and a game summary will be printed. If current_player equals to 
        Player 1, then player will be informed that they won the game, and player 2 will be informed that they lost the game. As an additional, I added a prize feature which randomly 
        selects a prize from the prize list for player 1, the winner. Otherwise, if current_player does NOT equal to Player 1, that means that current_player must equal Player 2. 
        Player 2 will be informed that they won, and player 1 will be informed that they lost the game. As an additional, I added a prize feature which randomly selects a prize from
        the prize list for player 2, the winner. After either the if branch or the else branch is executed the interpreter will break out of the loop. 
        """
        if current_stones == 0:
            # Condition is checked, current_player is redefined from player 2 to player 1 later on in my code so if player 2 took the last stone, then this branch will be executed.
            if current_player == "Player 1":
                # Subheading
                print("======================================================================================================")
                print("💎                                             𝐑𝐄𝐒𝐔𝐋𝐓𝐒                                           💎")
                print("======================================================================================================")
                # Informs player 1 that they won, and player 2 that they lost. Used concantenation because using commas automatically inserts spaces :(
                print("👎 Sorry, " + player_2 + "! You lost the game because you took the last stone! Better luck next time!")
                print("🏆 Congratulations, " + player_1 + "! You won the game!")
                
                # Subheading
                print("======================================================================================================")
                print("💎                                              𝐏𝐑𝐈𝐙𝐄𝐒                                            💎")
                print("======================================================================================================")
                # Intializing a variable that stores a list of 4 different possible prizes the winner can win
                prizes_winner = ['$10 Tim Horton\'s Gift Card', 'Apple Watch SE', '$20 iTunes Gift Card', '$30 Amazon Gift Card']
                # Intializing a variable that stores the prize selected by the choice function in the random class. 
                # The choice method in the random class returns a randomly selected element from the specified sequence which in this case is the list, "prizes_winner"
                prize = random.choice(prizes_winner) 
                # Used concatenation to print out statements 
                print("As " + player_1 + " is the winner of this game, they will win a prize! Prize will be randomly selected!")
                print("***Prizes are Generating***")
                print("***Prize Generated and Selected***")
                input("***Press Enter to Display your prize!***")
                print("Winning Prize for " + player_1 + ": " + prize)
                
                # Subheading
                print("======================================================================================================")
                print("💎                                            𝐆𝐀𝐌𝐄 𝐒𝐔𝐌𝐌𝐀𝐑𝐘                                     💎")
                print("======================================================================================================")
                # Used concatenation and typecasting 
                print("Total Number of Rounds Played: " + str(total_rounds) + " Rounds")
                print("======================================================================================================")            
            
            # Condition is checked - if current_player does NOT equal to Player 1, that means that current_player must equal Player 2 - in which this branch is executed 
            # (Current_player is redefined from player 1 to player 2 later on in my code so if player 1 took the last stone, then this branch will be executed.)
            else:
                # Subheading
                print("======================================================================================================")
                print("💎                                             𝐑𝐄𝐒𝐔𝐋𝐓𝐒                                           💎")
                print("======================================================================================================")
                # Informs player 1 that they lost, and player 2 that they won. Used concantenation because using commas automatically inserts spaces :(
                print("👎 Sorry, " + player_1 + "! You lost the game because you took the last stone! Better luck next time!")
                print("🏆 Congratulations, " + player_2 + "! You won the game!")
                
                # Subheading
                print("======================================================================================================")
                print("💎                                              𝐏𝐑𝐈𝐙𝐄𝐒                                            💎")
                print("======================================================================================================")
                """
                The prize feature will go through an if-else statement to check if player 2 is Coco the Computer or not. Since Coco is a Computer it wouldn't make sense for it to be
                able to win a prize. If player 2 is not Coco the Computer, player 2(human) will be able to win a prize. Else, player 2 will not win a prize because this means that the 
                player is Coco the Computer 
                """ 
                if player_2 != "Coco the Computer":
                    # Prize feature which allows player 2, the winner in this condition, to win a random prize.
                    # Intializing a variable that stores a list of 4 different possible prizes the winner can win
                    prizes_winner = ['$10 Tim Horton\'s Gift Card', 'Apple Watch SE', '$20 iTunes Gift Card', '$30 Amazon Gift Card']
                    # Intializing a variable that stores the prize selected by the choice function in the random class. 
                    # The choice method in the random class returns a randomly selected element from the specified sequence which in this case is the list, "prizes_winner"
                    prize = random.choice(prizes_winner) 
                    # Used concatenation to print out statements
                    print("As " + player_2 + " is the winner of this game, they will win a prize! Prize will be randomly selected!")
                    print("***Prizes are Generating***")
                    print("***Prize Generated and Selected***")
                    input("***Press Enter to Display your prize!***")
                    print("Winning Prize for " + player_2 + ": " + prize)
                else:
                    print("Prizes were not awarded as Coco the Computer was the winner.")
                # Subheading
                print("======================================================================================================")
                print("💎                                            𝐆𝐀𝐌𝐄 𝐒𝐔𝐌𝐌𝐀𝐑𝐘                                     💎")
                print("======================================================================================================")
                # Used concatenation and typecasting 
                print("Total Number of Rounds Played: " + str(total_rounds) + " Rounds")
                print("======================================================================================================")     
                
            # A break statment is inserted here since we declared a winner - it can leave the loop as running it would no longer be necessary. This means that the game is finished 
            break

        # The else conditional branch is executed if current stones does NOT equal to 0, this means that the game is NOT over and winner/loser have NOT been declared. This means that 
        # the game SHOULD continue until a winner/loser IS declared - which is what this else branch does. In this branch the current round will be printed, and the player randomly 
        # choosen to go first will do so. Human players will be asked to enter a number from 1-3, representing the number of stones they wish to remove. In the case of Coco the Computer,
        # a random number between 1-3 will be generated. If the number is invaild, the player will be informed and then will be prompted to enter a vaild number. After each player takes 
        # out a specific number of stones, the current number of stones remaining will be printed. Once the current number of stones remaining equals 0, then current player will be 
        # re-defined to the opposite player so that when the interpretor goes back up to the loop the if branch will be executed and the correct winner/loser will be printed.
        else:
            print("------------------------------------------------------------------------------------------------------")
            # The counter for total_rounds will be incremented by 1 as the game/rounds are still continuing since current stones does NOT equal 0.  
            total_rounds += 1
            
            # Print the current round using concatenation and typcasting 
            print("✸✸✸✸✸✸✸✸")
            print("ROUND " + str(total_rounds))
            print("✸✸✸✸✸✸✸✸")
            
            
            """
            If current_player equals to Player 1, then player 1 will go first. They will be asked to take out 1,2, or 3 stones from the pile, if the value they entered is invalid they 
            will be asked again until the value IS valid. The current stones counter will be decremented, and current stones remaining will be printed. After player 1, player 2 will go. 
            If player 2 is Coco the Computer then a random number will be generated, if it is invaild it will continue to generate a number until the value is VALID. The current stones 
            counter will be decremented, and current stones remaining will be printed. If player 2 is NOT Coco the Computer, instead it is a friend/human, the same process that happened 
            for player 1 will take place for player 2. NOTE - The option of player 2 being a friend is an additional feature.
            """
            if current_player == "Player 1":
                
                # PLAYER 1
                # Intializing variable to allow player 1 to enter the number of stones they want to take out
                p1_choice = int(input(player_1 + ", How many stones do you want to take out? (1/2/3) : "))
                # The while loop will execute if the value they entered is greater then the number of stones avalible, or is greater than 3, or is less then/equal to 0 - then the player 
                # will be informed that it is an invalid entry. They will be prompted until they enter a valid number - in which it will break out of the loop as the condition will = false
                while ((p1_choice > current_stones) or (p1_choice > 3) or (p1_choice <= 0)):
                    print("Sorry, this is an invaild entry. Try again with a valid number!")
                    p1_choice = int(input(player_1 + ", How many stones do you want to take out? (1/2/3) : "))
                # Prints out the number of stones player 1 drew. Used concatenation and typecasting 
                print(player_1 + " just drew " + str(p1_choice) + " stones!")
                # current_stones will be decremented by the number of stones the user specified they wanted to take out
                current_stones = current_stones - p1_choice
                # Prints the remaining stones after player 1
                print(str(current_stones) + " stones remaining!\n")
                
                # PLAYER 2
                # After Player 1's turn we have to check if current_stones is equal to 0 or not. If current_stones is greater than 0 after player 1's turn, that means that the 
                # game is NOT over as there are still stones remaining, in which we need to continue the round and allow player 2 to take their turn. Otherwise, if current_stones is
                # equal to 0 that means that the game is over as there are no stones remaining, in which a winner/loser can be declared. As player 1 was the last one to take their turn, 
                # and if current_stones = 0, this means that player 1 took the last stone. This means that current player has to re-defined to the opposite player, so that when the 
                # interpreter goes back up to the loop to check if there is a winner/loser, the players that won and lost will be printed correctly. 
                if current_stones > 0:
                    # Player 2 can be Coco the Computer OR a friend (Human Player - which i added as an extra feature ...). We need to check if player 2 is a computer or if its a human/user.
                    # If player 2 is Coco the Computer then a number between 1-3 will be generated. If the number generated is greater than the number of stones available, then a new number 
                    # will be generated until it IS valid. Once a valid number has been generated, the players will be informed about how many stones player 2 removed and how many stones remain.  
                    if player_2 == "Coco the Computer":
                        # Initializing a variable to store the random number generated from 1-3 for Coco the Computer 
                        p2_choice = random.randint(1,3)
                        # While loop will check if the random number generated is greater than the number of stones remaining. If it is then a new number will be generated 
                        while (p2_choice > current_stones):
                            p2_choice = random.randint(1,3)
                        # Prints out the number of stones player 1 drew. Used concatenation and typecasting 
                        print("Coco the Computer just drew " + str(p2_choice) + " stones!")
                        # current_stones will be decremented by the number of stones the user specified they wanted to take out
                        current_stones = current_stones - p2_choice
                        # Prints the remaining stones after player 2
                        print(str(current_stones) + " stones remaining after round!")
                    # The else branch will execute if player 2 is NOT Coco the Computer, meaning that it is a human player. 
                    # The code in this branch logically functions the same as it would for player 1 
                    else:
                        # Intializing variable to allow player 2 to enter the number of stones they want to take out
                        p2_choice = int(input(player_2 + ", How many stones do you want to take out? (1/2/3) : "))
                        # The while loop will execute if the value they entered is greater then the number of stones avalible, or is greater than 3, or is less then/equal to 0 
                        # then the player will be informed that it is an invalid entry. They will be prompted until they enter a valid number - in which it will break out of
                        # the loop as the condition will equal false
                        while ((p2_choice > current_stones) or (p2_choice > 3) or (p2_choice <= 0)):
                            print("Sorry, this is an invaild entry. Try again with a valid number!")
                            p2_choice = int(input(player_2 + ", How many stones do you want to take out? (1/2/3) : "))
                        # Prints out the number of stones player 2 drew. Used concatenation and typecasting 
                        print(player_2 + " just drew " + str(p2_choice) + " stones!")
                        # current_stones will be decremented by the number of stones the user specified they wanted to take out
                        current_stones = current_stones - p2_choice
                        # Prints the remaining stones after player 2
                        print(str(current_stones) + " stones remaining!")
                # If current_stones IS equal to 0 that means that the game is over as there are no stones remaining, in which a winner/loser can be declared. As player 1 was the 
                # last one to take their turn, and if current_stones = 0, this means that player 1 took the last stone. This means that current player has to re-defined to the  
                # opposite player, so that when the interpreter goes back up to the loop to check if there is a winner/loser, the players that won and lost will be printed correctly. 
                else: 
                    # Re-defining 
                    current_player = "Player 2"
            
            # If current_player does NOT equal to Player 1, meaning that it must equal player 2, then player 2 will go first. We first need to check if player 2 is human/user or a computer. 
            # If player 2 is Coco the Computer then a random number will be generated, if it is invaild it will continue to generate a number until the value is VALID. The current stones 
            # counter will be decremented, and current stones remaining will be printed. If player 2 is NOT Coco the Computer, instead it is a friend/human, the same process that happened 
            # for player 1 will take place for player 2. NOTE - The option of player 2 being a friend is an additional feature. After player 2, player 1 will go. They will be asked to take 
            # out 1,2, or 3 stones from the pile, if the value they entered is invalid they will be asked again until the value IS valid. The current stones counter will be decremented, and 
            # current stones remaining will be printed. 
            else: 
                
                # PLAYER 2
                # Player 2 can be Coco the Computer OR a friend (Human Player - which i added as an extra feature ...). We need to check if player 2 is a computer or if its a human/user.
                # If player 2 is Coco the Computer then a number between 1-3 will be generated. If the number generated is greater than the number of stones available, then a new number 
                # will be generated until it IS valid. Once a valid number has been generated, the players will be informed about how many stones player 2 removed and how many stones remain.  
                if player_2 == "Coco the Computer":
                    # Initializing a variable to store the random number generated from 1-3 for Coco the Computer
                    p2_choice = random.randint(1,3)
                    # While loop will check if the random number generated is greater than the number of stones remaining. If it is then a new number will be generated 
                    while (p2_choice > current_stones):
                        p2_choice = random.randint(1,3)
                    # Prints out the number of stones player 1 drew. Used concatenation and typecasting
                    print("Coco the Computer just drew " + str(p2_choice) + " stones!")
                    # current_stones will be decremented by the number of stones the user specified they wanted to take out
                    current_stones = current_stones - p2_choice
                    # Prints the remaining stones after player 2
                    print(str(current_stones) + " stones remaining!\n")
                # The else branch will execute if player 2 is NOT Coco the Computer, meaning that it is a human player. 
                # The code in this else branch logically functions the same as it would for player 1 
                else:
                    # Intializing variable to allow player 2 to enter the number of stones they want to take out
                    p2_choice = int(input(player_2 + ", How many stones do you want to take out? (1/2/3) : "))
                    # The while loop will execute if the value they entered is greater then the number of stones avalible, or is greater than 3, or is less then/equal to 0 
                    # then the player will be informed that it is an invalid entry. They will be prompted until they enter a valid number - in which it will break out of
                    # the loop as the condition will equal false
                    while ((p2_choice > current_stones) or (p2_choice > 3) or (p2_choice <= 0)):
                        print("Sorry, this is an invaild entry. Try again with a valid number!")
                        p2_choice = int(input(player_2 + ", How many stones do you want to take out? (1/2/3) : "))
                    # Prints out the number of stones player 2 drew. Used concatenation and typecasting    
                    print(player_2 + " just drew " + str(p2_choice) + " stones!")
                    # current_stones will be decremented by the number of stones the user specified they wanted to take out
                    current_stones = current_stones - p2_choice
                    # Prints the remaining stones after player 2
                    print(str(current_stones) + " stones remaining!\n")
                
                # PLAYER 1
                # After Player 2's turn we have to check if current_stones is equal to 0 or not. If current_stones is greater than 0 after player 2's turn, that means that the 
                # game is NOT over as there are still stones remaining, in which we need to continue the round and allow player 1 to take their turn. Otherwise, if current_stones is
                # equal to 0 that means that the game is over as there are no stones remaining, in which a winner/loser can be declared. As player 2 was the last one to take their turn, 
                # and if current_stones = 0, this means that player 2 took the last stone. This means that current player has to re-defined to the opposite player, so that when the 
                # interpreter goes back up to the loop to check if there is a winner/loser, the players that won and lost will be printed correctly. 
                if current_stones > 0:
                    # Intializing variable to allow player 1 to enter the number of stones they want to take out
                    p1_choice = int(input(player_1 + ", How many stones do you want to take out? (1/2/3) : "))
                    # The while loop will execute if the value they entered is greater then the number of stones avalible, or is greater than 3, or is less then/equal to 0 - then the player 
                    # will be informed that it is an invalid entry. They will be prompted until they enter a valid number - in which it will break out of the loop as the condition will = false
                    while ((p1_choice > current_stones) or (p1_choice > 3) or (p1_choice <= 0)):
                        print("Sorry, this is not allowed.")
                        p1_choice = int(input(player_1 + ", How many stones do you want to take out? (1/2/3) : "))
                    # Prints out the number of stones player 1 drew. Used concatenation and typecasting 
                    print(player_1 + " just drew " + str(p1_choice) + " stones!")
                    # current_stones will be decremented by the number of stones the user specified they wanted to take out
                    current_stones = current_stones - p1_choice
                    # Prints the remaining stones after player 1
                    print(str(current_stones) + " remaining after round!\n")
                # If current_stones IS equal to 0 that means that the game is over as there are no stones remaining, in which a winner/loser can be declared. As player 2 was the 
                # last one to take their turn, and if current_stones = 0, this means that player 2 took the last stone. This means that current player has to re-defined to the  
                # opposite player, so that when the interpreter goes back up to the loop to check if there is a winner/loser, the players that won and lost will be printed correctly.
                else:
                    # Re-defining
                    current_player = "Player 1"
                
            # it will go back up to the loop to check if stones == 0 in which a winner/loser will declared 
            continue


# Introduction to the players 
# Heading
print("======================================================================================================")
print("💎 ✸ 💎 ✤ 💎 ♛ 💎 ✸ 💎 ✤ 💎 ♛ 💎 ✸ 💎 ✤ 💎 ♛ 💎 ✸ 💎 ✤ 💎 ♛ 💎 ✸ 💎 ✤ 💎 ♛ 💎 ✸ 💎 \n")
print("                                          𝐆𝐀𝐌𝐄 𝐎𝐅 𝐒𝐓𝐎𝐍𝐄𝐒\n")
print("💎 ✸ 💎 ✤ 💎 ♛ 💎 ✸ 💎 ✤ 💎 ♛ 💎 ✸ 💎 ✤ 💎 ♛ 💎 ✸ 💎 ✤ 💎 ♛ 💎 ✸ 💎 ✤ 💎 ♛ 💎 ✸ 💎 ")
print("======================================================================================================")

    
# Welcoming statement
print("Hello! Welcome to Game of Stones!")

# Asks the user if they would like to play the game. 
user_play = input("Would you like to play the game? ('Yes'/'No') : ")

# This while loop executes if the user wants to play the game. The condition is checked using a logical operator. 
while user_play == "Yes":
    # The if branch will only be executed if the user wants to play the game
    if user_play == "Yes":
        # Prints out game rules
        print("Since you want to play, here are the game rules!")
        # Subheading
        print("======================================================================================================")        
        print("💎                                          𝐆𝐀𝐌𝐄 𝐑𝐔𝐋𝐄𝐒                                           💎")
        print("======================================================================================================")        
        print("✸ The game starts with a random number of stones, ranging between 15 and 30.")
        print("✸ Two players alternate turns and on each turn may take out either 1, 2, or 3 stones")
        print("✸ The player forced to take the last stone loses, meaning that their opponent wins the game!")
        print("✸ GAME OBJECTIVE: Ensure that your opponent is forced to take the last remaining stone!")

        # Subheading
        print("======================================================================================================")        
        print("💎                                            𝐏𝐋𝐀𝐘𝐄𝐑𝐒                                             💎")
        print("======================================================================================================")
        # Asks the user if they want to play against Coco the Computer or a friend. These are the two options for player 2
        player_vs = int(input("Would you like to play against 'Coco the Computer' or a friend? \nEnter 0 for 'Coco the Computer' or 1 for friend: "))
        # Since player 1 is always going to be the same and has no options like player 2 does, the user will be asked to enter the name for the first player
        player_1 = input("Please enter the first player’s name: ")
        
        # This if-else code is for player 2. If the player 1 wants to play against Coco the Computer then player 2 will be hard coded to Coco the Computer
        # Else, we know the player wants to play with a friend in which they will be prompted to enter the name for the second player. 
        
        # If branch will be executed if user enters a 0 which means that they want to play against Coco the Computer
        if player_vs == 0:
            # Intialize player 2 to be Coco the Computer
            player_2 = "Coco the Computer"
            # Inform users who the players are 
            print("------------------------------------------------------------------------------------------------------")
            print("👥 Player 1: " + player_1)
            print("👥 Player 2: Coco the Computer")
            print("------------------------------------------------------------------------------------------------------")
            # Placed this input statement so that the user can read who the players are
            input("Press 'Enter' to continue: ") 
            
        # Else branch will be executed if the if branch is not executed. This only happens when the user enters 1 meaning that they want to play against a friend 
        else: 
            # User will be prompted to enter a name for the second player
            player_2 = input("Please enter the second player’s name: ")
            # Inform users who the players are
            print("------------------------------------------------------------------------------------------------------")
            print("👥 Player 1: " + player_1)
            print("👥 Player 2: " + player_2)
            print("------------------------------------------------------------------------------------------------------")
            # Placed this input statement so that the user can read who the players are
            input("Press 'Enter' to continue: ") 
            
            
        # Calling the function that stores the entire game functionality. This takes them through the start to the end of the game. 
        game_of_stones()

        # Asks the user if they would like to play again. If they say yes they will continue back up to the while loop where the game will be repeated. 
        # Else they will be exited out of the game
        print("------------------------------------------------------------------------------------------------------")
        user_play = input("Would you like to play again? ('Yes'/'No') : ")
        
        # If player wants to play again then it will continue back up to the while loop
        if user_play == "Yes":
            continue
        # Executed if the players don't want play again. They will answer a few questions, will be given a game summary, and will give a rating, it will then break out of the loop 
        else:
            # Subheading
            print("======================================================================================================")
            print("💎                                         𝐅𝐔𝐍 𝐐𝐔𝐄𝐒𝐓𝐈𝐎𝐍𝐍𝐀𝐈𝐑𝐄                                     💎")
            print("======================================================================================================")
            print("Everyone who plays our game is a winner! Feel positive by answering a few fun questions!")
            
            # Question 1 - Input + Response 
            q1 = input("Where would you like to travel for your dream vacation?: ")
            print("Wow! " + q1 + " is such a beautiful place! I would love to travel there!\n")
            # Question 2 - Input + Response
            q2 = input("What's your favourite animal?: ")
            print("I agree! " + q2 + " are awesome!\n")
            # Question 3 - Input + Response
            q3 = input("What's you favourite ice cream flavour?: ")
            print("Really! " + q3 + " is my favourite ice cream flavour too!\n")
            
            print("------------------------------------------------------------------------------------------------------")
            print("Players have exited the game! Thanks for playing!")
            # Allows the user to give a rating which is then stored in a variable 
            user_rating = int(input("Please rate our online card game from 1-5 stars: "))
            print("Thank you! Please give us a detailed feedback on our website at www.gameofstones.ca!")
            # Since the player no longer wants to play - the interpreter will break out of the loop
            break

# This if statment is if the user said that they don't want to play the game when they were first asked. Since the while loop does not check for this I had to create this if statement
if user_play == "No":
    print("Alright! Thanks for visiting our Game! Goodbye!")
    print("======================================================================================================")
