import requests
from bs4 import BeautifulSoup

main_page_url = "https://gol.gg/tournament/tournament-matchlist/LCS%20Summer%202022/"
response = requests.get(main_page_url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find_all('tr')

for row in table:
  contents = row.contents
  if contents[4].text == "WEEK8":
    print(contents[0].a['href'])

