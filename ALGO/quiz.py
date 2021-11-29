#1. Display the purpose of the program
#2. Display the instructions
#3. Ask the user a question
#4. What for the answer
#5. If user is correct, display "correct" and add 1 to the score
#6. Else display wrong
#7. Go back to step 3 until all the questions have been answered
#8. print the score of the user

print("This is a CodeLagos Quiz program written in Python.")
print("Each question carries one mark.")
print("Choose your answer by typing from the option a, b, c, d or the answer itself that the letter is holding. \n")

score = 0

print("1. How many out of school centers does codelagos have? \n")
print(" a. 4\n b. 12\n c. 21 \n d. 30 \n Type your answer below")
answer1 = input("= ")
if(answer1 == "c" or answer1 == "21"):
    score += 1
    print("Correct")
else:
    print("Wrong")

print("2. In what year did codelagos start? \n")
print(" a. 2017\n b. 2012\n c. 1999 \n d. 2018 \n Type your answer below")
answer2 = input("= ")
if(answer2 == "a" or answer2 == "2017"):
    score += 1
    print("Correct")
else:
    print("Wrong")
    
print("3. How many Lagoscians does codelagos intend to train by 2020? \n")
print(" a. 1,000,000\n b. 2,000,000\n c. 3,000,000 \n d. 4,000,000 \n Type your answer below")
answer3 = input("= ")
if(answer3 == "a" or answer3 == "1,000,000"):
    score += 1
    print("Correct")
else:
    print("Wrong")

print("Your score is "+str(score))
