#build html based on pulled player data
from classes import *
from bs4 import BeautifulSoup
from bs4.formatter import *

def build_index():
    file_name = "/tmp/index.html"
    file_html = open(file_name, "w+")

    text = """<!DOCTYPE html>
            <html>
                <head>
                    <title>League Fantasy</title>
                </head>
                <body>
                    <table style="width:100%">
                        <tr>"""
            
    for i in range(6):
        text +="<a href="+"/players/week"+str(i+1)+">Week "+str(i+1)+"</a>"
    text +="""
                    </tr>
                </table>
            </body>
        </html>"""
        
    soup = BeautifulSoup(text, 'html.parser')
    formatter = HTMLFormatter(indent=4)
    soup_str = str(soup.prettify(formatter=formatter))
    file_html.write(soup_str)
    file_html.close()

def build_player_html(all_players:dict, week):
    file_name = "/tmp/players/week" + str(week) + ".html"
    file_html = open(file_name, "w+")

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
"""
    
    for i in range(6):
        text+="<a href="+"/players/week"+str(i+1)+">Week "+str(i+1)+"</a>"
    text+="""
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
        + player.team + "</th><th>" \
        + str(score.kills) + "</th><th>" \
        + str(score.deaths) + "</th><th>" \
        + str(score.assists) + "</th><th>" \
        + str(score.triples) + "</th><th>" \
        + str(score.quadras) + "</th><th>" \
        + str(score.pentas) + "</th><th>" \
        + str(score.cs) + "</th><th>" \
        + str(score.total) + "</th><th>" \
        + str(score.games) + "</th></tr>"
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

def build_matchup_html(schedule, all_players:dict, users:dict, week):
    file_name = "tmp/matchups/week" + str(week) + ".html"
    file_html = open(file_name, "w+")
    total = 0
    matchups = schedule[week]

    text = """<!DOCTYPE html>
            <html>
            <head>
            <style>
                .matchup-container {
                display: flex;
                align-items: center;
                justify-content: center;
                flex-wrap: wrap;
                }
                .matchup {
                display: flex;
                flex-wrap: wrap;
                }
                .team {
                width: 900px;
                padding: 20px;
                text-align: center;
                }
                .team img {
                width: 80px;
                height: 80px;
                }
                .team h3 {
                margin-top: 10px;
                font-size: 1.5em;
                }
                .players {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                }
                .player {
                width: 750px;
                margin: 10px;
                text-align: center;
                }
                .player h4 {
                margin-top: 10px;
                }
                .player span {
                font-weight: bold;
                }
                .team-score {
                margin: 20px 0;
                }
                .team-score h4 {
                text-align: center;
                }
                .table {
                width: 100%;
                border-spacing: 20px;
                }
            </style>
            </head>
            <body>
            <div class="matchup-container">
"""
    for i in range(3):
        #Player 1
        user1 = matchups.matches[i][0]
        user2 = matchups.matches[i][1]

        text += """
                <div class="matchup">
                <div class="team team-one">
                <h3>"""
        text += user1.name
        text += """</h3>
                <div class ="players">
                <table class="table">
    """
        text += """<tr>
                    <th>Role</th><th>Name</th><th>Team</th><th>Kills</th><th>Deaths</th>
                    <th>Assists</th><th>Triples</th><th>Quadras</th>
                    <th>Pentas</th><th>CS</th><th>Total</th><th>Games</th></tr>
                    """
        total = 0
        
        
        for role in user1.roles:
            player_name = user1.roles[role]
            player = all_players[player_name]
            score = player.scores[week]
            text += "<tr><th>" + str(player.role) + "</th><th>" + str(player_name) + "</th><th>" + str(player.team) \
                + "</th><th>" + str(score.kills) + "</th><th>" + str(score.deaths) + "</th><th>" + str(score.assists) \
                + "</th><th>" + str(score.triples) + "</th><th>" + str(score.quadras) + "</th><th>" + str(score.pentas) \
                + "</th><th>" + str(score.cs) + "</th><th>" + str(score.total) + "</th><th>" + str(score.games) \
                + "</th></tr>"
            
            if role != "Bench":
                total += score.total

        text += "</table></div><h4>" + "Team Score: " + str(round(total, 2)) +"</h4></div>"

        #Player 2
        text += """<div class="team team-two">
                <h3>"""
        text += user2.name
        text += """</h3>
                <div class ="players">
                <table class="table">
    """
        text += """<tr>
                    <th>Role</th><th>Name</th><th>Team</th><th>Kills</th><th>Deaths</th>
                    <th>Assists</th><th>Triples</th><th>Quadras</th>
                    <th>Pentas</th><th>CS</th><th>Total</th><th>Games</th></tr>
                    """
        total = 0
        
        for role in user2.roles:
            player_name = user2.roles[role]
            player = all_players[player_name]
            score = player.scores[week]
            text += "<tr><th>" + str(player.role) + "</th><th>" + str(player_name) + "</th><th>" + str(player.team) \
                + "</th><th>" + str(score.kills) + "</th><th>" + str(score.deaths) + "</th><th>" + str(score.assists) \
                + "</th><th>" + str(score.triples) + "</th><th>" + str(score.quadras) + "</th><th>" + str(score.pentas) \
                + "</th><th>" + str(score.cs) + "</th><th>" + str(score.total) + "</th><th>" + str(score.games) \
                + "</th></tr>"
            
            if role != "Bench":
                total += score.total

        text += "</table></div><h4>" + "Team Score: " + str(round(total, 2)) +"</h4></div></div>"

    text += "</div></body></html>"

    soup = BeautifulSoup(text, 'html.parser')
    formatter = HTMLFormatter(indent=4)
    soup_str = str(soup.prettify(formatter=formatter))
    file_html.write(soup_str)
    file_html.close()