import argparse

arg_parser = argparse.ArgumentParser(usage='python chatbot.py [-h] [-a [gui/cli]]')
arg_parser.add_argument('-a', '--app', type=str, help='[gui/cli] Open the ChatBot in GUI/CLI Mode', required=False, metavar='')
arg_parser.add_argument('-t', '--train', type=str, help='Train the ChatBot using a different Intents File', default=False, metavar='')

args = arg_parser.parse_args()


if __name__ == "__main__":
    if args.app == "gui":
        from gui import ChatApplication
        app = ChatApplication()
        app.run()
    
    if args.app == "cli":
        from termcolor import colored
        from chat import bot_name, get_response
        
        name = colored(bot_name, 'magenta', attrs=['bold'])
        bye = colored("'quit'", 'yellow')
        you = colored('You: ', "red", attrs=['bold'])
        bot_name = colored(bot_name, "cyan", attrs=["bold"])
        print(colored("\nHello, there! I am", "green"), name, colored("! Type", "green"), bye, colored("to stop chatting!\n", "green"))

        while True:
            print(you, end="")
            sentence = input()
            if sentence == "quit":
                break

            response = get_response(sentence)
            print(f'{bot_name}: {response}\n')

    if args.train:
        from train import trainModel
        trainModel(args.train)