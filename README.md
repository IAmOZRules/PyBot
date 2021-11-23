# PyBot
A contextual chatbot written in Python using NLTK and PyTorch with a GUI created using Tkinter.

This chatbot has a Command Line Interface (CLI), and a Graphical User Interface (GUI), along with Voice Chat (Voice Input and Output).


| **Graphical User Interface**      | **Command Line Interface**      |
|------------|-------------|
|<img width="500" src="https://raw.githubusercontent.com/IAmOZRules/PyBot/master/images/gui.png?raw=true" />|<img width="500"  src="https://raw.githubusercontent.com/IAmOZRules/PyBot/master/images/cli.png?raw=true" />|

## Setup:
1. Clone the repository using ```git clone https://github.com/IAmOZRules/PyBot.git```
2. Navigate to the repository folder using ```cd PyBot```
3. Make sure all dependencies are installed.
 If not, run ```pip install -r requirements.txt```
4. Run ```python nltk_setup.py``` to install the required NLTK libraries.
5. And now you are good to go!

## Usage:

```
usage: python chatbot.py [-h] [options]

optional arguments:
  -h, --help            show this help message and exit
  -d, --verbose         Enable Verbose Mode in the ChatBot
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
python chatbot.py -t json/covid.json
python chatbot.py --train json/covid.json
```

- To run the chatbot in verbose mode:
```
python chatbot.py -d -c
python chatbot.py --verbose --cli
```

#### Sample Output for Verbose Mode:
```
You: Hello
PyBot: [greeting - (100.0%)] Hello! Nice to have you here!
```

### NOTE:
- Only ```json``` files are supported for intents.

## TODO:
- [x] Add a GUI ✅
- [x] Customize the Command Line Output ✅
- [x] Combine all tasks into a single CLI ✅
- [ ] Add support for training multiple intents at once ❌ (Seems dumb, not gonna do it)
- [x] Voice Input/Output ✅
- [x] Verbose Mode ✅

## Contributors
<table style="width: 100%" >
    <td align="center">
        <a href="https://github.com/IAmOZRules">
            <img src="https://avatars.githubusercontent.com/u/63207667?v=4" width="100px;" alt="IAmOZRules" />
            <br /><sub><b>Shreyaans Nahata</b></sub>
        </a>
        <br />
    </td>
    <td align="center">
        <a href="https://github.com/Siddharth-Gandhi">
            <img src="https://avatars.githubusercontent.com/u/61461606?v=4" width="100px;" alt="IAmOZRules" />
            <br /><sub><b>Siddharth Gandhi</b></sub>
        </a>
        <br />
    </td>
    <td align="center">
        <a href="https://github.com/SaiSridhar783">
            <img src="https://avatars.githubusercontent.com/u/58875230?v=4" width="100px;" alt="Sai" />
            <br /><sub><b>Sai Sridhar Akula</b></sub>
        </a>
        <br />
    </td>
</table>

#### This project is a major overhaul of the [Rude-ChatBot](https://github.com/IAmOZRules/Rude-Chatbot) Project.
