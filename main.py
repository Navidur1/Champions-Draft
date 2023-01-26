import requests
from bs4 import BeautifulSoup
from flask import *
from classes import *
from functions import *
import json
from google.cloud import firestore
import firebase_admin
from firebase_admin import firestore
import re

app = Flask(__name__)

APP_URL = "https://glassy-clock-375119.ue.r.appspot.com/"

base_url = "https://gol.gg"
main_page_url = "https://gol.gg/tournament/tournament-matchlist/LCS%20Summer%202022/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
response = requests.get(main_page_url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find_all(class_ = "table_list")
table = table[0].tbody.contents


all_players = {}

# for row in table:
#   contents = row.contents
#   week = contents[4].text
#   if week[:-1] == "WEEK":
#     week = int(week[-1])
#     game_url = base_url + str(contents[0].a['href'])[2:-5] + "fullstats/"
#     game_response = requests.get(game_url, headers=headers)
#     game_soup = BeautifulSoup(game_response.text, 'html.parser')
#     game_table = game_soup.find(class_ = "completestats")

#     current_scores = []
#     #Name
#     for name in game_table.contents[1].contents[1:]:
#       name = name.text
#       if name not in all_players:
#         all_players[name] = Player(name)
        
#       if all_players[name].scores[week] == None:
#         all_players[name].scores[week] = Score()
      
#       score = all_players[name].scores[week]
#       current_scores.append(score)

#     #Kills
#     for i in range(10):
#       kills = game_table.contents[4].contents[i+1].text
#       current_scores[i].kills += int(kills)

#     #Deaths
#     for i in range(10):
#       deaths = game_table.contents[5].contents[i+1].text
#       current_scores[i].deaths += int(deaths)

#     #Assists
#     for i in range(10):
#       assists = game_table.contents[6].contents[i+1].text
#       current_scores[i].assists += int(assists)

#     #CS
#     for i in range(10):
#       cs = game_table.contents[8].contents[i+1].text
#       current_scores[i].cs += int(cs)

#     #Triples
#     for i in range(10):
#       triples = game_table.contents[35].contents[i+1].text
#       current_scores[i].triples += int(triples)

#     #Quadras
#     for i in range(10):
#       quadras = game_table.contents[36].contents[i+1].text
#       current_scores[i].quadras += int(quadras)

#     #Pentas
#     for i in range(10):
#       pentas = game_table.contents[37].contents[i+1].text
#       current_scores[i].pentas += int(pentas)

#     #Update totals
#     for s in current_scores:
#       s.games += 1
#       s.update()




# # Application Default credentials are automatically created.
# app = firebase_admin.initialize_app() #https://firebase.google.com/docs/admin/setup#python_2 has info on users
# db = firestore.client()

# #convert string to unicode
# def to_uni(s:str):
#   return (re.sub('.', lambda x: r'\u % 04X' % ord(x.group()), s))

# #write info into database
# col_ref = db.collection(u'Players')
# for p in all_players:
#   player = all_players[p] #get player object

#   #convert name to unicode
#   uni_name = to_uni(p)
#   col_ref.document(uni_name).set({
#     u'name':uni_name,
#     u'team':to_uni(player.team)
    

#   })
#   break


# The `project` parameter is optional and represents which project the client
# will act on behalf of. If not supplied, the client falls back to the default
# project inferred from the environment.
# db = firestore.Client(project='my-project-id')

# for week in range(1, 9):
#   build_player_html(all_players, week)

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
