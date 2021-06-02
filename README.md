# PyBot
A contextual chatbot written in Python using NLTK and PyTorch with a GUI created using Tkinter.

This chatbot has a Command Line Interface (CLI), and a Graphical User Interface (GUI), along with Voice Chat (Voice Input and Output).


| **Graphical User Interface**      | **Command Line Interface**      |
|------------|-------------|
|<img width="500" src="https://raw.githubusercontent.com/IAmOZRules/PyBot/master/images/gui.png?raw=true" />|<img width="500"  src="https://raw.githubusercontent.com/IAmOZRules/PyBot/master/images/cli.png?raw=true" />|

## Setup:
1. Clone the repository using ```git clone https://github.com/IAmOZRules/PyBot.git```
2. Navigate to the repository folder using ```cd Rude-Chatbot```
3. Make sure all dependencies are installed.
 If not, run ```pip install -r requirements.txt```

## Usage:

```
usage: python chatbot.py [-h] [options]

optional arguments:
  -h, --help            show this help message and exit
  -g, --gui             Open the ChatBot in GUI Mode
  -c, --cli             Open the ChatBot in CLI Mode
  -v, --voice           Open the ChatBot in Voice Chat Mode
  -t [intent], --train [intent]
                        Train the ChatBot using a different Intents File
```

## Examples:
- To run the ChatBot in GUI Mode:
```
python chatbot.py -g
python chatbot.py --gui
```
- To run the ChatBot in CLI Mode:
```
python chatbot.py -c
python chatbot.py --cli
```
- To run the ChatBot in Voice Chat Mode:
```
python chatbot.py -v
python chatbot.py --voice
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
- [ ] Add support for training multiple intents at once ❌ (Seems dumb, not gonna do it)
- [x] Voice Input/Output ✅

#### This project is a major overhaul of the [Rude-ChatBot](https://github.com/IAmOZRules/Rude-Chatbot) Project.
