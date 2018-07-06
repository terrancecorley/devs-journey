# Dev's Journey
# Terrance Corley

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

#### Player Setup ####
class player:
  def __init__(self):
    self.name = ''
    self.job = ''
    self.location = 'b2'
    self.game_over = False

myPlayer = player()

#### Title Screen ####
def title_screen_selections():
  option = input('> ')
  if option.lower() == ('play'):
    setup_game() 
  elif option.lower() == ('help'):
    help_menu()
  elif option.lower() == ('quit'):
    sys.exit()
  while option.lower() not in ['play', 'help', 'quit']:
    print('Please enter a valid command.')
    option = input('> ')  
    if option.lower() == ('play'):
      setup_game() 
    elif option.lower() == ('help'):
      help_menu()
    elif option.lower() == ('quit'):
      sys.exit()

def title_screen():
  os.system('clear')
  print('###############################')
  print('  # Welcome to Dev\'s Journey  ')
  print('###############################')
  print('            - Play -           ')
  print('            - Help -           ')
  print('            - Quit -           ')
  print('- Copyright 2017 Terrance Corley -')
  title_screen_selections()

def help_menu():
  print('###############################')
  print('  # Welcome to Dev\'s Journey  ')
  print('###############################')
  print('- Use commands up, down, left, right to move.')
  print('- Type your commands to execute them.')
  print('- Use command "knock" to inspect the doors.')
  print('- Good luck and have fun!')
  title_screen_selections()




#### Map ####

  """
 a1  a2  a3  a4
-----------------
|   |   |   |   | a1
-----------------
|   |   |   |   | b2
-----------------
|   |   |   |   | c3
-----------------
|   |   |   |   | d4
-----------------
  """

ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {
  'a1': False,
  'a2': False,
  'a3': False,
  'a4': False,
  'b1': False,
  'b2': False,
  'b3': False,
  'b4': False,
}

zonemap = {
  'a1': {
    ZONENAME: 'Town Market',
    DESCRIPTION: 'description',
    EXAMINATION: 'examine',
    SOLVED: False,
    UP: '',
    DOWN: 'b1',
    LEFT: '',
    RIGHT: 'a2',
  },
  'a2': {
    ZONENAME: 'Town Hall',
    DESCRIPTION: 'You enter the Heroes Town Hall.',
    EXAMINATION: 'examine',
    SOLVED: False,
    UP: '',
    DOWN: 'b2',
    LEFT: 'a1',
    RIGHT: 'a3',
  },
  'a3': {
    ZONENAME: 'Town Square',
    DESCRIPTION: 'description',
    EXAMINATION: 'examine',
    SOLVED: False,
    UP: '',
    DOWN: 'b3',
    LEFT: 'a2',
    RIGHT: 'a4',
  },
  'a4': {
    ZONENAME: 'Town Hall',
    DESCRIPTION: 'description',
    EXAMINATION: 'examine',
    SOLVED: False,
    UP: '',
    DOWN: 'b4',
    LEFT: 'a3',
    RIGHT: '',
  },
  'b1': {
    ZONENAME: '',
    DESCRIPTION: 'description',
    EXAMINATION: 'examine',
    SOLVED: False,
    UP: 'a1',
    DOWN: '',
    LEFT: '',
    RIGHT: 'b2',
  },
  'b2': {
    ZONENAME: 'Home',
    DESCRIPTION: 'This is your home.',
    EXAMINATION: 'Your home looks the same - nothing has changed.',
    SOLVED: False,
    UP: 'a2',
    DOWN: '',
    LEFT: 'b1',
    RIGHT: 'b3',
  },
  'b3': {
    ZONENAME: '',
    DESCRIPTION: 'description',
    EXAMINATION: 'examine',
    SOLVED: False,
    UP: 'a3',
    DOWN: '',
    LEFT: 'b2',
    RIGHT: 'b4',
  },
  'b4': {
    ZONENAME: '',
    DESCRIPTION: 'description',
    EXAMINATION: 'examine',
    SOLVED: False,
    UP: 'a4',
    DOWN: '',
    LEFT: 'b3',
    RIGHT: '',
  },
}

#### GAME INTERACTIVITY ####
def print_location():
  print('\n' + ('#' * (4 + len(myPlayer.location))))
  print('# ' + zonemap[myPlayer.location][ZONENAME].upper() + ' #')
  print('# ' + zonemap[myPlayer.location][DESCRIPTION] + ' #')
  print('\n' + ('#' * (4 + len(myPlayer.location))))

def new_line():
  print('\n')


