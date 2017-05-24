#S.McDonald 11/20/2016
#random_numbers
#This program creates a series of numbers in a file. This program allows to determine how many random numbers will be produced.
#The random numbers are in the range of 1-500

import random #to be used for generating random numbers

def main():
    try:
        #input
        #open the file for writing
        random_file = open('user_random.txt', 'w')


        #ask user to specify how many random numbers between 1 and 500
        for amt in range(int(input("Enter the amount of numbers you wish the file to hold: "))):
            line = str(random.randint(1, 500)) #number range between 1 and 500
            #write to an output file
            random_file.write(str(line) + '\n')
            print(line + '\n', end="")


        #close files
        random_file.close()

    #exceptions/else
    except FileNotFoundError:
        print("ERROR: FILE DOES NOT EXIST! CHECK FILE LOCATION!") #print if FileNotFoundError occurs

    except PermissionError:
        print("ERROR: FILE CANNOT BE CREATED IN THIS DIRECTORY! CHOOSE A DIFFERENT ONE!") #print if PermissionError occurs

    except ValueError:
        print("ERROR! YOU MUST ENTER AN INTEGER FOR THE AMOUNT OF RANDOM NUMBERS YOU WISH TO GENERATE!") #print if ValueError occurs

    except:
        print("ERROR! AND ERROR HAS OCCURED!") #print if any other error occurs

    else:
        print("\nYour random numbers have been saved to the file: user_random.txt") #else, print to user that their random numbers have been saved to a file


#call the main function
main()





