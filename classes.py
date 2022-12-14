NUM_WEEKS = 8
class Player:
  def __init__(self, name, team=None):
    self.name = name
    self.team = team
    self.point = [None] * NUM_WEEKS

class Users:
  def __init__(self, name):
    self.top = None
    self.jg = None
    self.mid = None
    self.adc = None
    self.supp = None
    self.util = None
    self.bench1 = None
    self.bench2 = None

    self.wins = 0
    self.losses = 0

    self.points_for = 0
    self.points_against = 0
    
class Team:
  def __init__(self, name, top=None, jg=None, mid=None, adc=None, supp=None):
    self.name = name
    self.top = top
    self.jg = jg
    self.mid = mid
    self.adc = adc
    self.supp = supp

class Score:
  def __init__(self):
    self.kills = 0
    self.deaths = 0
    self.assists = 0
    self.first_bloods = 0
    self.triples = 0
    self.quadras = 0
    self.pentas = 0
    self.cs = 0
    self.total = 0
    
  def update(self, kills, deaths, assists, first_bloods, triples, quadras, pentas, cs):
    self.kills += kills
    self.deaths += deaths
    self.assists += assists
    self.first_bloods += first_bloods
    self.triples += triples
    self.quadras += quadras
    self.pentas += pentas
    self.cs += cs
    self.total = self.kills + self.deaths + self.assists + self.first_bloods + self.triples +                        self.quadras + self.pentas + self.cs


    

  


    