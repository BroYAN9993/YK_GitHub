#!/usr/bin/python
# -*- coding:utf-8 -*-
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """
    A test for class AnonymousSurvey.
    """

    def test_store_single_response(self):
        """
        Test dose every single response can be stored properly。
        """
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)

unittest.main()
