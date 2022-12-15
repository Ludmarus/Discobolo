#!/usr/bin/env python3
"""
Interface
"""

# pyinstaller --onefile --add-binary
# "sportsbetting\resources\chromedriver.exe;sportsbetting\resources" --add-data
# "sportsbetting\resources\teams.db;sportsbetting\resources" interface_pysimplegui.py --noconfirm
import collections
import json
import queue
import threading
import os
import sys
import time
from math import ceil

import PySimpleGUI as sg

import colorama
import termcolor
import sportsbetting as sb
from sportsbetting.auxiliary_functions import get_nb_outcomes, load_odds, save_odds
from sportsbetting.database_functions import get_all_competitions
from sportsbetting.user_functions import parse_competitions, get_sports_with_surebet, trj_match
from sportsbetting.interface_functions import (odds_table_combine,
                                               best_match_under_conditions_interface,
                                               best_match_freebet_interface,
                                               best_match_cashback_interface,
                                               best_matches_combine_interface,
                                               best_match_stakes_to_bet_interface,
                                               best_stakes_match_interface,
                                               best_matches_freebet_interface,
                                               best_match_pari_gagnant_interface,
                                               odds_match_interface, delete_odds_interface,
                                               delete_site_interface,
                                               get_current_competitions_interface,
                                               best_combine_reduit_interface,
                                               find_surebets_interface, odds_match_surebets_interface,
                                               find_values_interface, odds_match_values_interface,
                                               open_bookmaker_odds, find_perf_players, display_middle_info, search_perf,
                                               display_surebet_info, best_match_miles_interface, sort_middle_gap, sort_middle_trj,
                                               sort_middle_proba, get_best_conversion_rates_freebet, compute_odds, calculator_interface)

PATH_DATA = os.path.dirname(sb.__file__) + "/resources/data.json"
PATH_SITES = os.path.dirname(sb.__file__) + "/resources/sites.json"
PATH_COMPETITIONS = os.path.dirname(sb.__file__) + "/resources/competitions.json"
PATH_THEME = os.path.dirname(sb.__file__) + "/../theme.txt"

print(r"""
   _____                  __             __         __  __  _            
  / ___/____  ____  _____/ /______      / /_  ___  / /_/ /_(_)___  ____ _
  \__ \/ __ \/ __ \/ ___/ __/ ___/_____/ __ \/ _ \/ __/ __/ / __ \/ __ `/
 ___/ / /_/ / /_/ / /  / /_(__  )_____/ /_/ /  __/ /_/ /_/ / / / / /_/ / 
/____/ .___/\____/_/   \__/____/     /_.___/\___/\__/\__/_/_/ /_/\__, /  
    /_/                                                         /____/   
""")

try:
    sb.ODDS = load_odds(PATH_DATA)
except FileNotFoundError:
    pass

HEIGHT_FIELD_SIMPLE     = 10
HEIGHT_FIELD_GAGNANT    = 12
HEIGHT_FIELD_COMBINE    = 18
LENGTH_FIELD            = 160

sb.DB_MANAGEMENT = "--db" in sys.argv
nb_bookmakers = len(sb.BOOKMAKERS)


# All the stuff inside your window.
theme = "DarkBlue3"
if not os.path.exists(PATH_THEME):
    with open(PATH_THEME, "a+") as file:
        file.write(theme)
else:
    with open(PATH_THEME, "r") as file:
        theme = file.readlines()[0].strip()
sg.change_look_and_feel(theme)

sg.set_options(enable_treeview_869_patch=False)
parsing_layout = [
    [
        sg.Listbox(sb.SPORTS, size=(20, 6), key="SPORT", enable_events=True),
        sg.Column([[sg.Listbox((), size=(27, 12), key='COMPETITIONS', select_mode='multiple')],
                   [sg.Button("Tout désélectionner", key="SELECT_NONE_COMPETITION")],
                   [sg.Button("Compétitions actuelles", key="CURRENT_COMPETITIONS", visible=sb.DB_MANAGEMENT)],
                   [sg.Button("Sélectionner mes compétitions", key="MY_COMPETITIONS")],
                   [sg.Button("Sauver mes compétitions", key="SAVE_MY_COMPETITIONS")],
                   [sg.Button("Big 5", key="MAIN_COMPETITIONS", visible=False)]]),
        sg.Column([[sg.Listbox(sb.BOOKMAKERS_BOOST, size=(20, nb_bookmakers+1), key="SITES", select_mode='multiple')],
                   [sg.Button("Tout sélectionner", key="SELECT_ALL"), sg.Button("Tout désélectionner", key="SELECT_NONE_SITE")],
                   [sg.Button("Sélectionner mes sites", key="MY_SITES"), sg.Button("Sauvegarder mes sites", key="SAVE_MY_SITES")]])
    ],
    [sg.Text("", size=(100, 1), key="SUREBET_PARSING", visible=False)],
    [sg.Text("", size=(100, 1), key="HIGH_FREEBET_PARSING", visible=False)],
    [sg.Col([[sg.Button('Démarrer', key="START_PARSING")]]),
     sg.Col([[sg.Button('Récupérer tous les sports', key="START_ALL_PARSING")]]),
     sg.Col([[sg.Checkbox('Seulement football, basketball et tennis', key="PARTIAL_PARSING", default=True)]]),
     sg.Col([[sg.Button('Stop', key="STOP_PARSING", button_color=("white", "red"), visible=False)]]),
     sg.Col([[sg.ProgressBar(max_value=100, orientation='h', size=(20, 20), key='PROGRESS_PARSING',
                             visible=False)]]),
     sg.Col([[sg.Text("Initialisation de selenium en cours", key="TEXT_PARSING", visible=False)]]),
     sg.Col([[sg.Text("8:88:88", key="REMAINING_TIME_PARSING", visible=False)]])],
    [sg.Col([[sg.ProgressBar(max_value=100, orientation='v', size=(10, 20),
                             key="PROGRESS_{}_PARSING".format(site), visible=False)],
             [sg.Text(site, key="TEXT_{}_PARSING".format(site), visible=False)]],
            element_justification="center") for site in sb.BOOKMAKERS_BOOST]
]
