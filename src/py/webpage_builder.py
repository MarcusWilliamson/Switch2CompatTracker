from jinja2 import Environment, FileSystemLoader
import json
from datetime import datetime

# Import json contents (game statuses)
with open("src/json/game_statuses.json") as file:
    statuses = json.load(file)

# Setting up jinja2 for writing to HTML using templates
env = Environment(loader=FileSystemLoader('src/templates/'))
template = env.get_template("template.html")

# Get current time
ct = datetime.now()
time_updated = str(ct)[0:16]

filename = "index.html"
with open(filename, mode='w', encoding='utf-8') as webpage:
    webpage.write(template.render(time_updated=time_updated, games = statuses))
    webpage.close()