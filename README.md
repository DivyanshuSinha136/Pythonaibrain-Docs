# PythonAIBrain
Make your first offline AI Assistant in python. No complex setup, No advance coding. No API key required. Just install configure and run!
## Installation
Install pythonaibrain package.
```bash
pip install pythonaibrain==1.0.8
```

## Modules
- Camera
- TTS
- PTT
- Context
- Brain
- Advance Brain

### Camera
PyAI supports Camera to click photos, make videos and scane QR and Bar Code, it can save photos or videos and also send Images and Videos to PyAI to take answer

#### Example
For start your camera
```python
# Import modules
import pyai
from pyai import Camera
import tkinter as tk
from tkinter import *

root = tk.Tk() # Create the GUI
Camera(root) # Call the Function and pass the master as root
root.mainloop() # Start GUI app
```
Or, 
```python
from pyai.Camera import Start
Start()
```

Or, 
``` python
from pyai import Brain

brain = Brain ()
brain.process_messages('Click Photo')
```

From this you can easly use camera in your program.

## TTS
TTS stands for **Text To Speech**, it convert text into both **Male** voice and **Female** voice.

### Example
``` python
# Import modules
import pyai
from pyai import TTS

tts = TTS(text = 'Hello World')
tts.say(voice= 'Male') # for male voice
tts.say(voice= 'Female') #for female voice
```

> tts.say() -> By default it takes Male voice
> tts.say(voice= 'Male') -> Pass the voice as Male
> tts.say(voice= 'Female') -> Pass the voice as Female

## PTT
PTT stands for **PDF To Text**, it can extract text from a given image

### Example
```python
# Import modules
import pyai
from pyai import PTT

ptt = PTT(path = 'example.pdf') # You can change example.jpeg from your file name
print(ppt) # PTT returns the text extract from the given pdf
```

### Syntax
```python
PTT(path: str = None)
```

Give your own file path.

## Context
It is a module in pyai which can able to extract answers from the give context

### Example
```python
# Import modules
import pyai
from pyai import Contexts

context = '''
Patanjali Ayurved is an Indian company. It was founded by Baba Ramdev and Acharya Balkrishna in 2006.
'''

question = 'Who founded Patanjali Ayurved?'
contexts = Contexts()
answer = contexts.ask(context= context, question= question)
```
Or, Also
```python
# Import modules
import pyai
from pyai import Contexts as contexts

context = '''
Patanjali Ayurved is an Indian company. It was founded by Baba Ramdev and Acharya Balkrishna in 2006.
'''

question = 'Who founded Patanjali Ayurved?'
answer = contexts.ask(context= context, question= question)
```

## Brain
It's a simple brain module which configure the input message.

### What it does
It classify the input message and find the type of message, like

- Question
- Answer
- Command
- Shutdown
- Make Directory
- Statement
- Name
- Know
- Start

It also extract the name, location, and age from the given message, by using NER.

#### Question
The Brain Module classify the given message weather it is a question or something else if answer then returns Question.

#### Answer
The Brain Module classify the given message weather it is a answer or something else if answer then returns Answer.

#### Command
The Brain Module classify the given message weather it is a command or something else if command then returns Command

#### Shutdown
The Brain Module also classify the given message weather the given command shutdown or not if it is then it shutdown your device and it returns Shutdown

But there are few issue releated to it :
- This command doesn't support website to run this command, because it need a terminal support.
- This doesn't run or work on Android, IOS.

#### Make Directory
The Brain Module also classify the given message weather the given command Make Directory or not if it is then it create a Directory on your device and returns Make Dir.

It generally comes under File handling of the PyAI Module which is also known as fh.

#### Statement
The Brain Module also classify the given message weather the given command statement or not, if it is then it statement then it returns Statement.

Statement -> It means a simple text which is not a question, answer, command, etc...  It a simple text. Like for example:
```text
The sun rises in the east.
```

#### Name
The Brain Module also classify the given message weather the given command name or not, if it is then it name then it returns Name.

Name -> It means the input message is caring name or specify the name like

```text
I'm Divyanshu.

Myself Divyanshu.

Divyanshu Sinha
```

#### Know
Know is similar to Statement.

```text
Do you know ___ ?
```
Like that.

#### Start
The Brain Module also classify the given message weather the given command start or not, if it is then it start any thing on your device and it returns Start.

Like:
```text
Start www.youtube.com
```
Or,
```text
Start Notepad
```

But it have issue:
- It doesn't works with website, because it support terminals like CMD for Window and etc.
- It also doesn't works in Android, IOS.

### How to create intents.json
You should know how to create a *intents.json* for run this **Brain Module**.

#### Pattern to create a *intents.json* file:
```json
{
    "intents":[{
        "tag": "greeting",
      "patterns": ["Hi", "Hello", "Hey", "What's up?", "Howdy", "Greetings", "Hi there", "Is anyone there?", "Yo!"],
      "responses": ["Hello! How can I help you today?", "Hey there!", "Hi! What can I do for you?"]
    },
    {
        "tag": "bye",
        "pattern": ["By", "See you soon", "See u soon", "Take care"],
        "responce":["Bye! have a greate day", "See you"]
    },
    ]
}
```
From this way you can create your own database.
> Remember this Database file in .json

### How to use **Brain Module**
To use **Brain Module** we should import Brain from **PyAI**

```python
from pyai import Brain
```

