import requests
from bs4 import BeautifulSoup
from flask import *
from classes import *
from functions import *
import json

app = Flask(__name__)

base_url = "https://gol.gg"
main_page_url = "https://gol.gg/tournament/tournament-matchlist/LCS%20Summer%202022/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
response = requests.get(main_page_url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find_all(class_ = "table_list")
table = table[0].tbody.contents

all_players = {}

for row in table:
  contents = row.contents
  week = contents[4].text
  if week[:-1] == "WEEK":
    week = int(week[-1])
    game_url = base_url + str(contents[0].a['href'])[2:-5] + "fullstats/"
    game_response = requests.get(game_url, headers=headers)
    game_soup = BeautifulSoup(game_response.text, 'html.parser')
    game_table = game_soup.find(class_ = "completestats")
    team_header = game_soup.find('h1').text.split("vs")
    team1 = team_header[0][:-1]
    team2 = team_header[1][1:]

    current_scores = []
    #Name
    for i in range(len(game_table.contents[1].contents[1:])):
      name = game_table.contents[1].contents[1:][i].text
      if name not in all_players:
        if i < 5:
          all_players[name] = Player(name, team1)

        else:
          all_players[name] = Player(name, team2)
        
      if all_players[name].scores[week] == None:
        all_players[name].scores[week] = Score()
      
      score = all_players[name].scores[week]
      current_scores.append(score)

    #Kills
    for i in range(10):
      kills = game_table.contents[4].contents[i+1].text
      current_scores[i].kills += int(kills)

    #Deaths
    for i in range(10):
      deaths = game_table.contents[5].contents[i+1].text
      current_scores[i].deaths += int(deaths)

    #Assists
    for i in range(10):
      assists = game_table.contents[6].contents[i+1].text
      current_scores[i].assists += int(assists)

    #CS
    for i in range(10):
      cs = game_table.contents[8].contents[i+1].text
      current_scores[i].cs += int(cs)

    #Triples
    for i in range(10):
      triples = game_table.contents[35].contents[i+1].text
      current_scores[i].triples += int(triples)

    #Quadras
    for i in range(10):
      quadras = game_table.contents[36].contents[i+1].text
      current_scores[i].quadras += int(quadras)

    #Pentas
    for i in range(10):
      pentas = game_table.contents[37].contents[i+1].text
      current_scores[i].pentas += int(pentas)

    #Update totals
    for s in current_scores:
      s.games += 1
      s.update()

build_index()

for week in range(1, 9):
  build_player_html(all_players, week)

# # Imports the Cloud Logging client library
# # import google.cloud.logging

# # Instantiates a client
# client = google.cloud.logging.Client()

# # Retrieves a Cloud Logging handler based on the environment
# # you're running in and integrates the handler with the
# # Python logging module. By default this captures all logs
# # at INFO level and higher
# client.setup_logging()

# def implicit():
#     from google.cloud import storage

#     # If you don't specify credentials when constructing the client, the
#     # client library will look for credentials in the environment.
#     storage_client = storage.Client()

#     # Make an authenticated API request
#     buckets = list(storage_client.list_buckets())
#     print(buckets)

@app.route('/')
def hello():
  return render_template('index.html')

@app.route('/week<int:week>')
def display_players(week):
  file_name = "week" + str(week) + ".html"
  return render_template(file_name)
  
if __name__ == "__main__":
  app.run("localhost", 5000)
