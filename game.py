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
    ZONENAME: 'Mr. Petrov - Lead Web Designer',
    DESCRIPTION: 'You stand in front of a bright red door, you can hear the buzzing sound of what appears to be bad 90\'s techno music playing on the other side.',
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
  print('# ' + zonemap[myPlayer.location][DESCRIPTION] + ' #\n')
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

def text_speech2(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.03)

def player_examine(action):
  if zonemap[myPlayer.location][SOLVED]:
    print('* A mysterious voice on the company loudspeaker yells *\nYou have already been through this door!! Why on earth would you ever want to go back?! Fool!!')
  elif zonemap[myPlayer.location][ZONENAME] == 'Mr. Petrov - Lead Web Designer':
    os.system('clear')
    petrov1 = '(AMBIANCE): uhn tis uhn tis uhn tis uhn tis\n'
    text_speech2(petrov1)
    petrov2 = 'Mr. Petrov: Yas! Yas! Come on innnnnn, recruit!\n'
    text_speech2(petrov2)
    petrov3 = 'Terrance: ' + 'Umm, hi there it\'s nice to mee-\n'
    text_speech2(petrov3)
    petrov4 = 'Mr. Petrov: Hold on comrade! Hold on...\n'
    text_speech2(petrov4)
    petrov5 = 'Mr. Petrov: Before I even shake your hand, answer me this...\n'
    text_speech2(petrov5)
    petrov6 = 'Mr. Petrov: ...do you...like-a de technaw?\n'
    text_speech2(petrov6)
    petrov7 = 'Terrance: ' + '...the technaw? Do you mean techn-\n'
    text_speech2(petrov7)
    petrov8 = 'Mr. Pretov: Yas comrade! Thee techNAWWWWWW!\n'
    text_speech2(petrov8)
    petrov9 = 'Terrance: ' + 'I mean sure, techno is...alright.\n'
    text_speech2(petrov9)
    petrov10 = 'Mr. Pretov: Alright? ALRIGHT?! No, no, no. This will not work. Recruit, how can you nawt love et huh? What else are you going to say next? That you are still using PNG in place of SVG for your site logos?!\n'
    text_speech2(petrov10)
    petrov11 = 'Mr. Pretov: Wait...I know almost nothing about your design skills, comrade. How about you riddle me this...if I have a wonderful high res photo of me and all my friends outside the best technaw club in San Francisco...which image format should this photo be saved as?\n'
    text_speech2(petrov11)
    answer = input('> JPG, PNG, SVG, GIF?...')
    if answer == 'JPG':
      zonemap[myPlayer.location][SOLVED] = True
      petrov12 = 'Mr. Pretov: HAAAAAYYYYY! Shots! Shots! Shots! Take a shot comrade, I knew you were a smart one!\n'
      text_speech2(petrov12)
    else: 'Mr. Pretov: That is wrong comrade...'
  else:
    print('You can trigger a puzzle here.')

def player_options(action):
  os.system('clear')
  print('These commands are available: "move", "knock", "quit"')

#### Game Functionality ####
def text_speech(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.03)

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
  # Build stats here

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