import argparse

import termcolor

arg_parser = argparse.ArgumentParser(usage='python chatbot.py [-h] [options]')
arg_parser.add_argument('-d', '--verbose', help='Enable Verbose Mode in the ChatBot', default=False, action='store_true')
arg_parser.add_argument('-g', '--gui', help='Open the ChatBot in GUI Mode', required=False, action='store_true')
arg_parser.add_argument('-c', '--cli', help='Open the ChatBot in CLI Mode', required=False, action='store_true')
arg_parser.add_argument('-v', '--voice', help='Open the ChatBot in Voice Chat Mode', required=False, action='store_true')
arg_parser.add_argument('-t', '--train', type=str, help='Train the ChatBot using a different Intents File', default=False, metavar='[intent]')

args = arg_parser.parse_args()


if __name__ == "__main__":
    if args.gui:
        from gui import ChatApplication
        app = ChatApplication()
        app.run()
    
    if args.cli:
        from chat import bot_name, get_response
        from common import *
        print(greeting)

        while True:
            print(you, end="")
            sentence = input()
            if sentence == "exit" or sentence == "goodbye":
                print(f'{bot_name}: Thank you for visiting! I hope to see you again!\n')
                break

            response, tag, prob = get_response(sentence)
            prob = round(prob, 4) * 100

            if args.verbose:
                tag = termcolor.colored(tag, 'magenta')
                prob = termcolor.colored(f'({prob}%)', 'yellow')
                print(f'{bot_name}: [{tag} - {prob}] {response}\n')
            else:
                print(f'{bot_name}: {response}\n')
    
    if args.voice:
        from voice import VoiceChat
        VoiceChat(args.verbose)

    if args.train:
        from train import trainModel
        trainModel(args.train)