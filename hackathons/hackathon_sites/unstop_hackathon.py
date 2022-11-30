import requests
from csv import writer

cookies = {
    # '_gcl_au': '1.1.324447386.1667389202',
    # '_gid': 'GA1.2.99191914.1667389202',
    # '_scid': '2dbbf7ad-cf6b-4890-a203-30f5f51649ed',
    # '_fbp': 'fb.1.1667389202681.553366206',
    # 'g_state': '{"i_l":0}',
    # 'allowedCookie': '1',
    # '_clck': 'd7tobp|1|f69|0',
    # '_ga_98GC4MBLXM': 'GS1.1.1667440344.6.1.1667440369.35.0.0',
    # '_ga': 'GA1.2.866513608.1667389202',
    # '_clsk': 'uln4rg|1667440370954|2|1|i.clarity.ms/collect',
}

headers = {
    'authority': 'unstop.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIyIiwianRpIjoiNDNmMjMzNjAwMTQ4MGMwNzk1YzhmNDg4NWFjNzRiODkwNzM2YTIwNTc2NDI4N2RmMGI5NzY3ZWUzNjcyNTkxNTExYmI5ZWQ0ZjY0NGE4NWUiLCJpYXQiOjE2NjczODkyMTguNzk3Mjg5LCJuYmYiOjE2NjczODkyMTguNzk3MjkyLCJleHAiOjE2Njg1OTg4MTguNzg0ODE0LCJzdWIiOiI0MTY3MTQ4Iiwic2NvcGVzIjpbXX0.QzMhVgCRd_WjvniRcFqApSVWGw_iNAAwRL9GPD6FsOxOvZ-HlAjBt5j1coDC4YgzfMvH_Bl2KYsduhtypDND7OF4zzdKA8bWi-Ko-9epI_X9ZWSKm1AUjHjsjtBnZa0LcqJOT00xTpLNTF2badnkb1eSTE5oJ3RPV_X-E0rUPAnowlTcxt6Dlh4B1xrx3fx2yOpfIpuXj5ybQd-ESCFW027surpHj7za2DOEvqbzUCbAZyWoWu9DHESTHYyBjPaoH3_LqEtrViB3oNhBCmKoBGhRjSruBNnW3Q-XOsDS5P8sy6oYaDMNP1HIOSJIUQnILx6RzJ5lu7cof-OEBrkny1_prm_I2NWZkOHkIh_3z72v0um2VD1KkURAmJ857FMRWOP-PAfyDjRlMnQ_QQwLAuWNIx7wRz0pqKdi2AQsfcUOTDCWLm3I1vItg4Kt2nKbdllWh1OIqroTYqO2u579v5oiHSYCzgTHCKr7_qgcAo0botMSXdnS0s-kezXNKHWeM7d8CxR5tJQH5U5DnuHtNkrfzoI9znyzQipAqDLHcHvGdc8wLhe5fZ3aA7SaDcwhUt9b7va4HjkVEi6wqncN2ZFaYw2swUt42Uw9MInzf-HesquG6WQqtaidmB9_tLjHT3bfT36rV4geOilVue3bdweyDSYSXXM6_lrJv7Zn9oM',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_gcl_au=1.1.324447386.1667389202; _gid=GA1.2.99191914.1667389202; _scid=2dbbf7ad-cf6b-4890-a203-30f5f51649ed; _fbp=fb.1.1667389202681.553366206; g_state={"i_l":0}; allowedCookie=1; _clck=d7tobp|1|f69|0; _ga_98GC4MBLXM=GS1.1.1667440344.6.1.1667440369.35.0.0; _ga=GA1.2.866513608.1667389202; _clsk=uln4rg|1667440370954|2|1|i.clarity.ms/collect',
    'referer': 'https://unstop.com/hackathons?filters=all,,all,all&types=oppstatus,teamsize,payment,eligible',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}

params = {
    'opportunity': 'hackathons',
    'filters': 'All,,All,All',
    'types': 'oppstatus,teamsize,payment,eligible',
    'atype': 'explore',
    'showOlderResultForSearch': 'true',
    'page': '1',
}

response = requests.get('https://unstop.com/api/public/opportunity/search-new', params=params, cookies=cookies, headers=headers)

re = response.json()
data = re['data']['data']
hackathons = []

for x in data:
    temp = [x['title'], x['seo_url'], x['logoUrl2'], x['end_date']]
    hackathons.append(temp)

# with open("hackathons.csv", 'w', encoding='utf8', newline='') as f:
#     the_writer = writer(f)
#     header = ["Hackathon", 'Hackathon Links', "Hackathon Image Link", 'Hackathon End Date']
#     the_writer.writerow(header)
#     for hack in hackathons:
#         print(f'Hackathon : {hack[0]}')
#         print(f'Hackathon Link : {hack[1]}')
#         print(f'Hackathon Image Link : {hack[2]}')
#         print(f'Hackathon End Date : {hack[3]}')
#         print("---------------------------------------------------------------------------------------------------------------------")
#         info = [hack[0], hack[1], hack[2], hack[3]]
#         the_writer.writerow(info)
