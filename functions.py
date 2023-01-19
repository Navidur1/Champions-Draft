#build html based on pulled player data
from classes import *
from bs4 import BeautifulSoup
from bs4.formatter import *

def build_player_html(all_players:dict, week):
    file_name = "templates/week" + str(week) + ".html"
    file_html = open(file_name,"w")

    text = """<!DOCTYPE html>
            <html>
            <style>
            table, th, td {
            border:1px solid black;
            }
            </style>
            <body>

            <h2>LCS Players</h2>

            <table style="width:100%">
                <tr>
                    <a href="http://localhost:5000/week1">Week 1</a>
                    <a href="http://localhost:5000/week2">Week 2</a>
                    <a href="http://localhost:5000/week3">Week 3</a>
                    <a href="http://localhost:5000/week4">Week 4</a>
                    <a href="http://localhost:5000/week5">Week 5</a>
                    <a href="http://localhost:5000/week6">Week 6</a>
                    <a href="http://localhost:5000/week7">Week 7</a>
                    <a href="http://localhost:5000/week8">Week 8</a>
                </tr>
            </table>

            <table style="width:100%">
                <tr>
                    <th>Name</th>
                    <th>Team</th>
                    <th>Kills</th>
                    <th>Deaths</th>
                    <th>Assists</th>
                    <th>Triples</th>
                    <th>Quadras</th>
                    <th>Pentas</th>
                    <th>CS</th>
                    <th>Total</th>
                    <th>Games</th>
                </tr>"""
    
    for p in all_players:      
        player = all_players[p]
        score = player.scores[week]
        
        if(score == None):
            continue

        line = "<tr><th>" \
        + p + "</th><th>" \
        + "Men" + "</th><th>" \
        + str(score.kills) + "</th><th>" \
        + str(score.deaths) + "</th><th>" \
        + str(score.assists) + "</th><th>" \
        + str(score.triples) + "</th><th>" \
        + str(score.quadras) + "</th><th>" \
        + str(score.pentas) + "</th><th>" \
        + str(score.cs) + "</th><th>" \
        + str(score.total) + "</th><th>" \
        + str(score.games) + "</th><tr>"
        text += line

    text += """ 
            </table>
            </body>
            </html>"""

    soup = BeautifulSoup(text, 'html.parser')
    formatter = HTMLFormatter(indent=4)
    soup_str = str(soup.prettify(formatter=formatter))
    file_html.write(soup_str)
    file_html.close()