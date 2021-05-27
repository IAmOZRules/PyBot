# PyBot
A chatbot written in Python using NLTK and PyTorch with a GUI created using Tkinter.

This chatbot has a Command Line Interface (CLI), and a Graphical User Interface (GUI).


| **Graphical User Interface**      | **Command Line Interface**      |
|------------|-------------|
|<img width="500" src="https://raw.githubusercontent.com/IAmOZRules/PyBot/master/images/gui.png?raw=true" />|<img width="500"  src="https://raw.githubusercontent.com/IAmOZRules/PyBot/master/images/cli.png?raw=true" />|

## Setup:
1. Make sure ```pytorch```, ```numpy```, ```tkinter``` and ```nltk``` are installed.
> If not, run ```pip install tkinter torch numpy nltk torchvision```
2. Clone the repository using ```git clone https://github.com/IAmOZRules/PyBot.git```
3. Navigate to the repository folder using ```cd Rude-Chatbot```

## Usage:

```
python chatbot.py [-h] [-a [gui/cli]]

optional arguments:
  -h, --help     show this help message and exit
  -a , --app     [gui/cli] Open the ChatBot in GUI/CLI Mode
  -t , --train   Train the ChatBot using a different Intents File
```

## Examples:
- To run the ChatBot in GUI Mode:
```
python chatbot.py -a gui
python chatbot.py --app gui
```
- To run the ChatBot in CLI Mode:
```
python chatbot.py -a cli
python chatbot.py --app cli
```
- To train the ChatBot using a different Intent:
```
python chatbot.py -t intents.json
python chatbot.py --train intents.json
```

### NOTE:
- Only ```json``` files are supported for intents.

## TODO:
- [x] Add a GUI ✅
- [x] Customize the Command Line Output ✅
- [x] Combine all tasks into a single CLI ✅
- [ ] Add support for training multiple intents at once

## This project is a major overhaul of the similar project [Rude-ChatBot](https://github.com/IAmOZRules/Rude-Chatbot)
