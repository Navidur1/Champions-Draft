from scrape import all_players, users, cur_week
from google.cloud import firestore
from google.cloud import storage 

def init_database():
    db = firestore.Client(project='champions-draft')
    return db

def get_week(db):
    week_dict = db.collection('info').document('meta_data').get().to_dict()
    return week_dict['week']

#Store all players
def write_data():
    db = init_database()

    # for name in all_players:
    #     doc_ref = db.collection('all_players').document(name)
    #     player = all_players[name]
    #     doc_ref.set(player.to_dict())

def read_data():
    db = init_database()

    cur_week = get_week(db)

    # docs = db.collection('all_players').stream()
    # for doc in docs:
    #     all_players[doc.id] = doc.to_dict()

    for user in users:
        doc_ref = db.collection('users').document(user)
        doc = doc_ref.get().to_dict()
        users[user].teams = doc['teams']
