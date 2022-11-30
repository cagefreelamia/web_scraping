from hackathon_sites.unstop_hackathon import hackathons as list1
from hackathon_sites.eventbrite_hackathons import hackathons as list2
from hackathon_sites.HackerEarth_hackathon import hackathons as list3
from csv import writer

data = list1+list2+list3

with open("hackathons.csv", 'w', newline='') as f:
    the_writer = writer(f)
    header = ["Hackathon", 'Hackathon Links', "Hackathon Image Link", 'Hackathon End Date']
    the_writer.writerow(header)
    for hack in data:
        # print(f'Hackathon : {hack[0]}')
        # print(f'Hackathon Link : {hack[1]}')
        # print(f'Hackathon Image Link : {hack[2]}')
        # print(f'Hackathon End Date : {hack[3]}')
        # print("---------------------------------------------------------------------------------------------------------------------")
        info = [hack[0], hack[1], hack[2], hack[3]]
        the_writer.writerow(info)