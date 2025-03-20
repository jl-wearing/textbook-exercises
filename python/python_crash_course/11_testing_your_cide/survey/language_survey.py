from survey import AnonymousSurvey

#Define a question, and make a survey.
question = "What is your favorite programming language?"
survey = AnonymousSurvey(question)

#Show the question, and store the responses to the question.
survey.show_question()

print("\nEnter 'q' at any time to quit: ")
while True:
    response = input('Language: ')
    if response == 'q':
        break
    survey.store_response(response)

#Show the survey results.
survey.show_results()