def prompt():
  print('\n' + '============================')
  print('What would you like to do?')
  action = input('> ')
  acceptable_actions = [ 'move', 'go', 'travel', 'walk', 'examine', 'inspect', 'interact', 'knock', 'quit', 'exit', 'list', 'options'
  ]
  while action.lower() not in acceptable_actions:
    print('Unknown action, type "list" to see available actions.\n')
    action = input('> ')
  if action.lower() in ['quit', 'exit']:
    sys.exit()
  elif action.lower() in ['move', 'go', 'travel', 'walk']:
    player_move(action.lower())
  elif action.lower() in ['examine', 'inspect', 'interact', 'knock']:
    player_examine(action.lower())
  elif action.lower() in ['list', 'options']:
    player_options(action.lower())

def player_move_invalid(destination):
  if destination == '':
    input('That door does not exist, try again.')
    player_move('move')

def player_move(my_action):
  ask = 'Where would you like to move to?\n'
  dest = input(ask)
  if dest in ['up', 'north']:
    destination = zonemap[myPlayer.location][UP]
    player_move_invalid(destination)
    movement_handler(destination)
  elif dest in ['down', 'south']:
    destination = zonemap[myPlayer.location][DOWN]
    player_move_invalid(destination)
    movement_handler(destination)
  elif dest in ['left', 'west']:
    destination = zonemap[myPlayer.location][LEFT]
    player_move_invalid(destination)
    movement_handler(destination)
  elif dest in ['right', 'east']:
    destination = zonemap[myPlayer.location][RIGHT]
    player_move_invalid(destination)
    movement_handler(destination)

def movement_handler(destination):
  if destination != '':
    print('\n' + 'You have moved to the ' + destination + '.')
    myPlayer.location = destination
    print_location()

def player_examine(action):
  if zonemap[myPlayer.location][SOLVED]:
    print('* A mysterious voice on the company loudspeaker yells *\nYou have already been through this door!! Why on earth would you ever want to go back?! Fool!!')
  else:
    print('You can trigger a puzzle here.')

def player_options(action):
  os.system('clear')
  print('These commands are available: "move", "examine", "quit"')

#### Game Functionality ####
def text_speech(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    # time.sleep(0.03)

def enter_to_continue():
  input('> Press "Enter" to continue')
  os.system('clear')

def main_game_loop():
  while myPlayer.game_over is False:
    prompt()
    # here handle if puzzles solved, boss defeated, explored everything

def setup_game():
  os.system('clear')

  #### NAME COLLECTING ####
  question1 = 'Hello, what\'s your name?\n'
  text_speech(question1)
  player_name = input('> ')
  myPlayer.name = player_name

  #### JOB HANDLING ####
  question2 = 'What role would you like to play?\n'
  question2_added = '(You can play as a front-end developer, back-end developer, or web designer.)\n'
  text_speech(question2)
  text_speech(question2_added)
  player_job = input('> ')
  valid_jobs = ['front-end developer', 'back-end developer', 'web designer']
  if player_job.lower() in valid_jobs:
    myPlayer.job = player_job
  else:
    while player_job.lower not in valid_jobs:
      player_job = input('> ')
      if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
  
  #### PLAYER STATS ####
  if myPlayer.job is 'front-end developer':
    self.hp = 120
    self.mp = 20
  elif myPlayer.job is 'back-end developer':
    self.hp = 40
    self.mp = 120
  elif myPlayer.job is 'web designer':
    self.hp = 60
    self.mp = 60

  #### INTRODUCTION #### 
  myPlayer.name = player_name

  title1 = '#### Noogle HQ Lobby ####\n'
  speech1 = 'HR Lady: Welcome ' + player_name + '!\n'
  speech2 = 'We are really excited to have you interview with us today at Noogle!\n'
  speech3 = 'So just to recap, you will be having 8 interviews today and they will all be taking place on the 11th floor.\n'
  speech4 = 'If you will just follow me to the elevator we can get you started!\n' 
  speech5 = '#### Noogle 11th Floor ####\n'
  speech6 = 'Here we are!\n'
  speech7 = 'Okay, step on out now and get to it! Try not to get too lost now...'
  speech8 = 'Hehehehe...\n'
  

  os.system('clear')
  text_speech(title1)
  new_line()
  text_speech(speech1)
  text_speech(speech2)
  text_speech(speech3)
  text_speech(speech4)
  enter_to_continue()
  text_speech(speech5)
  new_line()
  text_speech(speech6)
  text_speech(speech7)
  text_speech(speech8)
  enter_to_continue()

  print('########################')
  print('#   Let\'s start now!  #')
  print('########################')
  main_game_loop()
  

title_screen()