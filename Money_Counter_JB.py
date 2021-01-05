# This programme counts British coins based on their weight

# Started with dictionary of UK coin weights

coindict = {
    "1": 3.56,
    "2": 7.12,
    "5": 3.25,
    "10": 6.5,
    "20": 5.0,
    "50": 8.0
    }

while True:     # Put this eternal loop in so I don't have to keep restarting it

    print()     # Blank lines for aesthetics

    objective = input("\nWould you like to \n\n(a) weigh coins \nor \n(b) fill a coin bag?\n\n " ) # First choice: find the value of a batch of coins or fill a bag correctly?
        
    if objective == ("b"): # The fill a bag option
        
        bag=int(input("\n\nHow much does the bag take? In £: ")) # ASss for fill value printed on the bag
        
        choice = input("\n\nWhat coin denomination do you have in pence? (i.e. 20): ") # Asks for coin type
        singleweight = coindict.get(choice) # Used the key to set variable of coin weight using dictionary values
        filled = bag*100 # Got in a pickle trying to do this all in the line below so took it out and made a new variable
        weight = (((1 / int(choice)) * (singleweight))*filled) # The answer of how much weight of given coins fill a bag
        
        print("\n\nYou'll need " + str(weight) + " grams of " + (str(choice)) + "p pieces") # Answers in a sentence
        print("\n\n______________________________________________")

    else: 

        choice = input("\n\nWhich coins are you weighing? (Just the number, don't type 'p'): ") # Asked for input of coin type

        weight = int(input("\n\nHow many grams do they weigh in total? ")) #Asked for total batch weight. It's an int cos our scales don't do decimal grams

        singleweight = coindict.get(choice) # Used the key to set variable of coin weight using dictionary values 
        count = round(weight / singleweight) # Divided the total weight by the coin weight and rounded it (our scales don't do deicmial grams)
        value = ((count * int(choice))/100) #Times the coin value by number of coins
        value2d = "{:.2f}".format(value) #formats the total value to two decimal places for currency. Found this formatting solution here: http://bit.ly/3ogxk5V

        print("\n\nThere are " + (str(count)) + " X " + (str(choice)) + "p coins which makes £" + (str(value2d))) # Prints the results
        print("\n\n______________________________________________")