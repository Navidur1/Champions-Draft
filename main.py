import requests
from bs4 import BeautifulSoup
from flask import *
from classes import *
import json

app = Flask(__name__)

base_url = "https://gol.gg"
main_page_url = "https://gol.gg/tournament/tournament-matchlist/LCS%20Summer%202022/"
response = requests.get(main_page_url)
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
    game_response = requests.get(game_url)
    game_soup = BeautifulSoup(game_response.text, 'html.parser')
    game_table = game_soup.find(class_ = "completestats")

    current_scores = []
    #Name
    for name in game_table.contents[1].contents[1:]:
      name = name.text
      if name not in all_players:
        all_players[name] = Player(name)
        
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
      
@app.route('/')
def hello():
  return render_template('testing.html')

@app.route('/test')
def test():
  print("accessing testing data")
  with open("test.json", "r") as f:
    data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
  app.run("0.0.0.0", 5050)
