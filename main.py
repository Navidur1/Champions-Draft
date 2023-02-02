from flask import *
from classes import *
from functions import *
from scrape import *
from database import *
app = Flask(__name__, template_folder="/tmp")

users = {
    "Adam": {
        "Top": "Summit",
        "JG": "Closer",
        "Mid": "Maple",
        "ADC": "Prince",
        "Support": "Zven",
        "Bench": "Young"
    },
    "Navid": {
        "Top": "ssumday",
        "JG": "Pyosik",
        "Mid": "Haeri",
        "ADC": "FBI",
        "Support": "Vulcan",
        "Bench": "Contractz"
    }
}

@app.route('/', methods=['POST', 'GET'])
def hello():
    build_index()
    run_scrape()
    write_data()
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
    build_matchup_html(all_players, users, week)
    file_name = "matchups/week" + str(week) + ".html"
    return render_template(file_name)
  
if __name__ == "__main__":
    app.run()
