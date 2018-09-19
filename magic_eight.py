import sys
import random
# Ask user to input a question
def ask_question():
    question = input("What is your question? ")
    return question

# Check wether the input is a question
# param: question - string, input of the user
def check_question(question):
    if question.endswith("?"):
        return True
    else:
        print("I’m sorry, I can only answer questions.")
        return False

def add_questions():

    answers = random.randint(1,20)

    if answers == 1:
        print("It is certain.")

    elif answers == 2:
        print("It is decidedly so.")

    elif answers == 3:
        print("Without a doubt.")

    elif answers == 4:
        print("Yes - definitely.")

    elif answers == 5:
        print("You may rely on it.")

    elif answers == 6:
        print("As I see it, yes")

    elif answers == 7:
        print("Most likely.")

    elif answers == 8:
        print("Outlook good.")

    elif answers == 9:
        print("Yes.")

    elif answers == 10:
        print("Signs point to yes.")

    elif answers == 11:
        print(" Reply hazy, try again")

    elif answers == 12:
        print("Ask again later.")

    elif answers == 13:
        print("Better not tell you now.")

    elif answers == 14:
        print("Cannot predict now.")

    elif answers == 15:
        print("Concentrate and ask again.")

    elif answers == 16:
        print("Don't count on it.")

    elif answers == 17:
        print("My reply is no.")

    elif answers == 18:
        print("My sources say no.")

    elif answers == 19:
        print("Outlook not so good.")

    elif answers == 20:
        print("Very doubtful.")


	# Program start
def start():
    while True:
        question = ask_question()
        if check_question(question):
            break
    add_questions()

start()