After importing the Module we use it in our main program as,

```python
brain = Brain(intents_path= 'intents.json') # Use can replace intents.json with you database file name but extention should be same (.json)

# Also Use
brain = Brain() # This will also work
```

After this, we predict the message type of we can say classify the message

```python
message = input('Message : ')
message_type = brain.predict_message_type(message= message) # On using predict_message_type() function we get the type of message is (question, answer, statement, command, shutdown, make directory, name, know, etc...)
```
By gating the message type, we find the perfect answer for the message
```python
if message_type in ['Question', 'Answer']:
    print(f'Answer : {brain.process_messages(message = message)}')

```
From these things you can create your own AI Assistant. But this is basic.

For Advance we can use Advance Brain Module.
### Advance Brain
This is advance version of **Brain Module**
It work like Brain but smartly.

### What it does
It classify the input message and find the type of message, like

- Question
- Answer
- Command
- Shutdown
- Make Directory
- Statement
- Name
- Know
- Start

It also extract the name, location, and age from the given message, by using NER.

#### Question
The Brain Module classify the given message weather it is a question or something else if answer then returns Question.

#### Answer
The Brain Module classify the given message weather it is a answer or something else if answer then returns Answer.

#### Command
The Brain Module classify the given message weather it is a command or something else if command then returns Command

#### Shutdown
The Brain Module also classify the given message weather the given command shutdown or not if it is then it shutdown your device and it returns Shutdown

But there are few issue releated to it :
- This command doesn't support website to run this command, because it need a terminal support.
- This doesn't run or work on Android, IOS.

#### Make Directory
The Brain Module also classify the given message weather the given command Make Directory or not if it is then it create a Directory on your device and returns Make Dir.

It generally comes under File handling of the PyAI Module which is also known as fh.

#### Statement
The Brain Module also classify the given message weather the given command statement or not, if it is then it statement then it returns Statement.

Statement -> It means a simple text which is not a question, answer, command, etc...  It a simple text. Like for example:
```text
The sun rises in the east.
```

#### Name
The Brain Module also classify the given message weather the given command name or not, if it is then it name then it returns Name.

Name -> It means the input message is caring name or specify the name like

```text
I'm Divyanshu.

Myself Divyanshu.

Divyanshu Sinha
```

#### Know
Know is similar to Statement.

```text
Do you know ___ ?
```
Like that.

#### Start
The Brain Module also classify the given message weather the given command start or not, if it is then it start any thing on your device and it returns Start.

Like:
```text
Start www.youtube.com
```
Or,
```text
Start Notepad
```

But it have issue:
- It doesn't works with website, because it support terminals like CMD for Window and etc.
- It also doesn't works in Android, IOS.

### How to create intents.json
You should know how to create a *intents.json* for run this **Advance Brain Module**.

#### Pattern to create a *intents.json* file:
```json
{
    "intents":[{
        "tag": "greeting",
      "patterns": ["Hi", "Hello", "Hey", "What's up?", "Howdy", "Greetings", "Hi there", "Is anyone there?", "Yo!"],
      "responses": ["Hello! How can I help you today?", "Hey there!", "Hi! What can I do for you?"]
    },
    {
        "tag": "bye",
        "pattern": ["By", "See you soon", "See u soon", "Take care"],
        "responce":["Bye! have a greate day", "See you"]
    },
    ]
}
```
From this way you can create your own database.
> Remember this Database file in .json

## How to use **Advance Brain Module**
To use **Advance Brain Module** we should import Brain from **PyAI**

```python
from pyai import AdvanceBrain
```

After importing the Module we use it in our main program as,

```python
advance_brain = AdvanceBrain(intents_path= 'intents.json') # Use can replace intents.json with you database file name but extention should be same (.json)

# Also
advance_brain = AdvanceBrain() # This also work
```

After this, we predict the message type of we can say classify the message

```python
message = input('Message : ')
message_type = advance_brain.predict_message_type(message= message) # On using predict_message_type() function we get the type of message is (question, answer, statement, command, shutdown, make directory, name, know, etc...)
```
By gating the message type, we find the perfect answer for the message
```python
if message_type in ['Question', 'Answer']:
    print(f'Answer : {advance_brain.process_messages(message = message)}')

```

## Python AI Modules and their use
| Module Name | Description |
| :---: | :---:|
|Brain| It is use to create Brain for AI by passing **.json** file (or, **Knowledge for Brain**)|
|AdvanceBrain|It is use to create Advance Brain for AI by passing **.json** file (or, **Knowledge for Brain**). It can understand better than Brain|
|TTS|Convert text into Voice|
|PTT|PDF into Text|
|Camera|Use camera to click photos and make videos|
|Context|Get Answer from the context for the respective question|



## PythonAI Brain also provides built-in AI Assistant
If you don't want to create your own AI assistant by coding or you want to see how this modules work you can also use PyBrain which is a built-in python AI assistance, provided by pythonaibrain == 1.0.8

### How to use it
```python
import PyBrain
PyBrain.App('-g')
```

By using this you can use PyBrain in GUI.

Or,
```python
import PyBrain
PyBrain.app.run(debug= False)
```

Or,
```python
from PyBrain import Server
server = Server()
server.run()
```
By using this you can use PyBrain in Web.

---
### Visit [PyPI](https://pypi.org/project/pythonaibrain/1.0.8) for installation.
