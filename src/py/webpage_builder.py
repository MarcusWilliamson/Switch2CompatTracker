from jinja2 import Environment, FileSystemLoader
import json

# Import json contents (game statuses)
with open("../json/game_statuses.json") as file:
    statuses = json.load(file)

# Setting up jinja2 for writing to HTML using templates
env = Environment(loader=FileSystemLoader('../templates/'))
template = env.get_template("template.html")

filename = "test_out.html"
with open(filename, mode='w', encoding='utf-8') as webpage:
    webpage.write(template.render(games = statuses))