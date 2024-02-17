#Simple Quiz Game in Python
#text-based game that does not need to import any modules
#all lower case answer lol


#displaying a welcome to the quiz game
print("Are you a Naruto Expert?")
print("Lets find out!")
answer = input('Are you ready to play the quiz? (yes/no): ') #variable to store users response to beginning the quiz game
score = 0 #initializing score to 0 to start counting
#total_questions = 10 #number of questions total

if answer.lower() == 'yes':
    answer = input("Question 1: Which team number is Naruto in? (type the number in word) ")
    if answer.lower() == 'seven':
        score += 1 #earn 1 point added to the score variable if right answer is submitted
        print('Correct!')
    else:
        print('Wrong answer :(')
    
    answer = input("Question 2: Who is the fifth hokage of the Hidden Leaf village? ")
    if answer.lower() == 'tsunade':
        score+=1
        print('Correct!')
    else:
        print('Wrong answer :(')
    
    answer = input("Question 3: What is the color of Sakura's hair? " )
    if answer.lower() == 'pink':
        score+=1
        print('Correct!')
    else:
        print('Wrong again :(')
    
    answer = input("Question 4: What element is the chidori jutsu? ")
    if answer.lower() == 'lightning':
        score+=1
        print('Correct!')
    else:
        print('Wrong answer :(')
    
    answer = input("Question 5: Which clan is Sasuke from? ")
    if answer.lower() == 'uchiha':
        score+=1
        print("Correct!")
    else:
        print('Wrong answer :(')

    answer = input("Question 6: Who had the one-tail beast in him? ")
    if answer.lower() == 'gaara':
        score+=1
        print('Correct!')
    else:
        print('Wrong answer :(')

    answer = input("Question 7: Who is Sasuke's brother? ")
    if answer.lower() == 'itachi':
        score+=1
        print('Correct!')
    else:
        print('Wrong answer :(')
    
    answer = input("Question 8: Who is Team 7's mentor? ")
    if answer.lower() == 'kakashi':
        score += 1
        print('Correct!')
    else:
        print('Wrong answer :(')

    answer = input("Question 9: What is the name of the girl that was in the same team as Kakashi under Minato? ")
    if answer.lower() == 'rin':
        score+=1
        print('Correct!')
    else:
        print('Wrong answer :(') 

    answer = input("Question 10: Which clan possess the byakugan? ")
    if answer.lower() == 'hyuga':
        score += 1
        print('Correct!')
    else:
        print('Wrong answer :(')
    
    print("Thank you for playing the quiz, you attempted", score, "questions correctly!")
    if score == 10:
        print("You are a Naruto Expert!!!!!!")
    elif score >= 5:
        print("Very close to becoming an expert.")
    else:
        print("You are a beginner, but don't give up!")

#if answer is no...
print("BYE!")
    
