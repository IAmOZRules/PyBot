from termcolor import colored
from chat import bot_name

bye = colored("'quit'", 'yellow')
you = colored('You: ', "red", attrs=['bold'])
bot_name = colored(bot_name, "cyan", attrs=["bold"])
greeting = colored("\nHello, there! I am ", "green")+ bot_name + colored("! Type ", "green") + bye + colored(" to stop chatting!\n", "green")