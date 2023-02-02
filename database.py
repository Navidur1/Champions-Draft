from scrape import all_players
from google.cloud import firestore
from google.cloud import storage 

def init_database():
    db = firestore.Client(project='champions-draft')
    return db

def get_week(db):
    get_week = db.collection(u'info').document(u'meta_data').get()
    meta_data = get_week.to_dict()
    return meta_data['week']

#Store all players
def write_data():
    db = init_database()
    week = get_week(db)
    print(week)

    doc_ref = db.collection(u'all_players').document(str(week))

    for p in all_players:
        player = all_players[p]
        score = player.scores[week]
        player_doc = {
            player.name:{
                u'name':player.name,
                u'role':u'ADC',
                u'team':u'TSM',
                u'score':{
                    u'assists': score.assists,
                    u'cs':score.cs,
                    u'deaths':score.deaths,
                    u'games':score.games,
                    u'kills':score.kills,
                    u'pentas':score.pentas,
                    u'quadras':score.quadras,
                    u'total':score.total,
                    u'triples':score.triples
                }
            }
        }
        
        doc_ref.set(player_doc)
        break