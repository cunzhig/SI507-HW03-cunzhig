
import sys
import random
# Ask user to input a question
def ask_question():
    question = input("What is your question?")
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

    answers = random.randint(1,8)

    if question == "":
        sys.exit()

    elif answers == 1:
        print "It is certain"

    elif answers == 2:
        print "Outlook good"

    elif answers == 3:
        print "You may rely on it"

    elif answers == 4:
        print "Ask again later"

    elif answers == 5:
        print "Concentrate and ask again"

    elif answers == 6:
        print "Reply hazy, try again"

    elif answers == 7:
        print "My reply is no"

    elif answers == 8:
        print "My sources say no"
    elif answers == 9:
        print "NO"

	# Program start
def start():
    while True:
        question = ask_question()
        if check_question(question):
            break
