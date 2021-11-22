import json
from chat import get_response
from prettytable import PrettyTable

with open('json/test.json') as json_file:
    data = json.load(json_file)

t = PrettyTable(["Question", "Actual Tag", "Predicted Tag", "Match Tag"])

for question in data:
    _, tag = get_response(question)
    t.add_row([question, data[question], tag, tag == data[question]])

print(t)
