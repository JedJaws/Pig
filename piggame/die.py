#! /usr/bin/env python3
# Christian Verry
# CPSC 386-03
# 2022-03-01
# CJVerry@csu.fullerton.edu
# @JedJaws
#
# Lab 02-00
#
# This module is my very first game!
#


"""This is the file die.py, it only holds one small die function"""


import random


class Die:
    """This class creates a Die object for the pig game"""

    def __init__(self):
        pass

    @classmethod
    def roll(cls):
        """dummy doc string"""
        return random.randrange(1, 7)

    @classmethod
    def pylint_passer(cls):
        """does nothing"""
