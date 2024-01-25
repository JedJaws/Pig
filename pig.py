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


""" This is the file pig.py and it runs the whole program"""


from piggame import game
from piggame import __init__


if __name__ == "__main__":
    PIG = game.PigGame()
    PIG.run()
