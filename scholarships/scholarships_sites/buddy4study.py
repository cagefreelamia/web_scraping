import requests

headers = {
    'authority': 'api.buddy4study.com',
    'accept': 'application/json',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZSI6WyJyZWFkIiwid3JpdGUiLCJ0cnVzdCJdLCJleHAiOjE2OTkxOTU1NDUsImF1dGhvcml0aWVzIjpbIlVTRVIiXSwianRpIjoiM2ZmNzA5OTYtZjc4NS00MjQyLTk1YTgtMDdkMjUzZTRjOWNhIiwiY2xpZW50X2lkIjoiYjRzIn0.QC47Lwr8svIC_Vyp2oAyMFb8XAKb46WQYAYVkJbZjLA',
    # Already added when you pass json=
    # 'content-type': 'application/json',
    'origin': 'https://www.buddy4study.com',
    'referer': 'https://www.buddy4study.com/',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}

json_data = {
    'page': 0,
    'length': 100,
    'rules': [
        {
            'rule': [
                260,
                282,
                254,
                288,
                270,
                283,
                298,
                299,
                301,
                1056,
                1057,
                1055,
                278,
                296,
                263,
                122,
                123,
                124,
                125,
            ],
        },
    ],
    'mode': 'OPEN',
    'sortOrder': 'DEADLINE',
}

response = requests.post('https://api.buddy4study.com/api/v1.0/ssms/scholarship/', headers=headers, json=json_data)
re = response.json()

data = re['scholarships']


scholarships = []


for el in data:
    temp = [el['scholarshipName'], el['deadlineDate'], el['scholarshipMultilinguals'][0]['applicableFor'], 'https://buddy4study.com/'+el['pageSlug'], el['logoFid']]
    scholarships.append(temp)

#print(len(scholarships))
for x in scholarships:
    print(f'SCHOLARSHIP NAME : {x[0]}')
    print(f'SCHOLARSHIP LAST DATE : {x[1]}')
    print(f'SCHOLARSHIP APPLICABLE FOR : {x[2]}')
    print(f'SCHOLARSHIP LINK : {x[3]}')
    print(f'SCHOLARSHIP IMAGE LINK : {x[4]}')
    print('-------------------------------------------------------------------------------')