#!/usr/bin/python
# -*- coding:utf-8 -*-
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """
    A test for class AnonymousSurvey.
    """

    def setUp(self):
        """
        Creat a object of surey and a group of answers,
        for test methods use.
        """
        question = "What language did you first learn to speak?"
        self.my_survey =AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']


    def test_store_single_response(self):
        """
        Test dose every single response can be stored properly.
        """
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """
        Test did three responses can be stored properly.
        """
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()
