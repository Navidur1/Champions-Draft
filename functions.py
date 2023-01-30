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
            
    for i in range(8):
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
    
    for i in range(8):
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

def build_matchup_html(all_players:dict, users:dict, week):
    file_name = "/tmp/matchups/week" + str(week) + ".html"
    file_html = open(file_name, "w+")
    total = 0

    text = """<!DOCTYPE html>
            <html>
            <head>
            <style>
                .matchup-container {
                display: flex;
                align-items: center;
                justify-content: center;
                }
                .matchup {
                display: flex;
                flex-wrap: wrap;
                }
                .team {
                width: 600px;
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
                width: 550px;
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
            </style>
            </head>
            <body>
            <div class="matchup-container">
                <div class="matchup">
                <div class="team team-one">
"""
    #Player 1
    text += """<h3>Navid</h3>
            <div class ="players">
            <table style="width:100%">
"""
    text += """<tr>
                <th>Role</th><th>Name</th><th>Kills</th><th>Deaths</th>
                <th>Assists</th><th>Triples</th><th>Quadras</th>
                <th>Pentas</th><th>CS</th><th>Total</th><th>Games</th></tr>
                """
    total = 0
    for role in users["Navid"]:
        player_name = users["Navid"][role]
        player = all_players[player_name]
        score = player.scores[week]
        text += "<tr><th>" + str(player.role) + "</th><th>" + str(player_name) + "</th><th>" + str(player.team) \
             + "</th><th>" + str(score.kills) + "</th><th>" + str(score.deaths) + "</th><th>" + str(score.assists) \
             + "</th><th>" + str(score.triples) + "</th><th>" + str(score.quadras) + "</th><th>" + str(score.pentas) \
             + "</th><th>" + str(score.cs) + "</th><th>" + str(score.total) + "</th><th>" + str(score.games) \
             + "</th></tr>"
        
        if role != "Bench":
            total += score.total

    # top = users["Navid"]["top"]
    # top_score = all_players[top].scores[week].total
    # text += "Top: " + top + " <span>Score: " + str(top_score) + "</span></h4></div>"
    
    # text += """<div class="player"><h4>"""
    # jg = users["Navid"]["jg"]
    # jg_score = all_players[jg].scores[week].total
    # text += "JG: " + jg + " <span>Score: " + str(jg_score) + "</span></h4></div>"
    
    # text += """<div class="player"><h4>"""
    # mid = users["Navid"]["mid"]
    # mid_score = all_players[mid].scores[week].total
    # text += "Mid: " + mid + " <span>Score: " + str(mid_score) + "</span></h4></div>"
    
    # text += """<div class="player"><h4>"""
    # adc = users["Navid"]["adc"]
    # adc_score = all_players[adc].scores[week].total
    # text += "ADC: " + top + " <span>Score: " + str(adc_score) + "</span></h4></div>"
    
    # text += """<div class="player"><h4>"""
    # supp = users["Navid"]["supp"]
    # supp_score = all_players[supp].scores[week].total
    # text += "Support: " + supp + " <span>Score: " + str(supp_score) + "</span></h4></div>"
    
    # text += """<div class="player"><h4>"""
    # bench = users["Navid"]["bench"]
    # bench_score = all_players[bench].scores[week].total
    # text += "Bench: " + bench + " <span>Score: " + str(bench_score) + "</span></h4></div>"

    # total += top_score + jg_score + mid_score + adc_score + supp_score

    text += """</table></div></div>"""

    #Player 2
    text += """<div class="team team-two">
            <h3>Adam</h3>
            <div class ="players">
"""
    text += """<div class="player"><h4>"""
    top = users["Adam"]["Top"]
    top_score = all_players[top].scores[week].total
    text += "Top: " + top + " <span>Score: " + str(top_score) + "</span></h4></div>"
    
    text += """<div class="player"><h4>"""
    jg = users["Adam"]["JG"]
    jg_score = all_players[jg].scores[week].total
    text += "JG: " + jg + " <span>Score: " + str(jg_score) + "</span></h4></div>"
    
    text += """<div class="player"><h4>"""
    mid = users["Adam"]["Mid"]
    mid_score = all_players[mid].scores[week].total
    text += "Mid: " + mid + " <span>Score: " + str(mid_score) + "</span></h4></div>"
    
    text += """<div class="player"><h4>"""
    adc = users["Adam"]["ADC"]
    adc_score = all_players[adc].scores[week].total
    text += "ADC: " + top + " <span>Score: " + str(adc_score) + "</span></h4></div>"
    
    text += """<div class="player"><h4>"""
    supp = users["Adam"]["Support"]
    supp_score = all_players[supp].scores[week].total
    text += "Support: " + supp + " <span>Score: " + str(supp_score) + "</span></h4></div>"
    
    text += """<div class="player"><h4>"""
    bench = users["Adam"]["Bench"]
    bench_score = all_players[bench].scores[week].total
    text += "Bench: " + bench + " <span>Score: " + str(bench_score) + "</span></h4></div>"

    total += top_score + jg_score + mid_score + adc_score + supp_score

    text += """<div class="team-score"><h4>Total Score: """ + str(total) + "</h4></div></div></div></div></body></html>"

    soup = BeautifulSoup(text, 'html.parser')
    formatter = HTMLFormatter(indent=4)
    soup_str = str(soup.prettify(formatter=formatter))
    file_html.write(soup_str)
    file_html.close()


