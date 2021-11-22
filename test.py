import json

from nltk.util import pr
from chat import get_response
from prettytable import PrettyTable

with open('json/test.json') as json_file:
    data = json.load(json_file)

count = 0
t = PrettyTable(["Question", "Actual Tag", "Predicted Tag", "Match Tag"])

for question in data:
    _, tag = get_response(question)
    t.add_row([question, data[question], tag, tag == data[question]])

    if tag == data[question]:
        count += 1

print(f"\nAccuracy: {count/50 * 100}%\n")

print(t)
