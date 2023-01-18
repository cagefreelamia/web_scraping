from urllib.request import urlopen
from bs4 import BeautifulSoup

x = urlopen("https://www.hackerearth.com/challenges/hackathon/")
soup = BeautifulSoup(x.read(), 'lxml')
ongoing_hackathons = soup.find("div", {"class" : "ongoing challenge-list"})
hackathon_names = ongoing_hackathons.find_all("span", {"class" : "challenge-list-title challenge-card-wrapper"})
hackathon_images = list(map(lambda temp: temp["style"].replace("background-image: url('", "").replace("');", ""), ongoing_hackathons.find_all("div", {"class" : "event-image"})))
hackathon_links = ongoing_hackathons.find_all("a", {"class" : "challenge-card-wrapper challenge-card-link"})

hackathons = []

for i in range(len(hackathon_names)):
    hackathons.append([hackathon_names[i].get_text(), hackathon_links[i].get("href"), hackathon_images[i]])
    

for hack in hackathons:
    y = urlopen(hack[1])
    soup2 = BeautifulSoup(y.read(), 'lxml')
    find_end_dates = soup2.find("div", {"class" : "end-time-block"})
    hack.append(find_end_dates.find("div", {"class" : "regular bold desc dark"}).get_text())
    print(f'Hackathon : {hack[0]}')
    print(f'Hackathon Link : {hack[1]}')
    print(f'Hackathon Image Link : {hack[2]}')
    print(f'Hackathon End Date : {hack[3]}')
    print("---------------------------------------------------------------------------------------------------------------------")
