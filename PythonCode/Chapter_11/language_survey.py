#!/usr/bin/python
# -*- coding:utf-8 -*-

from survey import AnonymousSurvey

#Define a question, and creat an AnonymousSurvey object indicate survey
question = 'What language did you first learn to speak?'
my_survey = AnonymousSurvey(question)

#Show the survey and save response
my_survey.show_question()
print "Enter 'q' at any time to quit.\n"
while True:
    response = raw_input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

#Display the responses of survey
print "\nThank you to everyone who participated in the survey!"
my_survey.show_results()
