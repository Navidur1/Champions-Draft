#build html based on pulled player data
from classes import *
def build_player_html(all_players:dict):

    file_html = open("templates/player.html","w")

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
                <th>Name</th>
                <th>Team</th>
                <th>Kills</th>
                <th>Deaths</th>
                <th>Assists</th>
                <th>First Bloods</th>
                <th>Triples</th>
                <th>Quadras</th>
                <th>Pentas</th>
                <th>CS</th>
                <th>Total</th>
                <th>Games</th>
            </tr>"""
    
    for p in all_players:
        print(p)
        
        player = all_players[p]
        score = player.scores[1]
        
        if(score == None):
            continue

        line = "<tr><th>" \
        + p + "</th><th>" \
        + "Men" + "</th><th>" \
        + str(score.kills) + "</th><th>" \
        + str(score.deaths) + "</th><th>" \
        + str(score.assists) + "</th><th>" \
        + str(score.first_bloods) + "</th><th>" \
        + str(score.triples) + "</th><th>" \
        + str(score.quadras) + "</th><th>" \
        + str(score.pentas) + "</th><th>" \
        + str(score.cs) + "</th><th>" \
        + str(score.total) + "</th><th>" \
        + str(score.games) + "</th><th>" \
        +"</th></tr>"
        text += line

    text += """ 
            </table>
            </body>
            </html>"""

    print(text)
    file_html.write(text)
    file_html.close()