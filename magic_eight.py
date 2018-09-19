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




# Program start
def start():
    while True:
        question = ask_question()
        if check_question(question):
            break