def build_index():
    file_name = "/tmp/index.html"
    file_html = open(file_name, "w+")

    text= '''
    <!DOCTYPE html>
<html>

<head>
    <style>
        table {
            border-collapse: collapse;
            margin-bottom: 30px;
        }

        th {
            background-color: green;
            Color: white;
        }

        th,
        td {
            width: 150px;
            text-align: center;
            border: 1px solid black;
            padding: 5px
        }

        .col {
            font-weight: bold;
        }

        h1 {
            color: black;
        }
    </style>
    <title>
        Champions Draft
    </title>
</head>

<body>
    <center>
        <h1>Champions Draft</h1>
        <table>
            <tr>
                <td class="col">Matchups</td>
                <td><a href="https://glassy-clock-375119.ue.r.appspot.com/matchup/week1">Week 1</a></td>
                <td><a href="https://glassy-clock-375119.ue.r.appspot.com/matchup/week2">Week 2</a></td>
                <td><a href="https://glassy-clock-375119.ue.r.appspot.com/matchup/week3">Week 3</a></td>
                <td><a href="https://glassy-clock-375119.ue.r.appspot.com/matchup/week4">Week 4</a></td>
                <td><a href="https://glassy-clock-375119.ue.r.appspot.com/matchup/week5">Week 5</a></td>
                <td><a href="https://glassy-clock-375119.ue.r.appspot.com/matchup/week6">Week 6</a></td>
                <td><a href="https://glassy-clock-375119.ue.r.appspot.com/matchup/week7">Week 7</a></td>
                <td><a href="https://glassy-clock-375119.ue.r.appspot.com/matchup/week8">Week 8</a></td>
            </tr>
            <tr>
                <td class="col">Player Data</td>
                <td><a href="https://glassy-clock-375119.ue.r.appspot.com/players/week1">Week 1</a></td>
                <td><a href="https://glassy-clock-375119.ue.r.appspot.com/players/week2">Week 2</a></td>
                <td><a href="https://glassy-clock-375119.ue.r.appspot.com/players/week3">Week 3</a></td>
                <td><a href="https://glassy-clock-375119.ue.r.appspot.com/players/week4">Week 4</a></td>
                <td><a href="https://glassy-clock-375119.ue.r.appspot.com/players/week5">Week 5</a></td>
                <td><a href="https://glassy-clock-375119.ue.r.appspot.com/players/week6">Week 6</a></td>
                <td><a href="https://glassy-clock-375119.ue.r.appspot.com/players/week7">Week 7</a></td>
                <td><a href="https://glassy-clock-375119.ue.r.appspot.com/players/week8">Week 8</a></td>
            </tr>
        </table>
        <form method="post">
            <input type="button" id='script' name="submit" value="Refresh">
        </form>
    </center>
</body>

</html>
    
    '''
    soup = BeautifulSoup(text, 'html.parser')
    formatter = HTMLFormatter(indent=4)
    soup_str = str(soup.prettify(formatter=formatter))
    file_html.write(soup_str)
    file_html.close()