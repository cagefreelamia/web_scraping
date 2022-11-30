import requests

session = requests.Session()

response = session.get("https://www.eventbrite.com/d/india/hackathons/")

cookies = session.cookies.get_dict()




headers = {
    'authority': 'www.eventbrite.com',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'mgrefby="https://www.google.com/"; G=v%3D2%26i%3D14167c2f-9deb-4b65-8e38-7434377b2f89%26a%3D106b%26s%3De81cc8b977797f4b53d9ae31bf9860b2598eeb38; ebEventToTrack=; SS=AE3DLHSoTGUR0zZtQWhX7NCNWrk3j_S_5A; eblang=lo%3Den_US%26la%3Den-us; AN=; AS=21679b2d-3339-4c2f-866d-c5890b876418; mgref=refsites; csrftoken=2603357a5b3c11ed9a52774f4d83bc02; _gid=GA1.2.1826180709.1667454943; _gcl_au=1.1.1796968696.1667454944; _fbp=fb.1.1667454943524.1735429612; ebGAClientId=1796936019.1667454943; _gat=1; _hp2_ses_props.1404198904=%7B%22r%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22ts%22%3A1667454944286%2C%22d%22%3A%22www.eventbrite.com%22%2C%22h%22%3A%22%2Fd%2Findia%2Fhackathons%2F%22%7D; __hstc=195498867.2909af266e7f959d5743e81257292bc3.1667454946566.1667454946566.1667454946566.1; hubspotutk=2909af266e7f959d5743e81257292bc3; __hssrc=1; __hssc=195498867.1.1667454946567; _pin_unauth=dWlkPU9XWTROR0ZrWW1ZdFpUTmtOQzAwWkRVM0xUZ3pNVFF0TTJVeE1UZzNOakV3WVRGaQ; ln_or=d; _ga_TQVES5V6SH=GS1.1.1667454946.1.0.1667454965.0.0.0; _ga=GA1.2.1796936019.1667454943; SP=AGQgbbk0ruS_-9JN21vixq8TpKHzr1N-4rmovjgskTHXzJCIkWdwj8Xzmva6HRdWn7bc18_4kN3M2tOsdXuFX5rHX_KRu1YhMkm2Pfvpe9Dkv0shGNfGzznrxIiPdA-BQqx_FhvG96jzNLXyy23rPKWmKcXN--3Lfcewq3mOs5xSISnl78JrU9IKM0QAY99t84cx6BDTLEXAgdIOj2IuSAYnjqRns1fzsV2kYeRdJPLnqtqz9JfzUPQ; _dd_s=rum=0&expire=1667455866719; _hp2_id.1404198904=%7B%22userId%22%3A%223235785017848290%22%2C%22pageviewId%22%3A%228741226918205364%22%2C%22sessionId%22%3A%225556250364968167%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D',
    'referer': 'https://www.eventbrite.com/d/india/hackathons/',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'x-csrftoken': '2603357a5b3c11ed9a52774f4d83bc02',
    'x-requested-with': 'XMLHttpRequest',
}

response = requests.get('https://www.eventbrite.com/api/v3/destination/events/?event_ids=426050637927,382911868707,449349405167,422024064337,409611829007,409611498017,409610815977,409612049667,409610324507,409611237237,401984214607,409610575257,402068556877,401881928667,402071585937,409805337797&expand=event_sales_status,image,primary_venue,saves,ticket_availability,primary_organizer,public_collections&page_size=20', cookies=cookies, headers=headers)
re = response.json()
data = re['events']

hackathons = []

for x in data:
    temp = [x['name'], x['url'], x['image']['url'], x['end_date']]
    hackathons.append(temp)

# for hack in hackathons:
#     print(f'Hackathon : {hack[0]}')
#     print(f'Hackathon Link : {hack[1]}')
#     print(f'Hackathon Image Link : {hack[2]}')
#     print(f'Hackathon End Date : {hack[3]}')
#     print("---------------------------------------------------------------------------------------------------------------------")