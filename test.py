from pyai import Brain, TTS 

brain = Brain() # you can also pass your own intents.json and function inside the Brain

while True:
  msg = input("Message : ")
  answer = brain.process_messages(msg)
  brain.pyai_say(answer)
  TTS(answer).say() # pass your comfortable voice either Male of female
