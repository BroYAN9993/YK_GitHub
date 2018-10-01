#!/usr/bin/python
# -*- coding:utf-8 -*-
class AnonymousSurvey():
    """
    Collect answers of anonymous survey
    """
    def __init__(self, question):
        """
        Save a question, and prepare for saving answers.
        """
        self.question = question
        self.responses = []

    def show_question(self):
        """
        Show the question.
        """
        print self.question

    def store_response(self, new_response):
        """
        Save a single response of question
        """
        self.responses.append(new_response)

    def show_results(self):
        """
        Show all of responses which we collected.
        """
        print 'Survey results:'
        for response in self.responses:
            print '- ' + response
