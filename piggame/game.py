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


""" This is the file game.py, it holds the essence of the gamee"""


import time
import random

from .player import Player
from .player import ComputerPlayer
from .die import Die


class PigGame:
    """This is the pig game"""

    def __init__(self):
        """creates a player list"""
        self._players = []

    @classmethod
    def pylint_passer(cls):
        """does nothing"""

    def run(self):
        """The game is being ran"""
        die_roll = Die()
        valid_input = False

        intro_message = (
            "Hello Player(s)!!\nAnd WELCOME "
            "TO YOUR IMPENDING DOOM!!!!..."
            "..\n.. Nah I'm just playing,"
            "we're gonna play some PIG!\n\n"
        )

        for i in intro_message:
            print(i, end="", flush=True)
            time.sleep(0.05)

        time.sleep(0.05)

        game_time = True

        while valid_input != game_time:

            player_prompt = "How many of you are playing (1 - 4)? "
            for i in player_prompt:
                print(i, end="", flush=True)
                time.sleep(0.05)

            num_players = int(input(""))

            if num_players > 4:
                print("That is too many players bucko! Try again >:(\n")
                continue
            if num_players < 0:
                print("That does not even make sense! Try again >:(\n")
                continue

            print("You entered:", num_players)
            valid_input = True

        for i in range(num_players):
            player_name = input("What is player {}'s name? ".format(i + 1))
            order = die_roll.roll()
            print("You rolled {},".format(order))
            self._players.append(Player(player_name, order))

        if num_players == 1:
            # add a computer player
            order = die_roll.roll()
            self._players.append(ComputerPlayer(order, self))

        print("\nBefore sorting", self._players)

        self._players.sort(key=lambda p: p.order)

        print("After sorting", self._players, "\n")

        current_index = 0
        roll_score = 0
        win_bound = 30
        roll_count = 0
        while True:
            curr_pl = self._players[current_index]
            if curr_pl._name == "Mr. Colloquial":
                pc_roll = "Here comes Mr. Colloquial!!!!\n"
                for i in pc_roll:
                    print(i, end="", flush=True)
                    time.sleep(0.05)
            else:
                print("{} is up!".format(curr_pl))
                roll_prompt = (
                    "Unfortunately you're gonna "
                    "have to roll automatically"
                    " \nso let me go ahead and do that for you :) \n"
                )
                for i in roll_prompt:
                    print(i, end="", flush=True)
                    time.sleep(0.05)

            rolled_number = die_roll.roll()

            print("You rolled {}".format(rolled_number))

            if rolled_number == 1:
                sorry_prompt = (
                    "I'm sorry buddy, I didn't mean it\nI"
                    " promise!.... Anywho next player!\n\n"
                )
                for i in sorry_prompt:
                    print(i, end="", flush=True)
                    time.sleep(0.05)
                roll_score = 0
                roll_count = 0
            elif curr_pl._name == "Mr. Colloquial":
                roll_count += 1
                roll_score += rolled_number

                if (roll_score + curr_pl._score) >= win_bound:
                    win_prompt = (
                        "NO WAY {} WOOOONNNN! YOU HAVE JUST"
                        " LOST TO THE BEST!"
                        "\nTO!!!\nWEENIE HUT JUNIORS!!!\n"
                        "YOU GO!!!!\n"
                        "His final score was {}\n\n".format(
                            curr_pl, (roll_score + curr_pl._score)
                        )
                    )
                    for i in win_prompt:
                        print(i, end="", flush=True)
                        time.sleep(0.05)
                    return 0

                comp_prompt = (
                    "Alrighttttt Mr. Colloquial!\nYour "
                    "current score is: {}"
                    "\nYour current roll score is: {}\nNumber of Rolls: {}\n"
                    "Do you want to roll again?\n\n".format(
                        curr_pl._score, roll_score, roll_count
                    )
                )
                for i in comp_prompt:
                    print(i, end="", flush=True)
                    time.sleep(0.05)

                comp_choice = random.randrange(1, 11)

                if comp_choice > 6:
                    comp_yes = "Yes! This fool is going down!\n\n"
                    for i in comp_yes:
                        print(i, end="", flush=True)
                        time.sleep(0.05)
                    continue
                if roll_count > 2:
                    comp_no = "Nah, it's all about technique o_O\n\n"
                    for i in comp_no:
                        print(i, end="", flush=True)
                        time.sleep(0.05)
                    curr_pl._score += roll_score
                    roll_score = 0
                    roll_count = 0
                else:
                    comp_yes = "Yes! This fool is going down!\n\n"
                    for i in comp_yes:
                        print(i, end="", flush=True)
                        time.sleep(0.05)
                    continue

            else:
                roll_score += rolled_number
                roll_count += 1

                if (roll_score + curr_pl._score) >= win_bound:
                    win_prompt = (
                        "NO WAY {}! YOU ARE THE WINNER\nCONGRATS!!!"
                        "\nFELICITATION!!!\nCOMPLIMENTI!!!!\n"
                        "Your final score was {}\n\n".format(
                            curr_pl, (roll_score + curr_pl._score)
                        )
                    )
                    for i in win_prompt:
                        print(i, end="", flush=True)
                        time.sleep(0.05)
                    return 0

                ask_prompt = (
                    "Heyyyyyy not too Shabby!\nYour current "
                    "score is: {}\nYour current roll score is: "
                    "{}\nNumber of rolls: {}\n"
                    "Wanna roll again (y/n): ".format(
                        curr_pl._score, roll_score, roll_count
                    )
                )
                for i in ask_prompt:
                    print(i, end="", flush=True)
                    time.sleep(0.05)

                prompt_ans = input("")

                if prompt_ans == "y":
                    no_play = False
                    play_on = False
                    while play_on == no_play:
                        rolled_number = die_roll.roll()
                        print("You rolled a {}".format(rolled_number))

                        if rolled_number == 1:
                            sorry_prompt = (
                                "Woof, that's rough! Say goodbye "
                                "to those points! Next!\n\n"
                            )
                            for i in sorry_prompt:
                                print(i, end="", flush=True)
                                time.sleep(0.05)
                            roll_score = 0
                            roll_count = 0
                            break

                        roll_score += rolled_number
                        roll_count += 1
                        if (roll_score + curr_pl._score) >= win_bound:
                            win_prompt = (
                                "NO WAY {}! YOU ARE THE WINNER\n"
                                "CONGRATS!!!\nFELICITATION!!!"
                                "\nCOMPLIMENTI!!!!"
                                "\nYour final score was {}\n\n".format(
                                    curr_pl, (roll_score + curr_pl._score)
                                )
                            )
                            for i in win_prompt:
                                print(i, end="", flush=True)
                                time.sleep(0.05)
                            return 0
                        ask_prompt = (
                            "Heyyyyyy not to Shabby!\n"
                            "Your current score is: {}"
                            " \nYour current roll score is: {}"
                            "\nNumber of rolls: {}"
                            "\n"
                            "Wanna roll again (y/n): ".format(
                                curr_pl._score, roll_score, roll_count
                            )
                        )
                        for i in ask_prompt:
                            print(i, end="", flush=True)
                            time.sleep(0.05)

                        prompt_q = input(" ")
                        if prompt_q == "y":
                            continue

                        no_play = True
                        no_prompt = "Wise choice player, Next!\n\n"
                        curr_pl._score += roll_score
                        roll_score = 0
                        roll_count = 0
                        for i in no_prompt:
                            print(i, end="", flush=True)
                            time.sleep(0.05)
                else:
                    no_prompt = "Wise choice player, Next!\n\n"
                    curr_pl._score += roll_score
                    roll_score = 0
                    roll_count = 0
                    for i in no_prompt:
                        print(i, end="", flush=True)
                        time.sleep(0.05)

            time.sleep(0.05)
            current_index = (current_index + 1) % len(self._players)
