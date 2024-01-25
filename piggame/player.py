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


""" player and computer objects"""


class Player:
    """This is the player class used in game"""

    def __init__(self, name, order):
        self._name = name
        self._score = 0
        self._order = order

    @property
    def name(self):
        """name for player"""
        return self._name

    @property
    def order(self):
        """players' order"""
        return self._order

    @property
    def score(self):
        """players' score"""
        return self._score

    @score.setter
    def score(self, new_score):
        """game calls _score"""
        self._score = new_score

    @classmethod
    def roll_again(cls):
        """true to roll"""
        return True

    def __repr__(self):
        """how player is represented"""
        return 'Player("{}, {}")'.format(self._name, self._order)

    def __str__(self):
        """type for name"""
        return self._name


class ComputerPlayer(Player):

    """This is the computer player"""

    def __init__(self, order, game):
        """Takes style of the player class"""
        super().__init__("Mr. Colloquial", order)
        self._game = game
