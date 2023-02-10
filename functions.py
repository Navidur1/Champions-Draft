#build html based on pulled player data
from classes import *
from scrape import roles, users
from bs4 import BeautifulSoup
from bs4.formatter import *

def build_index():
    file_name = "/tmp/index.html"
    file_html = open(file_name, "w+")

    text= '''
    <!DOCTYPE html>
<html>

<head>
    <title>
        Champions Draft
    </title>
    <link rel="stylesheet" href="static/css/main.css">
</head>

<body>
    <div class="center">
        <h1>Champions Draft</h1>
        <table>
            <tr>
                <td class="col">Matchups</td>
                <td><a href="matchups/week1">Week 1</a></td>
                <td><a href="matchups/week2">Week 2</a></td>
                <td><a href="matchups/week3">Week 3</a></td>
                <td><a href="matchups/week4">Week 4</a></td>
                <td><a href="matchups/week5">Week 5</a></td>
                <td><a href="matchups/week6">Week 6</a></td>
            </tr>
            <tr>
                <td class="col">Player Data</td>
                <td><a href="players/week1">Week 1</a></td>
                <td><a href="players/week2">Week 2</a></td>
                <td><a href="players/week3">Week 3</a></td>
                <td><a href="players/week4">Week 4</a></td>
                <td><a href="players/week5">Week 5</a></td>
                <td><a href="players/week6">Week 6</a></td>
            </tr>
        </table>
        <form method="post">
            <input type="button" id='script' name="submit" value="Refresh">
        </form>
    </div>
</body>

</html>
    
    '''
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
            <head>
                <title>
                    Champions Draft
                </title>
                <link rel="stylesheet" href="../static/css/main.css">
            </head>
            <body>
            <div class="center">
                <h1>Champions Draft</h1>
                <table>
                    <tr>
                        <td class="col">Matchups</td>
                        <td><a href="../matchups/week1">Week 1</a></td>
                        <td><a href="../matchups/week2">Week 2</a></td>
                        <td><a href="../matchups/week3">Week 3</a></td>
                        <td><a href="../matchups/week4">Week 4</a></td>
                        <td><a href="../matchups/week5">Week 5</a></td>
                        <td><a href="../matchups/week6">Week 6</a></td>
                    </tr>
                    <tr>
                        <td class="col">Player Data</td>
                        <td><a href="week1">Week 1</a></td>
                        <td><a href="week2">Week 2</a></td>
                        <td><a href="week3">Week 3</a></td>
                        <td><a href="week4">Week 4</a></td>
                        <td><a href="week5">Week 5</a></td>
                        <td><a href="week6">Week 6</a></td>
                    </tr>
                </table>
            </div>
            <h2>LCS Players</h2>
            <table class="data">
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

def build_matchup_html(schedule, all_players:dict, week):
    file_name = "/tmp/matchups/week" + str(week) + ".html"
    file_html = open(file_name, "w+")
    total = 0
    matchups = schedule[week]

    text = """<!DOCTYPE html>
            <html>
            <head>
                <title>
                    Champions Draft
                </title>
                <link rel="stylesheet" href="../static/css/main.css">
            </head>
            <body>
            <div class="center">
                <h1>Champions Draft</h1>
                <table>
                    <tr>
                        <td class="col">Matchups</td>
                        <td><a href="week1">Week 1</a></td>
                        <td><a href="week2">Week 2</a></td>
                        <td><a href="week3">Week 3</a></td>
                        <td><a href="week4">Week 4</a></td>
                        <td><a href="week5">Week 5</a></td>
                        <td><a href="week6">Week 6</a></td>
                    </tr>
                    <tr>
                        <td class="col">Player Data</td>
                        <td><a href="../players/week1">Week 1</a></td>
                        <td><a href="../players/week2">Week 2</a></td>
                        <td><a href="../players/week3">Week 3</a></td>
                        <td><a href="../players/week4">Week 4</a></td>
                        <td><a href="../players/week5">Week 5</a></td>
                        <td><a href="../players/week6">Week 6</a></td>
                    </tr>
                </table>
                <h2>Standings</h2>
                <table id="standings">
                    <thead>
                        <tr>
                        <th></th>
                        <th>Player</th>
                        <th>Wins</th>
                        <th>Losses</th>
                        <th>Points For</th>
                        <th>Points Against</th>
                        </tr>
                    </thead>
                    <tbody>
"""
    place = 1
    for user in sorted(users.values(), key=lambda x: (x.wins[week], x.points_for[week])):
        text += "<tr><td>" + str(place) + "</td><td>" + user.name + "</td><td>" + str(user.wins[week]) + "</td><td>" + str(user.losses[week]) + \
             "</td><td>" + str(round(sum(user.points_for[:week + 1]), 2)) + "</td><td>" + str(round(sum(user.points_against[:week + 1]), 2)) + "</td></tr>"

        place += 1

    text += """</tbody>
            </table>
            </div>

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
                <div class="players">
                <table class="data">
    """
        text += """<tr>
                    <th>Role</th><th>Name</th><th>Team</th><th>Kills</th><th>Deaths</th>
                    <th>Assists</th><th>Triples</th><th>Quadras</th>
                    <th>Pentas</th><th>CS</th><th>Total</th><th>Games</th></tr>
                    """
        total = 0
        
        
        for role in roles:
            player_name = user1.teams[week][role]
            player = all_players[player_name]
            score = player.scores[week]

            if score == None:
                continue
            
            text += "<tr><th>" + str(role) + "</th><th>" + str(player_name) + "</th><th>" + str(player.team) \
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
                <div class="players">
                <table class="data">
    """
        text += """<tr>
                    <th>Role</th><th>Name</th><th>Team</th><th>Kills</th><th>Deaths</th>
                    <th>Assists</th><th>Triples</th><th>Quadras</th>
                    <th>Pentas</th><th>CS</th><th>Total</th><th>Games</th></tr>
                    """
        total = 0
        
        for role in roles:
            player_name = user2.teams[week][role]
            player = all_players[player_name]
            score = player.scores[week]
            
            if score == None:
                continue

            text += "<tr><th>" + str(role) + "</th><th>" + str(player_name) + "</th><th>" + str(player.team) \
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
