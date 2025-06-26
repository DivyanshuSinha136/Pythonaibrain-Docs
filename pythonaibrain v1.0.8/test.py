from pyai import Brain

brain = Brain() # You can pass your own intents.json file and also function 
# Syntax
# Brain(intents= r'./intents.json', **function_mapping)

while True:
  msg = input('Message : ')
  answer = brain.process_messages(msg) # It's predict the message from the given intents.json file and return sutable answer for the asked question
  brain.pyai_say(answer) # It returns None
