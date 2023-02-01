from flask import *
from classes import *
from functions import *
from scrape import *
import os

app = Flask(__name__, template_folder="/tmp")

if not os.path.exists("/tmp/matchups"):
    os.makedirs("/tmp/matchups")

if not os.path.exists("/tmp/players"):
    os.makedirs("/tmp/players")

run_scrape()
build_index()

@app.route('/', methods=['POST', 'GET'])
def hello():
    build_index()
    if request.method == "POST":
        run_scrape()
    return render_template('index.html')

@app.route('/players/week<int:week>')
def display_players(week):
    build_player_html(all_players, week)
    file_name = "players/week" + str(week) + ".html"
    return render_template(file_name)

@app.route('/matchups/week<int:week>')
def display_matchups(week):
    build_matchup_html(schedule, all_players, users, week)
    file_name = "matchups/week" + str(week) + ".html"
    return render_template(file_name)
  
if __name__ == "__main__":
    app.run()
