NUM_WEEKS = 8

#SCORE CONSTANTS
KILLS_SCORE = 3
DEATHS_SCORE = -1
ASSISTS_SCORE = 2
CS_SCORE = 0.02
TRIPLES_SCORE = 2
QUADRAS_SCORE = 4
PENTAS_SCORE = 7

APP_URL = "https://glassy-clock-375119.ue.r.appspot.com/"

class Player:
	def __init__(self, name: str, team=None, role=None):
		self.name = name
		self.team = team
		self.role = role
		self.scores = [None] * (NUM_WEEKS + 1)

	def __str__(self):
		return (f"Name: {self.name}\n"
				f"Team: {self.team}\n"
				f"{self.scores}")

class Users:
	def __init__(self, name):
		self.top = None
		self.jg = None
		self.mid = None
		self.adc = None
		self.supp = None
		self.util = None

		self.schedule = [None] * 8
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
		self.triples = 0
		self.quadras = 0
		self.pentas = 0
		self.cs = 0
		self.total = 0
		self.games = 0

	def update(self):
		total = self.kills * KILLS_SCORE \
					+ self.deaths * DEATHS_SCORE \
					+ self.assists * ASSISTS_SCORE \
					+ self.cs * CS_SCORE \
					+ self.triples * TRIPLES_SCORE \
					+ self.quadras * QUADRAS_SCORE \
					+ self.pentas * PENTAS_SCORE

		if self.games > 2:
			total *= 2/self.games
			
		self.total = round(total, 2)

	def __str__(self):
		return (f"Kills: {self.kills}\n"
				f"Deaths: {self.deaths}\n"
				f"Assists: {self.assists}\n"
				f"CS: {self.cs}\n"
				f"Triples: {self.triples}\n"
				f"Quadras: {self.quadras}\n"
				f"Pentas: {self.pentas}\n"
				f"Total: {self.total}\n")
               


    

  


    