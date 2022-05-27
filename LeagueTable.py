from bs4 import BeautifulSoup
import requests, openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'League Table'
sheet.append(
    ['Position', 'Club Name', 'Game Played', "Game won", 'GAme drawn', 'Game lost', 'GF', 'GA', 'GD', 'Total point'])

try:
    league = requests.get('https://www.skysports.com/premier-league-table')
    soup = BeautifulSoup(league.text, 'html.parser')
    result = soup.find('tbody').find_all('tr', class_="standing-table__row")

    for item in result:
        list = item.find_all('td')
        rank = item.find_all('td')[0].text
        club = item.find_all('td')[1].get_text(strip=True)
        play = item.find_all('td')[2].text
        won = item.find_all('td')[3].text
        draw = item.find_all('td')[4].text
        lost = item.find_all('td')[5].text
        FG = item.find_all('td')[6].text
        AD = item.find_all('td')[7].text
        GD = item.find_all('td')[8].text
        point = item.find_all('td')[9].text
        print(rank, club, play, won, draw, lost, FG, AD, GD, point)
        sheet.append([rank, club, play, won, draw, lost, FG, AD, GD, point])

except Exception as e:
    print(e)
