from flask import *
from classes import *
from functions import *
from scrape import *
from database import *
import os

if not os.path.exists("/tmp/matchups"):
    os.makedirs("/tmp/matchups")

if not os.path.exists("/tmp/players"):
    os.makedirs("/tmp/players")

app = Flask(__name__, template_folder="/tmp")

build_index()
read_data()
run_scrape()
write_data()

@app.route('/', methods=['POST', 'GET'])
def hello():
    if request.method == "POST":
        run_scrape()
        write_data()
    return render_template('index.html')

@app.route('/players/week<int:week>')
def display_players(week):
    build_player_html(all_players, week)
    file_name = "players/week" + str(week) + ".html"
    return render_template(file_name)

@app.route('/matchups/week<int:week>')
def display_matchups(week):
    build_matchup_html(schedule, all_players, week)
    file_name = "matchups/week" + str(week) + ".html"
    return render_template(file_name)
  
if __name__ == "__main__":
    app.run()
